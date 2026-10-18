# POC pédagogique de façade, jamais un logiciel FIS OPF

## Objet et limites

Mock HTTP développé en Python standard library pour matérialiser l'API idempotente au niveau **du processus unique en mémoire**, illustrer le design d'une image conteneur non-root et les manifests OpenShift. **Aucune persistance**, aucune transaction, aucune conformité bancaire, aucun rail, aucun compte, aucune fonction FIS. Ne pas utiliser en production ni pour tester une migration FIS.

## Démarrage local

```bash
python3 poc/mock_app.py
curl -s http://localhost:8080/health
curl -i -X POST http://localhost:8080/demo/v1/payments -H 'Content-Type: application/json' -H 'Idempotency-Key: EXAMPLE-0000001' -d '{"reference":"DEMO-1","amountMinor":1234,"currency":"EUR"}'
```

Le mock retourne `202 Accepted` avec `ACCEPTED_SYNTHETIC`, **jamais `SETTLED`**. Pour publier sur OCP, construire en interne l'image du laboratoire, la pousser dans un registre privé autorisé, remplacer l'image `example.invalid`, valider politiques sécurité, puis seulement étudier l'application des manifests. Aucun manifest livré ne constitue une installation OPF.

```bash
oc kustomize poc/openshift/overlays/lab  # inspection locale, sans mutation
# oc apply -k poc/openshift/overlays/lab # seulement après revue et image valide
```
