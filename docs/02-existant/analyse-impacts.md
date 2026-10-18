# Analyse d'impacts applicatifs, réseaux et processus

| Évolution hypothétique | Apps | Flux | Données | Sécurité | Exploitation | Décision |
|---|---|---|---|---|---|---|
| Migration façade API sur OCP | canaux, POM, IAM | TLS, timeout, headers | idempotency key | OAuth/mTLS, WAF | traces, rate limit | adapter hors cœur |
| Introduction broker d'événements | hub, SIEM, data | messages, ordering | schema registry/PII | ACL topics | lag, DLQ | events après commit |
| Déplacement runtime Java/JEE | WAR/EAR, DB, MQ | JDBC, JMS/JNDI | transactions XA | UID, secrets | GC, probes | avec approbation éditeur |
| Modification rail instantané | moteurs, CBIS, core | réponses temps réel | statuts/horloge | signatures/certificats | alerte deadlines | qualification métier |
| Changement schéma ISO | adaptateurs, archivage | versions pain/pacs/camt | mapping | intégrité | versionnement | tests rulebook |
| Bascule zone DC | hubs, brokers, BD | latence réseau | réplication, perte | routes et DNS | PRA | scénario chronométré |

## Fiche d'instruction d'une évolution

1. Identité de la demande, origine, objectif métier, urgence, risques.
2. AS-IS certifié par propriétaires, hypothèses restantes.
3. Alternatives au moins A/B, impacts L0-L4, dette et coûts.
4. Chaîne d'événements et propriétés de livraison, timeouts, retours.
5. Criticité des données, RGPD, couverture réglementaire selon périmètre.
6. SLO/RTO/RPO et preuves avant / après.
7. Tests de sécurité, charge, chaos, réconciliation ; responsabilités.
8. Décision datée, approbateur, exceptions, échéance de revue.

## Matrice RACI proposée

`Architecte fonctionnel` responsable objectifs/règles ; `Architecte applicatif` concepteur flux/contrats ; `Architecte plateforme` OCP/réseau ; `RSSI` sécurité ; `DBA/Middleware` ressources d'état ; `Product owner paiements` statuts/rail ; `SRE` SLO/PRA ; `Éditeur` support et licences ; `Design Authority` arbitre. RACI par dossier à finaliser lors du cadrage.
