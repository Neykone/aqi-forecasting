# Répartition des tâches — Projet AQI Forecasting

**Sujet 11 :** prévoir l'AQI du jour suivant (J+1) d'une ville indienne à partir des mesures du jour courant et des jours précédents. Tâche principale : régression. Les prévisions sont comparées à un baseline de persistance (AQI de demain = AQI d'aujourd'hui).

Extension optionnelle : classer la catégorie d'AQI du jour suivant.

## Les 4 parties

| Partie | Contenu | Fichiers |
|--------|---------|----------|
| Données et exploration | Chargement du dataset, exploration, analyse des valeurs manquantes dans la série temporelle, choix de la ville | `src/data.py`, `notebooks/` |
| Preprocessing et représentation | Traitement des valeurs manquantes, construction des variables, construction de la cible J+1 | `src/preprocessing.py` |
| Modélisation | Baseline de persistance, modèles vus en cours, recherche d'hyperparamètres | `src/model.py`, `src/train.py` |
| Évaluation et résultats | Méthodologie d'évaluation, métriques, comparaison au baseline | `src/evaluate.py` |

Les fichiers `main.py` (entraînement complet), `test.py` (inférence) et `configs/config.yaml` sont communs.

Le rapport (5-6 pages) et la présentation (15 min) sont rédigés par tout le groupe, chacun sur la partie dont il s'est occupé.

## Organisation Git

- Une branche par partie plutôt que de travailler directement sur `main` : `git checkout -b <nom-de-la-branche>`
- Pull Request vers `main`, relue par quelqu'un d'autre avant la fusion
- Le dataset n'est pas versionné (voir `.gitignore`), chacun le télécharge en local

## Plan du rapport attendu

1. Objectif de la tâche
2. Pipeline de preprocessing et justification des choix
3. Modèles et espace de recherche des hyperparamètres
4. Méthodologie d'évaluation, résultats et discussion
5. Limites et pistes d'amélioration
