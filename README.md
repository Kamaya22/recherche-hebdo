# Recherche — une lecture tous les deux jours

Automatisation personnelle : chaque thématique scientifique ou sociale est explorée sur **deux semaines, en 7 lectures envoyées tous les deux jours**. Un jour sur deux à ~6h00 (Europe/Paris), un agent Claude planifié dans le cloud produit une lecture d'environ 30 minutes (avec 1 à 3 vidéos YouTube en anglais, ≥ 200 000 vues, chaînes reconnues) et l'envoie par email à la mailing list, à partir exclusivement de sources fiables acceptées par la communauté scientifique.

## Fonctionnement

- **Routine cloud Claude** : se réveille tous les jours (cron `0 5 * * *` UTC), lit `INSTRUCTIONS.md` et décide si c'est un jour de lecture. Le calendrier est fixé par la ligne `Start: YYYY-MM-DD` du `theme.md` du cycle en cours : lectures à J+0, J+2 … J+12 ; les jours impairs, l'agent s'arrête sans rien pousser (pas de mail). Un `cron` « tous les 2 jours » (`*/2`) n'est pas utilisé car il compte les jours du mois et se décale à chaque fin de mois de 31 jours.
- **Nouveau cycle** (J+14) : l'agent prend le premier thème de `themes/backlog.md` (priorité aux thèmes `validé`), crée `weeks/<YYYY-Www>/theme.md` (semaine ISO du premier jour) et réapprovisionne le backlog si besoin.
- **Jour de lecture** : l'agent rédige la lecture N (`weeks/<cycle>/day-N.md`, N = 1 … 7) et pousse sa branche de session ; `promote-to-main.yml` la publie sur `main`.
- **Envoi de l'email** : la GitHub Action `.github/workflows/send-reading.yml` détecte chaque nouveau `day-N.md` publié et l'envoie par email (SMTP Gmail) au destinataire défini par la variable de repo `MAIL_TO` (la mailing list ; à défaut, kamilmahmal22@gmail.com). Secrets requis dans le repo : `MAIL_USERNAME` (adresse Gmail, déjà configuré) et `MAIL_APP_PASSWORD` (mot de passe d'application Google, créé sur https://myaccount.google.com/apppasswords). Le connecteur Gmail de claude.ai ne sait que créer des brouillons : il n'est pas utilisé pour la livraison.

## Comment piloter les thématiques

Éditer `themes/backlog.md` (depuis GitHub web, l'app mobile GitHub, ou ce dossier local) :

- Changer le statut d'un thème de `proposé` à `validé` pour le confirmer.
- Réordonner les lignes pour changer la priorité (l'agent prend le premier `validé`, sinon le premier `proposé`).
- Supprimer ou ajouter des thèmes librement.

## Traçabilité et statistiques des sources

Pour pouvoir **vérifier** (et pas seulement espérer) que les lectures restent diversifiées et de qualité dans la durée, chaque source citée est enregistrée comme donnée structurée dans `data/` :

- **`data/registry.csv`** — registre canonique des **revues/venues**, étiquetées par **éditeur**, **type**, **discipline** et **pays**. C'est le fichier que tu **audites et corriges** : ouvre-le, rectifie un classement, traite les lignes `to-verify`, puis pousse. Taxonomie complète dans `data/README.md`. **Tu gardes le dernier mot.**
- **`data/citations/<YYYY-Www>-day-N.json`** — toutes les sources citées par une lecture (liste « Today's readings » **et** études mentionnées dans le texte), avec type de preuve, open access, peer-review et année — écrites par l'agent le jour même.
- **`data/STATS.md`** — tableaux statistiques **déterministes** (par éditeur, type de preuve, open access, discipline, pays, année, venues les plus citées, évolution par semaine, alertes de concentration), régénérés automatiquement à chaque push par la GitHub Action `build-stats.yml`. Fichier généré : ne pas l'éditer à la main.
- **Rapport de cycle** : à la **lecture 7**, l'agent écrit une analyse interprétée de la diversité des sources du cycle (`rapports/<cycle>.md`), envoyée par email via `send-report.yml`. La lecture 7 envoie donc deux mails (la lecture + le rapport).
- **Aperçu visuel local** : `python tools/preview_stats.py --open` ouvre un tableau de bord HTML (`stats-preview.html`, ignoré par git).

## Structure

```
INSTRUCTIONS.md           — instructions complètes de l'agent (format, qualité, traçabilité, rapport)
themes/backlog.md         — thèmes à venir (éditable à tout moment)
themes/history.md         — thèmes déjà traités
weeks/<YYYY-Www>/         — un dossier par cycle de 2 semaines : theme.md (avec Start:) + day-1.md … day-7.md
data/README.md            — codebook : colonnes du registre et taxonomie des sources
data/registry.csv         — registre canonique des revues/venues (auditable)
data/citations/<...>.json — sources citées par chaque lecture
data/STATS.md             — statistiques déterministes (généré automatiquement)
rapports/<YYYY-Www>.md    — rapports de diversité des sources, un par cycle
tools/build_stats.py      — génère data/STATS.md à partir des citations + registre
```

## Ajuster le format des lectures

Modifier `INSTRUCTIONS.md` : la routine relit ce fichier à chaque exécution, aucun changement de la routine elle-même n'est nécessaire. Pour corriger l'étiquetage des sources, éditer `data/registry.csv` (`STATS.md` se recalcule au push suivant).

## Mailing list

Les lectures sont envoyées au Google Group **recherche-hebdo@googlegroups.com**. S'abonner / se désabonner : https://groups.google.com/g/recherche-hebdo (chaque mail du groupe contient aussi un lien de désabonnement). Pour changer de destinataire, modifier la variable `MAIL_TO` du repo (Settings → Secrets and variables → Actions → Variables) — aucun commit nécessaire.

## Gestion de la routine

La routine se gère sur https://claude.ai/code/routines (activer/désactiver, supprimer, voir les exécutions).
