# Critères de recette par livrable et gates

| Gate | Pièce requise | Critère d'acceptation | Responsable du visa |
|---|---|---|---|
| G0 | carto AS-IS et besoins métier | apps, flux, données, risques et inconnus signés | propriétaires SI |
| G1 | matrice support FIS | versions, images, licences, runtime et OCP explicités | éditeur/achats |
| G2 | DAT/HLD/LLD/ADR | alternatives, justifications, schémas lisibles, sécurité | comité architecture |
| G3 | contrats et tests intégration | états, ISO, MQ/API, délais, anti-doublons | métier/intégration |
| G4 | performance et résilience | SLO, RTO/RPO et incidents mesurés | SRE/performance |
| G5 | dossier sécurité/conformité | risques/contrôles/exceptions approuvés | RSSI/conformité |
| G6 | exploitation/préprod | runbook, sauvegarde, secrets, upgrade/rollback | exploitation |
| G7 | mise en service | plan signé, tests et reconciliation complète | métier/risque |

## Critères rédactionnels des livrables

- Chaque cartographie comporte légende, date, version, périmètre, nom des propriétaires, protocole/direction, incertitudes.
- Chaque dossier contient contexte, besoins, analyse d'impacts, options, décision, risques, coûts, preuves et reste à faire.
- Chaque atelier a convocation, participants, décisions, actions datées et CR dans le délai prévu.
- Les dossiers d'avis séparent proposition d'avis accepté.
- La réception n'est définitive qu'après contrôle de complétude, conformité et validation formalisée.

## Exemples de preuve attendue

`test_id`, `build image digest`, `version OCP`, `dataset synthétique`, `start_at`, `end_at`, `latence`, `count accepted/settled/unknown`, `écart`, `logs masqués`, `artefact signé`, `approbateurs`.
