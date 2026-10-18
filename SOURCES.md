# Sources publiques et rigueur des preuves — consultées le 18/10/2026

| Réf. | Source | Ce qu'elle établit | Ce qu'elle n'établit pas |
|---|---|---|---|
| S01 | [FIS — Open Payment Framework](https://www.fisglobal.com/products/open-payment-framework) | ISO 20022, modules réutilisables, paiements temps réel, ACH, internationaux, architecture modulaire | Versions de runtime, support précis OCP |
| S02 | [FIS — Brochure OPF](https://www.fisglobal.com/-/media/fisglobal/files/PDF/brochure/Open-Payment-Framework-Brochure.pdf) | POM conteneurisé ; architecture de référence POM/exécution/intégration ; modules commerciaux et disponibilité annoncée | Images et topologie internes, niveaux de service mesurés |
| S03 | [FIS — Communiqué du 26/03/2026](https://fisglobal.gcs-web.com/news-releases/news-release-details/fis-named-leader-gartnerr-magic-quadranttm-banking-payment-hub) | OPF décrit en 2026 comme cloud-native, composable et ISO 20022 | Numéro de version exact « dernière version » |
| S04 | [Red Hat — OpenShift 4.22 SCC et exploitation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/day-2-operations-for-openshift-container-platform-clusters) | Contrainte `restricted-v2`, politique d'exécution et durcissement | Certification FIS sur OCP 4.22 |
| S05 | [Red Hat — PSA](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication_and_authorization/understanding-and-managing-pod-security-admission) | Contrôles PSA/SCC complémentaires | Configuration propre à OPF |
| S06 | [SWIFT — SR2026 CBPR+](https://www.swift.com/standards/iso-20022/iso-20022-bytes/call-action-november-2026) | Changements normatifs messages et validations à préparer | Configurations effectives d'un hub |
| S07 | [EPC — Document Center SCT Inst](https://www.europeanpaymentscouncil.eu/document-library/rulebooks) | Rulebooks et versions des schémas SEPA à sélectionner | Homologation métier automatique |
| S08 | [DORA — Règlement UE 2022/2554](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) | Cadre européen de résilience numérique applicable depuis janvier 2025 | Applicabilité précise à chaque composant/contrat |
| S09 | [Kubernetes — Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) | Stratégies déploiement et limites de rollout | Autorisation de rolling update FIS |
| S10 | [Kubernetes — PodDisruptionBudget](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) | Protection contre certaines disruptions volontaires | Tolérance aux crashs de nœud |
| S11 | [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | Contrôles de sécurité applicative | Certification produit |
| S12 | [ISO 20022](https://www.iso20022.org/) | Standards et catalogues de messages | Conformité sans tests de profil |

## Méthode

- Chaque affirmation sur **FIS** cite S01–S03 et reste bornée aux informations publiées.
- Chaque proposition d'architecture est marquée `HYPOTHESE` ou `PROPOSITION` ; aucune invention de port, base, queue, schéma, image ou version.
- Aucun téléchargement, copie ou redistribution du logiciel ou des supports propriétaires.
- Les illustrations XML/HTTP sont volontairement synthétiques et **non normatives**.
- Évolution des dénominations (FAST/INSTANT, XCT/WIRES) : conserver les deux libellés comme variantes documentaires, **sans présumer une correspondance de versions**.
