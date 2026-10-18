# Performance, dimensionnement et FinOps

## Modèle de dimensionnement paramétrique

Soit `λ` = demandes/s en pointe ; `t` = temps de service en secondes ; `c` = capacité d'un replica, mesurée sous SLA ; `h` = headroom. Nombre de réplicas `ceil(λ/(c×(1-h)))`, sous réserve de saturation DB/broker/tiers. Loi de Little sur une file stable : `L = λ × W`. Prévoir pics temps réel, volumétrie batch/MFT, retour réseau, granularité et taille de messages ; ne pas extrapoler un test API à l'intégralité de la chaîne bancaire.

## Paramètres à mesurer

| Mesure | Nom | Niveau de preuve |
|---|---|---|
| Latence | P50 / P95 / P99 / max end-to-end, par rail | traces + corrélation |
| Débit | ordres/s, éléments batch/s | files et mouvements |
| Saturation | CPU, heap, GC pause, threads, connexions JDBC | métrologie |
| Brokering | profondeur de queue, unacked, DLQ, consumer lag | mesures broker |
| DB | IO, latence, lock, active sessions, WAL | DBA |
| Défauts | timeout, backpressure, circuit open | tests chaos |
| Budget | cost/request, licence et nombre de vCPU/pods | factures/profilage |

## Campagnes

- Charge nominale fonctionnelle et P95/P99.
- Pointes x2/x5 comme scénarios d'exploration **non calibrés**, pas engagement de capacité.
- Spike instantané pendant lot lourd ; mesurer isolation inter-rails.
- GC stress, thread starvation, limites HPA, saturation pool DB et dead-letter.
- Shadow read-only avec comparaisons de réponses **sans émission de deuxième mouvement**.
- Soak test 24–72 h à ajuster ; fuites mémoire, connexions, fragmentation, index.

## Définition du GO

Mesures répétables, dataset synthétique, environnement représentatif, percentiles par route, zéro perte/doublon, limites documentées, garde-fous capacitaires et délestage approuvés ; décision business sur le coût et la criticité.
