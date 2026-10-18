# Catalogue de patterns d'intégration bancaires

## Principes

Une API REST synchrone, une commande asynchrone dans une file et un événement métier de diffusion sont **trois contrats distincts**. Ne jamais choisir Kafka ou MQ uniquement par mode. Chaque pattern est documenté par problème, mécanisme, garantie, limites, usage, validation.

| ID | Pattern | Problème résolu | Garantie/limite | Exemple et test |
|---|---|---|---|---|
| P-01 | API Gateway + BFF | accès canaux sécurisés | API n'est pas une transaction distribuée | JWT/mTLS/rate-limiting |
| P-02 | Request-Reply + Timeouts | consultation immédiate | timeout ≠ échec métier | rejouer lecture idempotente |
| P-03 | Command Queue / competing consumers | travail durable différé | broker ACK ≠ règlement | crash entre consume et commit |
| P-04 | Publish-Subscribe | notifications multi-usages | consommateurs peuvent être retardés | schéma versionné et DLQ |
| P-05 | Idempotent Consumer | livraison au moins une fois | déduplication durable obligatoire | duplicate + concurrence |
| P-06 | Transactional Outbox | désynchronisation DB/event | atomique avec mutation locale seulement | crash avant publication |
| P-07 | Inbox / Processed Events | duplicate ingestion | nécessite clé, index et rétention | retry après timeout |
| P-08 | Saga / compensation | enchaînement de domaines | pas d'atomicité globale ; irréversibilité rail | réponse hors ordre |
| P-09 | Circuit Breaker + Bulkhead | panne d'un service tiers | doit respecter délai métier et statut | anomalie core AML |
| P-10 | Retry + Backoff + Jitter | faute transitoire | retries sur ordres non-idempotents INTERDITS | test répétition contrôlée |
| P-11 | Dead Letter + Quarantine | poison messages | aucune perte silencieuse ni relecture aveugle | incident/manuel/quatre yeux |
| P-12 | CDC + Anti-Corruption Layer | coexistence mainframe/legacy | pas de double propriété transactionnelle | migration progressive |
| P-13 | Strangler / Branch by Abstraction | trajectoire incrémentale | routage unique par transaction | flux témoin puis ramp-up |
| P-14 | Bulkhead métier | isolation instant/batch | capacité DB partagée reste risque | surcharge batch sans impact instant |
| P-15 | Reconciliation | statut incertain / écart | autorité des différentes sources à définir | 100% états expliqués |
| P-16 | Schema / Contract Versioning | évolution messages | profiles ISO non interchangeables | N/N-1 et réjections |

## Sélection des technologies

**REST** : commandes et consultations de statut de canaux lorsque latence/confirmation le permettent. Codes HTTP distinguent transport et acceptation métier ; une 202 n'est pas un règlement.  
**IBM MQ / JMS ou autre broker fiable** : commandes nécessitant stockage durable, ordonnancement et liaison systèmes Open/legacy. La transaction MQ/base demande preuve ; une livraison JMS transmise n'est pas exactement once end-to-end.  
**Kafka / event backbone** : événements immuables de diffusion, tableaux de bord, analytique et abonnés ; ne pas publier sans stratégie d'outbox/transaction. Kafka n'est pas équivalent à un ledger financier.  
**MFT/SFTP** : ingestion de fichiers, contrôles taille/empreinte, quarantaines, versionnement et accusés métier.  
**COBOL/mainframe** : contrat anti-corruption, reprise et sécurité réseau minimales ; ne pas exposer directement en façade externe.

## Contrat de message minimum

`schemaVersion`, `eventId`, `correlationId`, `causationId`, `paymentId`, `occurredAt`, `businessStatus`, `producer`, `sourceSystem`, `reconciliationRef`, `payloadClassification`. Inclure `idempotencyKey` uniquement lorsque pertinente et protéger tout identifiant sensible.

## Exemple de séquence de panne sûre

Commande reçue → transaction locale persiste ordre `ACCEPTED` + outbox → relay publie événement → consommateur réserve idempotent → envoie au rail → crash avant réponse → système marque `UNKNOWN` → interroge/reconcilie → mise à jour vers `SETTLED` ou `REJECTED` sur preuve. **Aucun second débit n'est automatiquement émis**.

Voir [exemples de séquences](../../diagrams/03-sequences-paiement.mmd).
