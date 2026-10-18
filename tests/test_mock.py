"""Synthetic facade regression; this is not a vendor or payment certification."""
import sys, pathlib, unittest
sys.path.insert(0,str(pathlib.Path(__file__).parents[1]/'poc'))
import mock_app
class TestSynthetic(unittest.TestCase):
    def setUp(self): mock_app.state.clear()
    def test_idempotency(self):
        inp={'reference':'DEMO','amountMinor':1234,'currency':'EUR'}
        c1,a=mock_app.make_instruction('EXAMPLE-12345',inp)
        c2,b=mock_app.make_instruction('EXAMPLE-12345',dict(inp))
        self.assertEqual((c1,c2),(202,202));self.assertEqual(a,b)
        self.assertEqual(a['status'],'ACCEPTED_SYNTHETIC')
    def test_conflicting_retry(self):
        a={'reference':'DEMO','amountMinor':1234,'currency':'EUR'}
        b={'reference':'DEMO','amountMinor':1235,'currency':'EUR'}
        mock_app.make_instruction('EXAMPLE-12345',a)
        self.assertEqual(mock_app.make_instruction('EXAMPLE-12345',b)[0],409)
    def test_reject_invalid(self):
        self.assertEqual(mock_app.make_instruction('EXAMPLE-12345',{'reference':'X','amountMinor':0,'currency':'EUR'})[0],400)
    def test_bool_amount_not_accepted(self):
        self.assertEqual(mock_app.make_instruction('EXAMPLE-12345',{'reference':'X','amountMinor':True,'currency':'EUR'})[0],400)
if __name__=='__main__':unittest.main()
