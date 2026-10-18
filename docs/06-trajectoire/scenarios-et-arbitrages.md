# Arbitrage des scénarios

## Options de modernisation

| Scénario | Description | Intérêt | Risques | Condition GO |
|---|---|---|---|---|
| A — OPF moderne on-prem OCP | modules FIS autorisés sur OpenShift | contrôle, cloud-native, incremental | certification, licence, état, opérabilité | matrice éditeur écrite |
| B — OPF moderne VM/on-prem | conserver runtime validé hors OCP | limitation des changements | dette plateforme, homogénéité | analyse de dette et SLA |
| C — POM moderne / moteurs coexistants | modernisation façade/orchestration | strangler réduit big-bang | transactions ambiguës, mapping | contrats front/back validés |
| D — OPF géré/hébergé | délégation du runtime | transfert partie exploitation | données, souveraineté, réseau, coûts, exit | SLA/DORA/contrat/exit |
| E — conversion EAR/WAR legacy | transformer un packaging historique | réemploi potentiel | non-support éditeur, XA, JNDI, drivers | approbation expresse + POC |

## Sélection conditionnelle

**Préconisation provisoire :** A si certifié ; sinon C/B pour contenir les risques en conservant les moteurs, sans migration forcée. D est un scénario comparatif pour le métier et les risques ; E **n'est pas une solution standard** sans accord FIS.

## Arbitrage technique et métier

- `Coût` : licences, maintenance, infra, support, conformité, continuité, migration, désengagement.
- `Risque` : double paiement, réconciliation, indisponibilité, changement de base, dépendances.
- `Performances` : p95/p99, backpressure, isolation batch/instant.
- `Sécurité` : segments, IAM, audit, HSM, conformité.
- `Délai` : efforts d'inventaire/qualification, appels éditeur, apprentissage et test.
- `Réversibilité` : contrats, sauvegardes, changement de schema, données à conserver.
- `Responsabilité` : matrice RACI d'incident et support éditeur.

## Décision datée

| ID | Objet | Décision proposée | Statut |
|---|---|---|---|
| ADR-001 | Stratégie migration | incrémentale, pas de big bang | PROPOSE |
| ADR-002 | Modules conteneurisés | packaging FIS/support écrit avant usage | CONDITIONNEL |
| ADR-003 | State management | pas de source de vérité dupliquée | PROPOSE |
| ADR-004 | Retry paiement | seulement avec contrat d'idempotence vérifié | PROPOSE |
| ADR-005 | Base et message | conserver dépendances externes d'abord | PROPOSE |
| ADR-006 | Observabilité | traces pseudonymisées et indicateurs métiers | PROPOSE |
| ADR-007 | GitOps | manifests versionnés, data upgrades distincts | PROPOSE |
| ADR-008 | Choix HPA | mesure dépendances avant autoscaling | PROPOSE |

Les décisions restent à accepter par Design Authority et représentants des risques.
