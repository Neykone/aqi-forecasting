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

## Contrat entre les parties

Les signatures des fonctions et la configuration sont déjà fixées dans les fichiers. Chacun remplit le corps des fonctions de sa partie en respectant ce qui entre et ce qui sort, décrit dans les docstrings.

Si une signature doit changer, le signaler au groupe avant, parce que les autres parties s'appuient dessus. Les valeurs de `configs/config.yaml` sont une base de départ et peuvent être ajustées au fil des essais.

| Partie | Fonctions à écrire |
|--------|--------------------|
| Données et exploration | `load_data`, `filter_city`, `sort_by_date`, `get_city_series` |
| Preprocessing et représentation | `handle_missing_values`, `add_lag_features`, `add_rolling_features`, `build_target`, `build_feature_matrix`, `chronological_split` |
| Modélisation | `get_model_and_grid`, `persistence_baseline`, `build_pipeline`, `train_model` |
| Évaluation et résultats | `compute_metrics`, `print_metrics`, `compare_with_baseline` |

`src/utils.py` (`load_config`, `set_seed`, `save_model`, `load_model`) et les `main()` de `main.py` et `test.py` sont à prendre par celui qui a fini en premier.

## Organisation Git

La branche `main` est protégée : les push directs y sont refusés et toute modification passe par une Pull Request. Le dataset n'est pas versionné (voir `.gitignore`), chacun le télécharge en local.

### Installation, une seule fois

```bash
git clone https://github.com/<utilisateur>/aqi-forecasting.git
cd aqi-forecasting

python -m venv .venv
.venv\Scripts\activate          # macOS ou Linux : source .venv/bin/activate

pip install -r requirements.txt
```

Puis placer `city_day.csv` dans le dossier `data/`.

### Travailler sur sa partie

Créer sa branche depuis un `main` à jour :

```bash
git checkout main
git pull
git checkout -b preprocessing
```

Noms de branches suggérés : `data`, `preprocessing`, `modelisation`, `evaluation`.

Enregistrer son travail, aussi souvent que voulu :

```bash
git add .
git commit -m "Implement missing value handling"
```

Envoyer la branche sur GitHub :

```bash
git push -u origin preprocessing
```

Les fois suivantes, `git push` suffit.

### Ouvrir la Pull Request

Après le push, un bandeau apparaît sur la page du dépôt avec un bouton **Compare & pull request**. Sinon : onglet **Pull requests** puis **New pull request**, avec `main` à gauche et sa branche à droite.

Décrire en deux lignes ce que la branche apporte, puis demander la relecture à quelqu'un du groupe. La fusion se fait avec le bouton **Merge pull request**, une fois la PR approuvée.

### Récupérer le travail des autres

Après chaque fusion dans `main`, remettre sa propre branche à jour pour éviter les conflits :

```bash
git checkout main
git pull
git checkout preprocessing
git merge main
```

### En cas de conflit

Git indique les fichiers concernés. Les ouvrir dans VS Code, choisir quoi garder entre les marqueurs `<<<<<<<` et `>>>>>>>`, puis :

```bash
git add .
git commit
```

## Plan du rapport attendu

1. Objectif de la tâche
2. Pipeline de preprocessing et justification des choix
3. Modèles et espace de recherche des hyperparamètres
4. Méthodologie d'évaluation, résultats et discussion
5. Limites et pistes d'amélioration
