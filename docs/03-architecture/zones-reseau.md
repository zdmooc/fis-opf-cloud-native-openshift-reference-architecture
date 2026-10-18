# Cartographie des zones de sécurité et flux inter-systèmes

## Zonage de principe

- **Z0 Canal externe** : internet, partenaires, réseau interne des canaux.
- **Z1 Edge/API** : WAF, DDoS/ingress, API management, identité.
- **Z2 Domaine applicatif** : namespaces/workloads paiement, aucune sortie libre.
- **Z3 Intégration** : service adapters, MQ, gateways inter-zones.
- **Z4 Données** : DB transactionnelle, coffre secrets, HSM selon périmètre.
- **Z5 Échanges interbancaires** : routeur SWIFT/SEPA/RTGS externes sous contrôle.
- **Z6 Administration/observabilité** : GitOps/CI/CD/SIEM/metrics, réseau séparé.

## Catalogue logique de flux à compléter (ports non inventés)

| ID | Source | Cible | Catégorie | Chiffrement | Risque |
|---|---|---|---|---|---|
| NET-01 | Z0 | Z1 | HTTPS entrant | TLS, WAF | abus externe |
| NET-02 | Z1 | Z2 | API front/back | mTLS si profil supporté | identité et latence |
| NET-03 | Z2 | Z3 | API/MQ/JMS | TLS/mTLS | backlog et doublons |
| NET-04 | Z2 | Z4 | JDBC / appels DB | TLS | pool et deadlock |
| NET-05 | Z3 | Z5 | flux interbancaire | canal approuvé | délais et intégrité |
| NET-06 | Z3 | Core | adaptation MQ/API/fichier | tunnel/chiffrement | legacy |
| NET-07 | Z2 | Z6 | métriques/traces/logs | TLS, minimisation | fuite PII |
| NET-08 | Z6 | Z2 | GitOps/administration | RBAC + audit | changements non maîtrisés |

**Avant firewalling** : préciser IP/FQDN, direction, ports, résolution DNS, certificats, protocole, volume, taille max, timeout, identité, classification, environnement, protocole de reprise, équipe propriétaire. La NetworkPolicy Kubernetes ne gouverne pas à elle seule l'ensemble des flux hors cluster.

## Zero Trust

Identité workload + identité humaine + posture machine ; cloisonnement micro-réseau ; politiques egress restrictives ; moindre privilège ; rotation clés ; inventaire des dépendances ; audit. Un simple service mesh ne remplace pas la politique d'identité ni les flux sans HTTP.
