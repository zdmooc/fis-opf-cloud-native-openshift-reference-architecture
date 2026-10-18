#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
OWNER_REPO="zdmooc/fis-opf-cloud-native-openshift-reference-architecture"
command -v gh >/dev/null || { echo 'Installer/authentifier gh sur le poste local'; exit 2; }
command -v git >/dev/null || { echo 'Installer git sur le poste local'; exit 2; }
gh auth status >/dev/null
if command -v python3 >/dev/null 2>&1; then PY=python3; elif command -v python >/dev/null 2>&1; then PY=python; else echo 'Python 3 requis'; exit 5; fi
"$PY" scripts/audit_repo.py
"$PY" -m unittest discover -s tests -v
if [[ ! -d .git ]]; then git init -b main; fi
if git remote get-url origin >/dev/null 2>&1; then
  echo 'origin existe : vérifier manuellement avant toute publication.' >&2; exit 3
fi
if gh repo view "$OWNER_REPO" >/dev/null 2>&1; then
  echo 'Le dépôt existe déjà : vérification manuelle nécessaire.' >&2; exit 4
fi
git add .
git commit -m 'docs: FIS OPF cloud-native OpenShift reference architecture'
gh repo create "$OWNER_REPO" --private --source . --remote origin --push
printf '
Contrôle de visibilité :
';gh repo view "$OWNER_REPO" --json nameWithOwner,isPrivate,url
