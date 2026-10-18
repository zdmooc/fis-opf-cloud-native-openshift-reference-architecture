# Gouvernance d'architecture et suivi des chantiers

## Instances

| Instance | Cadence | Entrées | Sorties |
|---|---|---|---|
| Atelier découverte | au démarrage et sur demande | besoins, AS-IS, parties prenantes | CR, actions |
| Revue applicative | hebdomadaire | dossiers M/L, impacts | avis conditionnel |
| Design Authority | selon jalons | comparatif, ADR, risques | décision signée |
| Revue sécurité/données | avant gate | flux, PII, menaces | validation/exception |
| Revue exploitation | préprod/passage prod | SLO, runbooks, PRA | acceptation Run |
| Bilan portefeuille | hebdomadaire | tâches, deadlines, blockers | rapport synthèse |

## Registre d'action modèle

| ID | Dossier | Action | Responsable | Date | Statut | Preuve |
|---|---|---|---|---|---|---|
| ACT-001 | exemple | fournir matrice d'images supportées | éditeur | à définir | BLOCKED | non fournie |

## Préparer un avis

Présenter en dix minutes : besoin/risque, archi actuelle, 2–3 variantes, matrice d'impacts, état transactionnel, coût, options de réversibilité et recommandation conditionnelle. Le CR désigne actions, arbitrage, propriétaire et deadline ; jamais de décision « implicite ».
