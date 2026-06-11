# Recherche hebdomadaire — lecture quotidienne

Automatisation personnelle : chaque semaine, une thématique scientifique ou sociale est explorée. Chaque jour à ~7h00 (Europe/Paris), un agent Claude planifié dans le cloud produit une lecture d'environ 30 minutes sur le thème de la semaine et l'envoie par email à kamilmahmal22@gmail.com, à partir exclusivement de sources fiables acceptées par la communauté scientifique.

## Fonctionnement

- **Routine cloud Claude** : s'exécute tous les jours (cron `0 5 * * *` UTC). Elle clone ce repo, lit `INSTRUCTIONS.md` et le suit intégralement.
- **Lundi** : l'agent démarre une nouvelle semaine en prenant le premier thème de `themes/backlog.md` (priorité aux thèmes `validé`). Il réapprovisionne le backlog en propositions si besoin.
- **Chaque jour** : l'agent rédige la lecture du jour (`weeks/<YYYY-Www>/day-N.md`) et la pousse sur GitHub.
- **Envoi de l'email** : la GitHub Action `.github/workflows/send-reading.yml` détecte chaque nouveau `day-N.md` poussé et l'envoie par email (SMTP Gmail). Secrets requis dans le repo : `MAIL_USERNAME` (adresse Gmail) et `MAIL_APP_PASSWORD` (mot de passe d'application Google, créé sur https://myaccount.google.com/apppasswords).

## Comment piloter les thématiques

Éditer `themes/backlog.md` (depuis GitHub web, l'app mobile GitHub, ou ce dossier local) :

- Changer le statut d'un thème de `proposé` à `validé` pour le confirmer.
- Réordonner les lignes pour changer la priorité (l'agent prend le premier `validé`, sinon le premier `proposé`).
- Supprimer ou ajouter des thèmes librement.

## Structure

```
INSTRUCTIONS.md      — instructions complètes de l'agent (format, qualité des sources, logique)
themes/backlog.md    — thèmes à venir (éditable à tout moment)
themes/history.md    — thèmes déjà traités
weeks/<YYYY-Www>/    — archive des lectures : theme.md + day-1.md … day-7.md
```

## Ajuster le format des lectures

Modifier `INSTRUCTIONS.md` : la routine relit ce fichier à chaque exécution, aucun changement de la routine elle-même n'est nécessaire.

## Gestion de la routine

La routine se gère sur https://claude.ai/code/routines (activer/désactiver, supprimer, voir les exécutions).
