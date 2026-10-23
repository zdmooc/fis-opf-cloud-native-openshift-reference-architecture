# Flux OPF — mise à l'épreuve des règles métier dans le laboratoire

Les **états, contrôles d'autorisation, invariants d'idempotence, cas `UNKNOWN`, responsabilités et preuves financières** sont définis dans le [référentiel métier unique](https://github.com/zdmooc/banking-payments-business-architecture/blob/main/04-capacites-metier/ETATS_INVARIANTS.md) et la [gestion de dossiers paiement](https://github.com/zdmooc/banking-payments-business-architecture/blob/main/13-risques-fraude-operations/INVESTIGATIONS_CASE_MANAGEMENT.md).

La séquence fictive `RECEIVED → VALIDATED → ACCEPTED → DISPATCHED → {SETTLED | REJECTED | PENDING_RECONCILIATION}` est **une projection d'adaptateur à tester**, pas une machine normative EPC, ni la machine d'état attestée d'un module FIS OPF.

## Matrice de tests de la cible OPF/OpenShift — exigences de démonstration

| ID de test | Simulation technique | Observation à produire |
|---|---|---|
| BR-01 | Propager une référence métier à travers l'adaptateur | Lookup complet avant/après transformation |
| BR-02 | Répéter une requête et injecter deux consommateurs concurrents | Identité de commande et absence d'effet synthétique supplémentaire |
| BR-03 | Perdre la réponse HTTP après commit simulé | Relecture de la même commande ; aucune conclusion `FAILED` sans preuve |
| BR-04 | Obtenir seulement un ACK MQ/HTTP | Ne pas afficher un règlement comme prouvé |
| BR-05 | Simuler une réponse interbancaire perdue | État incertain, case/inquiry, aucune émission financière nouvelle aveugle |
| BR-06 | Corriger un message après statut settled fictif | Tracer l'original et l'opération de correction, sans écrasement |
| BR-07 | Injecter des champs de message perdus/versions IG incompatibles | Rejet de mapping et bilan de perte, pas conversion silencieuse |
| BR-08 | Changer configuration VoP/fraude/compliance d'un scénario fictif | Vérifier point de contrôle défini par la politique, pas une chaîne universelle inventée |
| BR-09 | Injecter des horodatages de fuseaux / sources distincts | Corrélation temporelle et signalement de dérive |
| BR-10 | Forcer un écart ordre/ledger/rail synthétique | Écart visible, propriétaire, preuve et correction sous autorisation |

Ces dix cas testent des **invariants génériques du laboratoire** ; ils ne certifient ni produit FIS, ni SCT Inst, ni réglementations.

## Contrôles de réalisation

Le contrat d'architecture doit préciser : propriétaire de règles, version de mapping et d'API, dates d'effet, preuves de test nominal/négatif, journaux et métriques, séparation opérateur/décideur financier, et plan de reprise contrôlée des adaptateurs. Les mises à jour sensibles exigent une revue adaptée, éventuellement à quatre yeux selon le cadre.

[Version intégrale historique](https://github.com/zdmooc/fis-opf-cloud-native-openshift-reference-architecture/blob/e829ec9229b7f362b02d77e6953d5e02f8c46843/docs/01-fonctionnel/flux-metier.md).
