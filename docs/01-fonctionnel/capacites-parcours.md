# FIS OPF — scénarios fonctionnels utiles aux tests de modernisation

La **carte des capacités, les rôles bancaires et les règles métier paiement** sont désormais maintenus exclusivement dans le [référentiel métier — capabilities](https://github.com/zdmooc/banking-payments-business-architecture/blob/main/04-capacites-metier/CAPABILITY_MAP.md) et la [carte des acteurs](https://github.com/zdmooc/banking-payments-business-architecture/blob/main/03-ecosysteme/ACTEURS_RESPONSABILITES.md).

Ce document garde les **scénarios de test et de transformation FIS OPF / OpenShift**, propres à la conception de solution. Ce sont des exigences hypothétiques, **pas des fonctionnalités attestées d'un module FIS**. L'ordre, les messages et délais schemes proviennent du canon et des rulebooks vérifiés.

[Version intégrale historique des parties métier et techniques](https://github.com/zdmooc/fis-opf-cloud-native-openshift-reference-architecture/blob/f9284818cf8dfc712dc759b500b9eadec73fc68f/docs/01-fonctionnel/capacites-parcours.md).

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
