# Publication GitHub privée — commande utilisateur

La connexion GitHub utilisée pour préparer cette architecture permet l'accès aux repositories existants, mais ne propose pas de création d'un nouveau repository. La publication distante n'a pas été effectuée.

## Sur un poste où Git et GitHub CLI sont authentifiés

1. Extraire l'archive ZIP puis ouvrir Git Bash **dans le dossier racine**.
2. Exécuter `bash scripts/publier-github.sh`.
3. Vérifier dans GitHub la visibilité **Private**, les fichiers et la réussite de `.github/workflows/quality.yml`.

Le script crée `zdmooc/fis-opf-cloud-native-openshift-reference-architecture` en **privé**, et le premier commit, à condition qu'un dépôt de ce nom n'existe pas déjà et que les droits GitHub soient suffisants. Il ne transmet aucun fichier hors du dossier de ce dépôt.

## Mode manuel

```bash
cd fis-opf-cloud-native-openshift-reference-architecture
python3 scripts/audit_repo.py
python3 -m unittest discover -s tests -v
git init -b main
git add .
git commit -m "docs: FIS OPF cloud-native OpenShift reference architecture"
gh repo create zdmooc/fis-opf-cloud-native-openshift-reference-architecture --private --source . --remote origin --push
```

Aucune URL publique ne doit être annoncée avant vérification de la création effective du dépôt GitHub.
