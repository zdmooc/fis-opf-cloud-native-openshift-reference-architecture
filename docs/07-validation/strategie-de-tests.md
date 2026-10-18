# Stratégie de tests multi-couches

## Pyramide de tests

L0 doc/schema/static ; L1 contrat API/message ; L2 intégration simulée ; L3 runtime réel éditeur en bac habilité ; L4 performance et résilience ; L5 sécurité, réseau, conformité ; L6 PRA/exploitation ; L7 acceptation bancaire.

## Jeu de scénarios

| ID | Scénario | Injection | Résultat attendu |
|---|---|---|---|
| T01 | paiement instantané nominal | aucune | statut terminal corrélé |
| T02 | erreur validation | champ incorrect | rejet avant émission |
| T03 | commande répétée | 2 POST même clé | une instruction unique |
| T04 | concurrence | 100 demandes même clé | une seule mutation durable |
| T05 | timeout rail | ACK absent | `UNKNOWN`, reconciliation, pas retry aveugle |
| T06 | crash après commit | pod kill | état durable, pas de double émission |
| T07 | base indisponible | couper JDBC | admission/états sûrs |
| T08 | broker down | broker indispo | file/backpressure/alarme |
| T09 | consumer en erreur | poison message | DLQ/quarantaine/alerte |
| T10 | inondation batch | pic charge ACH | latence instant protégée |
| T11 | zone arrêtée | node/site failure | RTO/RPO mesurés |
| T12 | certificats expirés | rotation faute | sécurité refuse, alerte |
| T13 | identités invalides | mauvais JWT/mTLS | 401/403, aucune mutation |
| T14 | exfiltration réseau | egress non déclaré | connexion bloquée |
| T15 | upgrade N-1/N | multi-version | tests compatibilité validés |
| T16 | rollback applicatif | erreur après upgrade | historique conservé |
| T17 | retour de paiement | erreur post-règlement | compensation contrôlée |
| T18 | rapprochement incomplet | référence divergente | écart et investigation |
| T19 | perte DNS | coupure | politiques panne maîtrisées |
| T20 | stress répétition longue | soak test | pas fuite/dégradation |
| T21 | fichier batch tronqué | MFT fail | quarantaine + accusé cohérent |
| T22 | message ISO non conforme | XSD + règle | refus traçable |
| T23 | accès opérateur | rôle insuffisant | refus journalisé |
| T24 | IA assistante | demande d'exécution | refus et escalade humain |

## Critères

- Tous les tests critiques T03–T08/T11/T12/T15/T18 doivent être observables, reproductibles et avec preuve archivée.
- Aucun essai contre rails/banques réels ; données strictement synthétiques.
- Les tests du simulateur prouvent **l'exemple** uniquement, pas les garanties OPF.
- Mesures prises par rapport aux SLO approuvés, sur dataset représentatif et avec bon dimensionnement.
