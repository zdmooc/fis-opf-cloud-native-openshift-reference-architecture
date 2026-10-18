# Synthèse de la recommandation

## Besoin et critères de succès

Mettre à disposition un hub de paiements agile sans rupture de tenue de compte ni dégradation de la chaîne de paiement : traitements instantanés, internationaux et de masse, disponibilité élevée, conformité, sécurité et coûts maîtrisés. Éviter un big bang ; assurer la coexistence, la réconciliation et la responsabilité de chaque domaine.

**Arbitrage :** conserver les moteurs existants pendant le déploiement de la couche de capture / orchestration lorsqu'elle le permet ; basculer progressivement les familles de paiements, sous réserve de support FIS. Une bascule à deux moteurs actifs sans propriété unique de l'ordre et sans réconciliation est refusée.

## Grille pondérée (PROPOSITION)

| Critère | Poids | A: OPF moderne OCP | B: maintien VM | C: façade découplée | D: service hébergé |
|---|---:|---:|---:|---:|---:|
| Maîtrise d'exploitation sur site | 15 | 5 | 5 | 4 | 2 |
| Support éditeur établi | 25 | 2 | 4 | 3 | 3 |
| Réversibilité | 15 | 4 | 4 | 4 | 2 |
| Résilience / HA prouvable | 20 | 4 | 3 | 3 | 4 |
| Délai / complexité transformation | 15 | 3 | 5 | 4 | 3 |
| Coûts maîtrisables | 10 | 3 | 3 | 3 | 2 |

Notes 1 à 5 **illustratives**, basées sur hypothèses seulement ; `support éditeur` doit être re-noté dès réception des pièces. Un score n'autorise jamais une mise en production sans gates.

## Gates incontournables

G0 périmètre connu ; G1 support/licence écrit ; G2 design approuvé ; G3 contrats/états validés ; G4 résilience/performance prouvées ; G5 sécurité/audit/continuité approuvés ; G6 préprod et recette signées ; G7 bascule avec rapprochement 100 % des mouvements traités. Les exceptions sont explicitées et signées, jamais implicites.
