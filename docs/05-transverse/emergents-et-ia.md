# Horizons : crypto-agilité, paiements programmables et IA

## Radar d'architecture

| Sujet | Pertinence | Décision actuelle | Condition de lancement |
|---|---|---|---|
| Stablecoins / monnaie tokenisée | nouveaux rails potentiels | **HORS HUB OPF DEMONTRE** | cadre légal, partenaires, ledger et finalité prouvés |
| MNBC / monnaie numérique de banque centrale | évolution de rails | suivi/ADR | exigences officielles et contrats |
| Agentic payments | initiation automatisée | expérimentation **sans émission réelle** | mandat, limites, consentement, audit, non-répudiation |
| IA générative | assistant opérateur, documentation, triage | RAG lecture seule anonymisé | gouvernance données, évaluation, approbation humaine |
| Post-quantique | renouvellement primitives et certificats | inventaire et crypto-agilité | normes et interopérabilité validées |
| Streaming data / data lake | analyse anomalies, reporting | projections de faits autorisés | outbox, PII, data quality |

**Contrôle :** une IA ou un agent ne peut pas créer/autoriser un mouvement financier sans les contrôles métiers, le consentement et les autorisations déterministes. Aucun connecteur à un rail réel n'est fourni.

## Architecture IA non transactionnelle

Source d'événements **désensibilisés** → filtration PII → entrepôt gouverné → index documentaire vectoriel → moteur RAG → assistant opérateur avec citations → confirmation humaine. Couper toute sortie agent vers une interface `executePayment` ; la production de rapports reste consultative. Journaliser sources, réponses, habilitations et hallucinations.
