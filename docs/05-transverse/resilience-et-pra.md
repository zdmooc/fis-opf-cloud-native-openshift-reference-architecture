# Résilience métier, continuité et plan de reprise

## Indicateurs et budgets

Disponibilité et résilience sont **par parcours complet**, pas par pod. La disponibilité « always-on/99.999% » dans certains documents commerciaux FIS ne constitue ni contrat ni mesure d'un déploiement particulier. Définir SLO signés pour capture, validation, exécution, retour statut, rapprochement et opérations.

| Domaine | Exemple d'objectif de conception, NON contractuel | Mesure obligatoire |
|---|---|---|
| Réception API | requête identifiable malgré timeout | durable accepted/rejected |
| Instantané | délai réglementaire/rail applicable | temps réception → résultat rail |
| Batch | capacité à reprendre sans duplication | lot/élément/offset traçables |
| Core | réponse dégradée explicite si indisponible | états et nombre en attente |
| MQ/Broker | reprise sans double mouvement | redelivery + corrélation |
| Base | restauration cohérente | RPO, RTO, WAL + broker + rail |
| Site | bascule contrôlée | split-brain, rôles et DNS |

## Modes de panne à modéliser

F1 crash pod avant écriture ; F2 crash après commit avant ACK ; F3 perte réponse rail ; F4 indisponibilité base ; F5 latence et backlog MQ ; F6 fail de nœud/zones ; F7 certificats expirés ; F8 saturation CPU/GC ; F9 upgrade nœud ; F10 erreur de règle ; F11 partition réseau ; F12 indisponibilité monitoring.

## Pattern de recouvrement

Une exécution technique peut être rejouée, mais la **mutation financière ne peut l'être que si elle est idempotente ou expressément autorisée**. Journal d'état durable + clés uniques + tentative et accusé distingués + réconciliation + procédures quatre yeux sur événements indéterminés. Répliquer un message ou rejouer une queue sans contrôle est un anti-pattern.

## PRA : séquence de preuve

1. Déclarer perte de site, horodatage et journaux figés.
2. Stopper toute production ambiguë, identifier propriétaire de la vérité pour chaque rail.
3. Restaurer DB/queues en état cohérent, confirmer réplication/élection sans split brain.
4. Réconcilier les ordres émis avant activation de nouveaux writers.
5. Réactiver canaux progressivement ; suivre alarmes et débit.
6. Produire rapport d'écarts, RTO/RPO mesurés, preuves et signataires.

Les cibles numériques RPO=0 ou RTO de quelques minutes ne doivent jamais être promises sans protocole de synchronisation et test démontré.
