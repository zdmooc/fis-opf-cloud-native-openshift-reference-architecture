# ISO 20022, profils de place, normes et contrats

## Catégories de messages (indicatives)

- **pain.001** : initiation client du virement ; **pain.002** : retour de statut à l'initiateur, selon canal.
- **pacs.008** : transfert de crédit interbancaire ; **pacs.002** : réponse/statut interbancaire ; **pacs.004** : retour de paiement ; **pacs.009** : transfert entre institutions financières.
- **camt.052/053/054** : rapports et notifications de cash management ; **camt.056** : demande d'annulation/rappel dans des scénarios spécifiques.
- Les versions/sous-ensembles admis **dépendent** de SCT/SCT Inst, CBPR+, du rail, de la date d'effet et du schéma de place.

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
