# Cartographie métier / fonctionnelle du Payments Hub

## Carte des capacités L0

| Capacité | Sous-capacités | Données clés | KPI métier |
|---|---|---|---|
| Acquisition | API, fichiers, événements, canaux | Ordre, origine, empreinte | taux d'acceptation, distribution |
| Contrôle | format, schéma, sanctions, fraude, limites | évaluation, résultat, motif | taux STP, faux positifs |
| Orchestration | décision de rail, timers, états, exception | instruction, corrélation, décision | délai médian/P99, backlog |
| Exécution | instantané, lots/ACH, international/RTGS | message rail, statut, règlement | délai de confirmation, erreurs |
| Tenue de compte | réservation/débit/crédit/écritures | compte, mouvement, référence | écarts de balance |
| Supervision métier | OVA/portail exploitation, SLA, pistes d'audit | état, événement, acteur | en attente, rejets, délais |
| Compensation/réconciliation | rapprochement, anomalies, réparation | relevé, montant, numéro | écart non rapproché |
| Pilotage produit | règle tarifaire, limite, échéance, version | paramétrage, rulebook | changements sans défaut |

## Cartographie des acteurs

- **Débiteur / entreprise / partenaire** : initie un ordre et reçoit un accusé.
- **Canal + IAM** : authentifie, autorise, remet une preuve de consentement si requise.
- **Hub OPF** : consolide et coordonne des responsabilités métier, selon modules présents.
- **Core banking** : exécute les changements de tenue de compte selon contrat.
- **Infrastructure de clearing / SWIFT / RTGS** : apporte statuts et confirmations.
- **Compliance / fraude** : contrôle des risques et décisions.
- **Opérateur** : instruit une anomalie avec double contrôle lorsque requis.

## Parcours représentatifs à documenter de bout en bout

1. Virement instantané nominal : réception → contrôle → exécution → réponse finale → audit.
2. Timeout canal après acceptation : recherche par référence, jamais création aveugle.
3. Timeout rail après émission : état ambigu, interrogation/réconciliation, pas de double ordre.
4. Paiement international : contrôle sanctions/FX, routing, SWIFT, statuts et investigations.
5. Lot SEPA : ingestion MFT → validation entête/éléments → traitement individuel → statuts agrégés.
6. Rejet avant règlement : code métier, information client, correction et nouvelle instruction.
7. Retour/annulation après règlement : transaction compensatoire selon rail et règle applicable.
8. Dégradation du core : état déterministe, file durable et reprise après rétablissement.
9. Maintenance de nœud OCP : quiescence/drain, statut conservé, reprise.
10. Réconciliation de fin de journée ou quasi temps réel : corrélation ordre/rails/compte/audit.

**Ne pas confondre** date métier, instant de réception, acceptation technique, acceptation métier, émission rail et règlement irrévocable. Les statuts et responsabilités sont fixés par contrats, pas par seule nomenclature.
