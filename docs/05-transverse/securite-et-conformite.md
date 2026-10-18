# Sécurité, conformité et architecture Zero Trust

## Objectifs de sécurité

Confidentialité, intégrité des ordres et mouvements, disponibilité 24/7, authentification forte, non-répudiation lorsque requise, traçabilité, séparation des responsabilités, conformité et résilience contre ransomware/compromission supply-chain.

## Threat model STRIDE synthétique

| Menace | Surface | Mesure | Vérification |
|---|---|---|---|
| Spoofing | API clients / workloads | IAM, scopes, mTLS, rotation certificats | tests identité refusée |
| Tampering | messages/ordres | intégrité, signature adaptée, hash/audit | modification détectée |
| Repudiation | actions de maintenance | journaux scellés, double validation | corrélation acteur/acte |
| Information disclosure | logs, backups, headers | masquage PII, chiffrement, minimisation | DLP + scans journaux |
| Denial of service | edge, broker, core | quotas, bulkheads, rate limits | charge abusive |
| Privilege escalation | pod et CI/CD | SCC restricted-v2, RBAC, politique images | admission et tests négatifs |

## Sécurité de bout en bout

1. **Identités** : comptes de service distincts, workload identity, accès humains fédérés, RBAC, JIT selon contexte.
2. **Réseaux** : segmentation deny-by-default, flux egress whitelist, DNS résolu et monitoré, bastions d'administration.
3. **Données** : classification, chiffrement avec KMS/HSM selon criticité, rotation, purge légale, prévention fuite vers SIEM.
4. **Images** : sources approuvées, SBOM, analyse, signature, policy en admission, exceptions documentées.
5. **CI/CD** : séparation des rôles builder/deployer/approver, signatures immuables et contrôle de drift.
6. **Runtime** : UID arbitraire, non-root, no privilege escalation, drop ALL capabilities, syscalls filtrés, volume root RO si possible.
7. **Opérations** : break-glass journalisé, accès au moindre privilège, sauvegardes protégées/récupérables.

## Réglementation : décider selon portée réelle

- **DORA** : TIC critiques, plan de continuité, incidents, tests de résilience, tiers TIC et responsabilité (S08). Une étude d'architecture n'est pas automatiquement une prestation opérationnelle réglementée.
- **RGPD** : qualifier données et traitements réels, minimiser PII et accès ; DPIA si nécessaire.
- **ISO 27001/27002** : politiques et contrôle d'accès, preuves, risques.
- **PCI DSS / 3DS** : **seulement si le système manipule des données de cartes ou entre dans le périmètre d'impact CDE**. Un hub de virements scripturaux n'est pas présumé PCI.
- **SWIFT CSP** : applicabilité à la connectivité/gateway et aux opérateurs concernés, à évaluer séparément.
- **Paiements instantanés UE** : règles de place, contrôle de bénéficiaire et délai d'exécution à vérifier par date, entité et schéma.

## Crypto-agilité et post-quantique

Maintenir inventaire certificats, protocoles, algorithmes, bibliothèques et chaînes de confiance ; simuler rotation, tester compatibilité et préparer migration algorithmique. Aucune affirmation de prise en charge post-quantique native dans OPF n'est faite.

## Revue de conception

Checklist : diagramme trust boundaries, classification données, modèles d'identité, journalisation, flux réseau minimaux, autorité des statuts, vulnérabilités dépendances, tests SAST/DAST, secrets, backup immuable et preuves des dérogations. Toute exception OCCP/privileged -> blocage jusqu'à approbation sécurité.
