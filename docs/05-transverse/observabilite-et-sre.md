# Observabilité, SRE et exploitation Day-2

## Signaux d'or et métriques métier

`received_total`, `accepted_total`, `rejected_total`, `settled_total`, `ambiguous_total`, `reconciliation_gap_total`, `rail_ack_latency_seconds`, `end_to_end_duration_seconds`, `queue_age_seconds`, `batch_stuck_total`, `core_unavailable_seconds`. Les noms sont proposés, pas des métriques offertes par OPF. Les mesurer si API/extension/sidecar autorisés.

## Traces

- Conserver `traceId` et identifiant métier **pseudonymisé** ; aucun PAN, IBAN brut, nom, montant nominatif sensible dans logs par défaut.
- Propager la corrélation à la frontière REST/MQ/MFT selon support, sans exiger de modifier le code propriétaire.
- Contrôler latence p99 et décorrélation lorsque le rail ne renvoie pas immédiatement.
- Les événements d'audit métier sont **séparés** des traces techniques (durée de rétention, accès, invariants).

## SLO et burn rate

SLO métier = fraction des paiements ayant atteint la condition de succès signée dans leur délai métier. Exclure/ inclure maintenances et dépendances externes seulement avec politique contractualisée. Error budget et seuils doivent être fixés avec le responsable métier ; alarmes par impact, pas seulement CPU.

## Runbooks prioritaires

- RB-01 statut incertain après 504 : interrogation durable et rail, pas de retry automatique.
- RB-02 backlog MQ : isolation, débit progressif, préservation de l'ordre et audit.
- RB-03 panne DB : suspendre admission si durabilité non assurée ; restaurer puis réconcilier.
- RB-04 incident certificat : rotation, test de confiance et vérification journaux.
- RB-05 pod évincé : drain, réattribution et contrôles des messages en cours.
- RB-06 régression release : arrêt canary, rollback applicatif **sans rollback aveugle des statuts et données**.

## Dashboard par audience

`Centre des paiements` : par rail, taux d'échec, demandes en attente, incidents ; `SRE` : saturation, traces, queue depth, disponibilité dépendances ; `Sécurité` : anomalies IAM/TLS/egress/admission ; `Architecture` : dette/versions/ADR/budget/performance.

## Read-only diagnostics

`scripts/preflight-readonly.sh` liste uniquement des informations non sensibles sur les projets et workloads ciblés (aucune lecture des secrets). Ne pas exécuter sur production sans autorisation.
