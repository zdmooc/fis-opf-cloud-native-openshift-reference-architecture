# Questionnaire FIS — pièces minimales pour un GO opérationnel

| ID | Question à poser | Type de preuve |
|---|---|---|
| FIS-01 | Dernière génération OPF exacte, builds par module, support lifecycle ? | release notes/versions |
| FIS-02 | Packaging conteneur disponible pour POM, moteurs, CBIS, utilitaires, console ? | inventaire images et chart/operator |
| FIS-03 | Versions OpenShift certifiées, OS/arch CPU et runtimes Java supportés ? | matrice écrite |
| FIS-04 | Compatible SCC `restricted-v2`, UID arbitraire, non-root, RO filesystem ? | security deployment guide |
| FIS-05 | DB, MQ/JMS, Kafka et modèles de transaction supportés par module ? | dépendances/référentiel |
| FIS-06 | Modes actifs-actifs, d'état/HA, drain et upgrade N/N-1 ? | PRA/runbook validé |
| FIS-07 | API, événements, adaptateurs, garanties de livraison et ordre ? | contracts OpenAPI/AsyncAPI |
| FIS-08 | Stratégie de migration de données, schémas, rejouabilité et idempotence ? | procédure éditeur |
| FIS-09 | SLAs support, RTO/RPO, fenêtre upgrades et compatibilité backups ? | contrat |
| FIS-10 | Licences image/CPU/pod/cloud, compatibilité OpenShift et droits de copie ? | contrat/licences |
| FIS-11 | Mises à jour rulebooks 2026 SEPA / SWIFT CBPR+, certification par module ? | attestation/parcours |
| FIS-12 | Audit, événements, métriques, tracing et interface SIEM disponibles ? | guide exploitation |
| FIS-13 | Chiffrement, mTLS, HSM, IAM, secrets, PKI et crypto-agilité ? | guide sécurité |
| FIS-14 | Support en panne de mainframe / Core et reprise d'états indéterminés ? | tests éditeur |
| FIS-15 | Interfaces fichiers, MFT, batch, scheduler, console de réparation ? | matrice intégration |
| FIS-16 | Prérequis sizing, HPC, performance garantie par flux ? | guide sizing |
| FIS-17 | Fourniture de bacs sandbox, artefacts d'installation et datasets fictifs ? | accès contractuel |
| FIS-18 | Stratégie réversibilité, export des événements et retrait des anciens modules ? | exit plan |

**G1 NO-GO** si FIS-01 à 06, 08, 10 sans documents probants.
