# Factory d'instruction des évolutions

## Objectif

Un portefeuille de **plusieurs centaines de dossiers annuels** nécessite triage, réemploi de patterns, contrôle de complétude et décisions rapides, sans raccourci sur la sécurité et les états financiers.

## Pipeline type

`Intake → qualification et criticité → pré-inventaire → impacts applicatifs/flux → variantes → risques & NFR → revue métier/technique → ADR/avis → publication carto → contrôle post-changement`.

## Catégories de dossiers

- `S` simple : changement paramètre ou contrat non transactionnel ; contrôle proportionné.
- `M` moyenne : nouvelle interface/version, changement réseau ou persistence locale.
- `L` complexe : migration runtime, nouveau rail, changement du modèle de paiement.
- `XL` critique : changement d'autorité des données, DR, double site ou nouvelle réglementation.

## Template fiche instruction

```markdown
# Dossier <ID> - <Titre>
Demandeur : | Capacité concernée : | Criticité : | Échéance :
Besoin métier : | Hypothèses : | Points inconnus :
AS-IS (L0-L4) : | TO-BE : | Flux affectés :
Interfaces / états / données / référentiels :
Exigences non fonctionnelles / réglementation applicable :
Alternatives et TCO :
Risques, contrôles, dépendances fournisseur :
Tests / résilience / sécurité / audit / rollback :
Décision / statut / approbateurs :
Actions / propriétaires / échéances / pièces de preuve :
```

## Dashboard équipe

KPIs : délai d'instruction médian, taux de dossiers incomplets, restes-à-faire bloquants, nombre d'ADR sans validation, écarts cartographiques, risques non traités, respect des revues, dette archi et taux de réouverture.

## Qualité

Pas d'avis sur hypothèses non déclarées ; un manque de matrice fournisseur marque le dossier `BLOCKED` ; réutiliser patterns sans copier aveuglément un contexte à l'autre.
