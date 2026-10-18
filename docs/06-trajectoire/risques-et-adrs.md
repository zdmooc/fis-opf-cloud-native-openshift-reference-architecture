# Registre des risques et Architectural Decision Records

## Matrice de risques

| ID | Risque | P | I | Traitement | Test de vérification | Responsable |
|---|---|---|---|---|---|---|
| R01 | doublon de paiement après retry | H | Critique | idempotence/reconciliation | KO avant/après commit | Architecte métier |
| R02 | perte d'ordre accepté | H | Critique | durabilité/outbox | kill/power loss | Exploitant |
| R03 | version OPF non certifiée | M | Critique | support écrit FIS | preuve éditeur | Contrats |
| R04 | rolling incompatible schéma | M | Critique | migration compatible/toggle | N/N-1 test | DBA |
| R05 | goulot Oracle/MQ | H | Élevé | load test/backpressure | pointe batch+instant | Performance |
| R06 | cas ambigu SWIFT/rail | M | Critique | statut UNKNOWN/recon | double statut | Paiements |
| R07 | SCC/UID incompatibles | M | Élevé | packaging conforme | admission restrictive | Platform |
| R08 | secrets/logs PII exposés | M | Critique | SIEM masqué/rotation | DLP et access review | Sécurité |
| R09 | PRA incohérent DB/broker | M | Critique | restauration et rapprochement | full failover | SRE |
| R10 | licences non transposables | M | Élevé | approbation contractuelle | review FIS | Achats |
| R11 | règles de place obsolètes | M | Critique | rulebook tests | jeux négatifs | Conformité |
| R12 | dépendance IAM/DNS | H | Élevé | segment/probes/cache contrôlés | DNS/IAM chaos | Plateforme |

`P` et `I` sont appréciations préliminaires qualitatives ; il faut une méthode de cotation signée.

## Fiche ADR modèle

```
ID : ADR-XXX
Titre :
Date / Statut : PROPOSE | ACCEPTED | REJECTED | SUPERSEDED
Contexte métier et architecture :
Options examinées :
Choix et justification :
Impacts fonctionnels / données / sécurité / coûts / délais :
Propriétés transactionnelles et échecs :
Préconditions fournisseur et conformité :
Tests et preuves :
Rollback / durée de vie :
Approbateurs :
Date de réexamen :
```

## ADR-001 — Coexistence progressive

**Proposé** : découpler progressivement les canaux de l'exécution, migrer par famille de flux et n'avoir qu'un exécuteur propriétaire par ordre. Alternatives : big bang et coexistence multi-writer ; refus de celles-ci par défaut en raison du risque d'écart. Contrôle : routage traçable, rapprochement quotidien ou plus fréquent selon SLA et simulation de retour arrière.

## ADR-002 — Garantie de livraison

**Proposé** : refus de toute promesse « exactement une fois » entre système bancaire, API et rail sans mécanisme prouvé ; préférer at-least-once sur transport + déduplication métier persistante + réconciliation. La perte ou duplication de messages pendant panne est testée explicitement.

## ADR-003 — Images éditeur

**Proposé** : utiliser seulement les packages autorisés, sans tentative de ré-empaquetage non supportée. G1 est bloquant ; les exemples OCP inclus sont déclarés « simulateur » et ne reproduisent pas OPF.
