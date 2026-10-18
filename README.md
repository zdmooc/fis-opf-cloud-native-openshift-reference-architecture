# FIS OPF — Cloud-Native Payment Hub / OpenShift Reference Architecture

**Étude d'architecture indépendante | Version documentaire 1.0 | 18 octobre 2026**  
**Hypothèse structurante :** génération contemporaine FIS Open Payment Framework (OPF), fondée sur les descriptions éditeur disponibles en 2026. Ce dépôt **n'affirme pas connaître un numéro de release OPF non publié**, ni disposer d'images, binaires, licences, schémas internes, configurations ou certification OpenShift.  
**Positionnement :** architecture de référence, scénarios de transformation, dossiers d'arbitrage et POC **simulé** ; aucune intégration FIS réelle n'est fournie.

## Décision architecturale synthétique

**Cible recommandée conditionnelle :** un hub OPF modulaire orchestré sous OpenShift, accompagné de composants d'intégration bancaires, en conservant initialement les bases et messageries d'entreprise hors du cluster tant que support, transactionnalité et bénéfices ne sont pas démontrés. **GO** pour études et émulation non productive ; **NO-GO production** sans certification/support écrit FIS + qualification de bout en bout et RTO/RPO/SLO éprouvés.

**Lecture continue :** [Étude intégrale en un seul fichier](ETUDE_COMPLETE.md) · **Publication :** [Guide pour dépôt GitHub privé](PUBLICATION_GITHUB.md).

**Lecture continue :** [Étude intégrale en un seul fichier](ETUDE_COMPLETE.md) · **Publication :** [Guide pour dépôt GitHub privé](PUBLICATION_GITHUB.md).

## Navigation des livrables

| Chantier | Livrable | Emplacement |
|---|---|---|
| Direction / cadrage | Synthèse, hypothèses, périmètre, preuves et écarts | [00 - Cadrage](docs/00-cadrage/README.md) |
| Métier et fonctions | Capacités, parcours, événements et règles de traitement | [01 - Fonctionnel](docs/01-fonctionnel/README.md) |
| Urbanisation / AS-IS | Hypothèses d'existant et chaîne de dépendances | [02 - Existant](docs/02-existant/README.md) |
| Architecture cible / transition | HLD, LLD, réseau et intégration hybride | [03 - Architecture](docs/03-architecture/README.md) |
| Données | Modèle conceptuel, ISO 20022, qualité, réconciliation | [04 - Données](docs/04-donnees/README.md) |
| Architecture transverse | Sécurité, HA, SRE, performance, observabilité | [05 - Exigences transverses](docs/05-transverse/README.md) |
| Migration et arbitrages | Options, ADR, jalons, risques, coûts, GO/NO-GO | [06 - Trajectoire](docs/06-trajectoire/README.md) |
| Validation | Matrice de tests, campagnes et critères d'acceptation | [07 - Validation](docs/07-validation/README.md) |
| Gouvernance | Avis d'architecture, ateliers, comités, traçabilité | [08 - Gouvernance](docs/08-gouvernance/README.md) |
| Laboratoire | Mock contractuel, manifests OpenShift **non OPF**, sécurité | [poc/](poc/README.md) |
| Diagrammes | Sources Mermaid réutilisables et rendus GitHub | [diagrams/](diagrams/README.md) |
| API / événements | Contrats illustratifs **non FIS** | [contracts/](contracts/README.md) |
| Sources | Références publiques horodatées | [SOURCES.md](SOURCES.md) |

## 10 conclusions utiles

1. L'éditeur présente OPF comme hub cloud-native ISO 20022 et POM comme couche d'intégration de canaux conteneurisée. La **granularité réelle des images/pods n'est pas publiée**.
2. POM, moteurs instantané, ACH et international sont des **capacités métier**, non une nomenclature Kubernetes garantie.
3. Des documents FIS de périodes différentes emploient les labels FAST/XCT ou INSTANT/WIRES : l'équivalence des versions **n'est pas assumée comme vérité contractuelle**.
4. Une architecture hybride Mainframe/Open/VM/Cloud est le point de départ **hypothétique**, à confirmer par un inventaire.
5. REST pour interrogation synchrone ; messagerie fiable pour commandes, événements pour diffusion de faits ; les bindings réels sont contractualisés.
6. Un retry réseau n'est pas une autorisation de réexécuter un paiement ; états durables, clés d'idempotence, réconciliation sont essentiels.
7. ISO 20022 est un modèle et un écosystème de profils/rulebooks : pas de garantie qu'un exemple XML soit un message certifiable.
8. `restricted-v2`, UID attribué, segmentation réseau, secrets, signatures et observabilité doivent être vérifiés sur les **images autorisées**.
9. La protection des données et la conformité doivent être déterminées par **périmètre réel**, pas par simple proximité avec les paiements carte/3DS.
10. La mise en production exige une validation conjointe éditeur, architecture, risque, sécurité et exploitation.

## Matrice de correspondance besoins ↔ preuves

Consulter [la matrice EX-001 à EX-030](docs/00-cadrage/exigences-tracabilite.md). Elle couvre les dimensions métiers, flux, API/MQ/Kafka, Java/JEE, conteneurs, zones réseaux, données, 24/7, sécurité, conformité, risques, décisions, cartographies, ateliers, suivi, livrables et délais.

## Qualité, sécurité documentaire et limite juridique

- Aucun composant propriétaire OPF, document non public, schéma fourni par un tiers ou donnée bancaire réelle.
- Les objets `poc/` sont exclusivement un **simulateur de façade** ; jamais un moteur de paiement, une implémentation ou une distribution FIS.
- Les budgets, capacités, délais et RPO/RTO présentés à titre de scénarios ne sont pas des engagements.
- Publication privée recommandée, revue de confidentialité avant publication publique.
- Texte original protégé : [tous droits réservés](LICENSE) ; marques, technologies et documents tiers restent la propriété de leurs titulaires.

## Démarrage rapide

```bash
python3 scripts/audit_repo.py
python3 -m unittest discover -s tests -v
# En laboratoire seulement, après adaptation des environnements :
# oc apply -k poc/openshift/overlays/lab
```

## Statut de preuve

`CONFIRME_EDITEUR` = publication FIS ; `CONFIRME_STANDARD` = documentation officielle ; `INDICE_PUBLIC` = contexte non contractuel ; `HYPOTHESE` = design fictif ; `A_VALIDER` = absence de preuve ; `DEMONSTRATION` = exemple non productif.
