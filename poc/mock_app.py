#!/usr/bin/env python3
"""In-memory synthetic API; deliberately not a banking or vendor implementation."""
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
import json, hashlib, re, threading, uuid, os

state = {}
lock = threading.Lock()

def make_instruction(key, payload):
    if not isinstance(key, str) or not (8 <= len(key) <= 128):
        return 400, {"error": "invalid synthetic key"}
    if not isinstance(payload, dict) or not isinstance(payload.get('reference'), str) or not isinstance(payload.get('amountMinor'), int) or isinstance(payload.get('amountMinor'), bool) or payload['amountMinor'] < 1 or payload.get('currency') != 'EUR':
        return 400, {"error": "invalid synthetic instruction"}
    if len(payload['reference']) > 80:
        return 400, {"error": "invalid reference"}
    fp=hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    with lock:
        if key in state:
            first_fp, receipt=state[key]
            if fp != first_fp:
                return 409, {"error": "key reused with different data"}
            return 202, receipt
        receipt={"paymentId": "DEMO-"+uuid.uuid4().hex[:16], "status": "ACCEPTED_SYNTHETIC", "simulated": True}
        state[key]=(fp,receipt)
        return 202, receipt

class Handler(BaseHTTPRequestHandler):
    def send_json(self, code, data):
        raw=json.dumps(data).encode()
        self.send_response(code)
        self.send_header('Content-Type','application/json')
        self.send_header('Content-Length',str(len(raw)))
        self.send_header('Cache-Control','no-store')
        self.end_headers();self.wfile.write(raw)
    def do_GET(self):
        if self.path in ('/health','/ready'):
            return self.send_json(200,{"ok":True,"synthetic":True})
        if self.path.startswith('/demo/v1/payments/'):
            ident=self.path.removeprefix('/demo/v1/payments/')
            with lock:
                match=next((r for _,r in state.values() if r['paymentId']==ident),None)
            return self.send_json(200,match) if match else self.send_json(404,{"error":"not found"})
        return self.send_json(404,{"error":"not found"})
    def do_POST(self):
        if self.path != '/demo/v1/payments':return self.send_json(404,{"error":"not found"})
        try:
            n=int(self.headers.get('Content-Length','0'))
            if n<1 or n>4096:raise ValueError('invalid size')
            data=json.loads(self.rfile.read(n).decode())
        except (ValueError,UnicodeDecodeError, json.JSONDecodeError):
            return self.send_json(400,{"error":"invalid request"})
        code, result=make_instruction(self.headers.get('Idempotency-Key',''),data)
        return self.send_json(code,result)
    def log_message(self, fmt, *args):pass # avoid logging synthetic payloads

if __name__=='__main__':
    port=int(os.environ.get('PORT','8080'))
    print('LAB MOCK ONLY: no payments processed', flush=True)
    ThreadingHTTPServer(('0.0.0.0',port),Handler).serve_forever()
