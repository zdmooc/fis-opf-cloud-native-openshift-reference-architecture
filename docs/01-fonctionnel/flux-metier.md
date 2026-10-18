# Événements, contrôles métier et cycles d'état

## Automate conceptuel d'ordre (non FIS)

`RECEIVED → VALIDATED → ACCEPTED → DISPATCHED → {SETTLED | REJECTED | PENDING_RECONCILIATION}`. Autres transitions possibles : `VALIDATION_FAILED`, `CANCEL_REQUESTED`, `RETURN_INITIATED`, `RETURNED`, `EXPIRED`. **Les événements de chaque rail sont plus complexes** ; cet automate n'est qu'un modèle d'analyse, jamais la vérité d'un module OPF.

## Règles non négociables

| Réf | Règle | Contrôle de preuve |
|---|---|---|
| BR-01 | Une instruction possède une identité stable et une corrélation jusqu'au règlement | lookup / réconciliation complète |
| BR-02 | Même demande métier + même clé => résultat original / statut, pas nouveau paiement | concurrence et crash injectés |
| BR-03 | Une réponse HTTP 504 **n'implique pas** échec de paiement | interrogation par référence |
| BR-04 | Un accusé MQ ou HTTP n'est pas la preuve d'un règlement définitif | preuve rail et compte |
| BR-05 | Un statut indéterminé ne déclenche pas un second mouvement automatique | quarantine + résolution |
| BR-06 | Une correction de message ne réécrit pas silencieusement un ordre réglé | piste d'audit inviolable |
| BR-07 | Les transformations ISO doivent conserver champs métier et références | tests aller-retour/profils |
| BR-08 | Fraude / conformité / VOP sont positionnés selon règles effectives | matrices de séquence signées |
| BR-09 | Les horodatages portent fuseau, source et temps de référence | comparaison et dérive |
| BR-10 | Les rapprochements expliquent tous mouvements et écarts | zéro écart inexpliqué à clôture |

## Gestion de la réponse ambiguë

1. Identifier commande et référence métier durable.
2. Inspecter l'état persistant de la commande, des émissions rail et des écritures.
3. Corréler par `paymentId`, `endToEndId`, identifiant de message ou équivalent contractuel.
4. Éviter un retry tant que le protocole de reprise sûr n'est pas spécifié.
5. Rejouer une **étape idempotente** seulement après preuves et journalisation.
6. Lever incident et saisir l'opérateur si l'état du rail ne peut être déterminé.

## Gouvernance des changements

Chaque règle de routing, limites et cutoffs doit avoir identifiant, version, tests de cas limites, responsable métier, dates d'effet et plan de retour. Modifications à quatre yeux pour domaines critiques.
