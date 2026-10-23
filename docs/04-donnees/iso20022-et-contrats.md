# Contrats ISO 20022 / OPF — adaptation, validation, versions

Le **catalogue et la sémantique métier des messages** `pain`, `pacs`, `camt`, les statuts, les correspondances, la corrélation et la preuve de règlement sont définis dans le [référentiel canonique ISO 20022](https://github.com/zdmooc/banking-payments-business-architecture/blob/main/11-iso20022/MATRICE_MESSAGES.md) et les [contrats de mapping métier](https://github.com/zdmooc/banking-payments-business-architecture/blob/main/11-iso20022/CONTRATS_MAPPING_ET_STATUTS.md).

Ce document FIS OPF/OpenShift conserve les exigences de **fabrication et de validation de contrats d'intégration** de la cible, pas un second catalogue de messages normatif.

[Version historique intégrale](https://github.com/zdmooc/fis-opf-cloud-native-openshift-reference-architecture/blob/e829ec9229b7f362b02d77e6953d5e02f8c46843/docs/04-donnees/iso20022-et-contrats.md).

## Matrice de contrats à faire signer

| Champ | Attendu |
|---|---|
| ID de contrat | propriétaire, version et période de compatibilité |
| Transport | TLS/API, MQ, Kafka, MFT, ordre livraison |
| Identité | authentification, scopes, confiance |
| Format | ISO base + usage guidelines + contraintes locales |
| Transaction | acceptation technique vs ordre vs règlement |
| Réponse | codes de rejet et mapping métier |
| Qualité | idempotence, duplicate, timeout, retry, DLQ |
| Audit | correlation, conservation et accessibilité |
| Tests | jeu nominal/négatif/bord et golden files approuvés |

## Modèle d'évolution

1. Recevoir les profils de place et leur date d'effet.
2. Construire mapping versionné (sans perte d'information ou transformations documentées).
3. Valider syntaxe XSD puis règles de schéma/usage guidelines et règles métiers.
4. Exécuter tests contractuels de compatibilité N/N-1 lorsque supportée.
5. Certifier les scénarios émission, réception, rejet, retour, replay, timeouts.
6. Déployer par gouvernance release, surveiller les rejets par message.

Attention à la transition CBPR+ SR2026 (S06) ; ne pas supposer qu'une XSD officielle valide toutes les règles de réseau.

## Exemples de contrats

Les contrats dans `contracts/` décrivent **une façade fictive de laboratoire** et non des APIs OPF officielles. Ne pas soumettre les exemples de payloads au réseau de paiement.
