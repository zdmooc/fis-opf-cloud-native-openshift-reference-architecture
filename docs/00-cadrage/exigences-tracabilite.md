# Traçabilité des exigences (référentiel générique)

**Objectif :** couverture des besoins fonctionnels, techniques, risques, décisions, exploitation et gouvernance. Statut initial = `DOCUMENTE, NON VALIDE EN PRODUCTION`. Les preuves ne sont pas des validations éditeur.

| ID | Domaine | Attendu | Livrable de preuve | Statut |
|---|---|---|---|---|
| EX-001 | Métier | cartographie capacités produits et schémas | [01-fonctionnel/capacites-parcours.md](../01-fonctionnel/capacites-parcours.md) | DOCUMENTE / A_VALIDER |
| EX-002 | Fonctionnel | parcours instantané, masse, international, exceptions | [01-fonctionnel/flux-metier.md](../01-fonctionnel/flux-metier.md) | DOCUMENTE / A_VALIDER |
| EX-003 | Urbanisation | AS-IS hybride et interfaces | [02-existant/cartographie-as-is.md](../02-existant/cartographie-as-is.md) | DOCUMENTE / A_VALIDER |
| EX-004 | Intégration | API synchronous et contrats | [03-architecture/integration-patterns.md](../03-architecture/integration-patterns.md) | DOCUMENTE / A_VALIDER |
| EX-005 | Intégration | messaging fiable commandes | [03-architecture/integration-patterns.md](../03-architecture/integration-patterns.md) | DOCUMENTE / A_VALIDER |
| EX-006 | Intégration | événements/pub-sub | [03-architecture/integration-patterns.md](../03-architecture/integration-patterns.md) | DOCUMENTE / A_VALIDER |
| EX-007 | Applicatif | Java/JEE legacy et stratégie coexistence | [02-existant/analyse-impacts.md](../02-existant/analyse-impacts.md) | DOCUMENTE / A_VALIDER |
| EX-008 | Plateforme | Kubernetes/OpenShift/Red Hat | [03-architecture/lld-openshift.md](../03-architecture/lld-openshift.md) | DOCUMENTE / A_VALIDER |
| EX-009 | Réseau | cartographie zones/flux/protocoles | [03-architecture/zones-reseau.md](../03-architecture/zones-reseau.md) | DOCUMENTE / A_VALIDER |
| EX-010 | Données | modèle conceptuel, data quality | [04-donnees/architecture-donnees.md](../04-donnees/architecture-donnees.md) | DOCUMENTE / A_VALIDER |
| EX-011 | Paiement | ISO 20022/SEPA/SWIFT | [04-donnees/iso20022-et-contrats.md](../04-donnees/iso20022-et-contrats.md) | DOCUMENTE / A_VALIDER |
| EX-012 | Résilience | 24/7 et défaillances | [05-transverse/resilience-et-pra.md](../05-transverse/resilience-et-pra.md) | DOCUMENTE / A_VALIDER |
| EX-013 | Performance | latence, débits, capacité | [05-transverse/performance-capacity.md](../05-transverse/performance-capacity.md) | DOCUMENTE / A_VALIDER |
| EX-014 | Sécurité | Zero Trust et segmentation | [05-transverse/securite-et-conformite.md](../05-transverse/securite-et-conformite.md) | DOCUMENTE / A_VALIDER |
| EX-015 | Conformité | DORA, RGPD, périmètre PCI | [05-transverse/securite-et-conformite.md](../05-transverse/securite-et-conformite.md) | DOCUMENTE / A_VALIDER |
| EX-016 | Sécurité | crypto-agilité et futur post-quantique | [05-transverse/emergents-et-ia.md](../05-transverse/emergents-et-ia.md) | DOCUMENTE / A_VALIDER |
| EX-017 | Disponibilité | reprise transactionnelle/anti-doublon | [05-transverse/resilience-et-pra.md](../05-transverse/resilience-et-pra.md) | DOCUMENTE / A_VALIDER |
| EX-018 | Run | monitoring, SRE, runbooks | [05-transverse/observabilite-et-sre.md](../05-transverse/observabilite-et-sre.md) | DOCUMENTE / A_VALIDER |
| EX-019 | Impacts | composants et flux inter-systèmes | [02-existant/analyse-impacts.md](../02-existant/analyse-impacts.md) | DOCUMENTE / A_VALIDER |
| EX-020 | Migration | cible + architecture de transition | [06-trajectoire/roadmap-migration.md](../06-trajectoire/roadmap-migration.md) | DOCUMENTE / A_VALIDER |
| EX-021 | Arbitrage | comparaison scénarios risques | [06-trajectoire/scenarios-et-arbitrages.md](../06-trajectoire/scenarios-et-arbitrages.md) | DOCUMENTE / A_VALIDER |
| EX-022 | Décisions | avis d’architecture et ADR | [06-trajectoire/risques-et-adrs.md](../06-trajectoire/risques-et-adrs.md) | DOCUMENTE / A_VALIDER |
| EX-023 | Livrables | CR ateliers sous une semaine | [08-gouvernance/cadence-livrables.md](../08-gouvernance/cadence-livrables.md) | DOCUMENTE / A_VALIDER |
| EX-024 | Livrables | HLD transition sous trois semaines | [08-gouvernance/cadence-livrables.md](../08-gouvernance/cadence-livrables.md) | DOCUMENTE / A_VALIDER |
| EX-025 | Livrables | avis et cartos sous un mois | [08-gouvernance/cadence-livrables.md](../08-gouvernance/cadence-livrables.md) | DOCUMENTE / A_VALIDER |
| EX-026 | Pilotage | suivi comités hebdomadaire | [08-gouvernance/comitologie-et-suivi.md](../08-gouvernance/comitologie-et-suivi.md) | DOCUMENTE / A_VALIDER |
| EX-027 | Cadence | plusieurs centaines demandes/an | [08-gouvernance/kit-instruction-architecture.md](../08-gouvernance/kit-instruction-architecture.md) | DOCUMENTE / A_VALIDER |
| EX-028 | Qualité | recette de livrables et critères | [07-validation/matrice-de-recette.md](../07-validation/matrice-de-recette.md) | DOCUMENTE / A_VALIDER |
| EX-029 | Risques | points bloquants éditeur support | [06-trajectoire/questions-editeur.md](../06-trajectoire/questions-editeur.md) | DOCUMENTE / A_VALIDER |
| EX-030 | Anticipation | IA et paiements émergents cadrés | [05-transverse/emergents-et-ia.md](../05-transverse/emergents-et-ia.md) | DOCUMENTE / A_VALIDER |

## Règle de fermeture

Une exigence n’est `VERIFIEE` qu’avec identifiant de test, run, résultat daté, architecture/réglementation applicable, propriétaire et approbateur. Une description documentaire seule ne suffit pas.
