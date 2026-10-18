# Cadrage, classification des faits et frontières

## Mission d'architecture de référence

Construire un système d'information de paiements 24/7, interconnecté, évolutif, intégrant une plateforme OPF moderne aux mondes mainframe, serveurs Java/JEE, applications Open, VM et OpenShift. Assurer l'urbanisation, la maîtrise des flux, la capacité d'instruire un grand nombre d'évolutions et l'observabilité des décisions.

## Hypothèses formelles

| ID | Hypothèse | État | Validation requise |
|---|---|---|---|
| H-01 | Produit FIS OPF de génération cloud-native 2026 | HYPOTHESE DE CADRAGE | Version/build/licence par composant |
| H-02 | POM disponible et intégrable aux moteurs paiements | CONFIRME_EDITEUR pour la capacité | Contrats runtime et API réels |
| H-03 | Certains composants peuvent fonctionner sur OpenShift | A_VALIDER | Matrice de compatibilité éditeur |
| H-04 | Architecture bancaire hybride mainframe/Open/VM/Cloud Native | HYPOTHESE | CMDB, interviews, diagrammes à jour |
| H-05 | Base relationnelle, broker d'entreprise, ordonnanceur | HYPOTHESE | Inventaire par flux et environnement |
| H-06 | Criticité et disponibilité 24/7 | CIBLE METIER | Contrat SLO + RTO/RPO par service |
| H-07 | Périmètre SCT Inst, SCT, SDD, SWIFT/RTGS | EXEMPLES | Rail et périmètre contractuels |
| H-08 | Réseaux, seuils, données, protocoles, IDs inconnus | A_VALIDER | Mesures et contrats |

## Frontières de système

**Dans le domaine d'étude** : capture des ordres, contrôle, routage, exécution via moteurs, statuts, réparations, exceptions, intégration aux systèmes de tenue de compte, interfaces avec rails, événements et observation.

**Interfaces adjacentes** : canaux web/mobile/entreprise, API management, IAM, antifraude, AML/sanctions, FX, SWIFT, comptabilité, MFT et mainframe. Les intégrations 3-D Secure, biométrie, tokenisation carte et monétique **ne sont pas attribuées par défaut à OPF** : elles constituent des domaines à cartographier si le périmètre le justifie.

**Hors périmètre** : firmware HSM, conception des réseaux interbancaires eux-mêmes, transformation du cœur bancaire, développement de modules FIS propriétaires, preuve de certification par un simulateur.

## Classification

- `CONFIRME_EDITEUR` — brochure/pages officielles, pas de déduction sur une installation.
- `CONFIRME_STANDARD` — documentation d'une plateforme/autorité.
- `HYPOTHESE` — représentations fictives révisables.
- `PROPOSITION` — décision de conception recommandée et non acceptée.
- `A_VALIDER` — point bloquant demandant une preuve.
- `DEMONSTRATION` — lab sans composants OPF réels.

## Niveaux et décision

L0 cartographie métier → L1 contexte SI → L2 containers/logique → L3 composants/interfaces → L4 déploiement OpenShift. Une décision d'architecture doit préciser : contexte, options, impacts métiers/data/réseau, coûts, risques, sécurité, observabilité, rollback, tests, avis du fabricant, approbation et date de révision.
