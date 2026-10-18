# TCO, licensing, dimensionnement et options économiques

## Postes de coûts

| Catégorie | Variables à estimer | Source de preuve |
|---|---|---|
| Logiciel OPF | licences, modules, env, support, adaptation/migration | devis FIS |
| OCP | nœuds/vCPU, licences, worker, infra support | contrat Red Hat/infra |
| Middleware | IBM MQ/Kafka, support, HA, stockage | contrats et inventaire |
| Base | Oracle ou autre, HA, option DR, stockage | licences + metering |
| Infra DC | compute, stockage IOPS, réseau, firewall, HSM | finance/infra |
| Exploitation | SRE 24/7, supervision, incidents | coût Run et SLA |
| Projets | formation, qualification, risque, migration | plan charges |
| Risques | indisponibilité et coût du rapprochement manuel | risque métier |
| Sortie | portabilité, historique, format et stratégie de réversibilité | clauses contractuelles |

## Modèle de calcul (à remplir)

`TCO_3ans = licences + infrastructure + middleware + DBA + équipe SRE + assurance/conformité + projet + DR + intégrations + risque résiduel chiffré`. Utiliser une estimation basse/centrale/haute ; documenter source, hypothèse, incertitude et date.

## Comparaison des options

A on-prem OCP vs B VM on-prem vs C coexistence vs D géré : chacun a une grille `CAPEX`, `OPEX`, `licences`, `économies de rationalisation`, `maintenance`, `DR`, `latences réseau`, `transferts de responsabilités`, `exit`. Aucun prix ou gain n'est prétendu réel dans ce dépôt.

## Sensibilité

Tester volume annuel, pics TPS, nombre de rails/modules, rétention, environnements, nombre d'équipes, proportion des personnalisations, coût de raccordement mainframe, tarif licence par CPU/pod/instance et exigences d'audit. Attention aux règles d'éditeur lors de l'autoscaling de vCPU.
