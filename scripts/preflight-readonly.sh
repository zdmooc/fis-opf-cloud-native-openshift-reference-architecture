#!/usr/bin/env bash
# WARNING: read-only discovery. Requires oc authenticated; no secrets read, no mutations.
set -euo pipefail
NS="${1:-}"
if [[ -z "$NS" ]]; then echo 'Usage: ./scripts/preflight-readonly.sh <authorized-namespace>' >&2; exit 2; fi
command -v oc >/dev/null || { echo 'oc is required' >&2; exit 3; }
case "$NS" in *[!a-z0-9-]*) echo 'Unexpected namespace characters' >&2; exit 4;; esac
printf 'Context: ';oc config current-context
printf '\nProject (non-sensitive metadata):\n';oc get namespace "$NS" -o custom-columns=NAME:.metadata.name,STATUS:.status.phase
printf '\nWorkloads:\n';oc -n "$NS" get deploy,sts,ds -o wide
printf '\nPod phases:\n';oc -n "$NS" get pods -o custom-columns=NAME:.metadata.name,PHASE:.status.phase,NODE:.spec.nodeName
printf '\nServices:\n';oc -n "$NS" get svc
printf '\nPod disruption budgets:\n';oc -n "$NS" get pdb
printf '\nNetwork policies:\n';oc -n "$NS" get networkpolicy
printf '\nChecks done; no mutation performed.\n'
