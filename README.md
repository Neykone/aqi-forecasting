# Forecasting Urban Air Quality (AQI) in Indian Cities

Prévision de l'AQI du jour suivant (J+1) pour une ville indienne à partir des mesures du jour courant et des jours précédents. Tâche principale : régression. Les prévisions sont comparées à un baseline de persistance qui prédit l'AQI de demain avec l'AQI d'aujourd'hui.

Projet intégré de Machine Learning, année 2026/2027.

## Dataset

Air Quality Data in India, disponible sur Kaggle :
https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india

Télécharger le fichier `city_day.csv` et le placer dans le dossier `data/`. Les données ne sont pas versionnées sur GitHub.

## Installation

```bash
git clone https://github.com/<utilisateur>/aqi-forecasting.git
cd aqi-forecasting

python -m venv .venv
source .venv/bin/activate        # Windows : .venv\Scripts\activate

pip install -r requirements.txt
```

## Utilisation

Entraînement complet (chargement, preprocessing, entraînement, évaluation, sauvegarde du modèle) :

```bash
python main.py
```

Test et inférence avec le modèle déjà entraîné, indépendamment de l'entraînement :

```bash
python test.py
```

## Structure

```
aqi-forecasting/
├── README.md
├── requirements.txt
├── main.py                 Point d'entrée de l'entraînement
├── test.py                 Test et inférence avec le modèle entraîné
├── configs/
│   └── config.yaml         Hyperparamètres et configuration
├── src/
│   ├── data.py             Chargement et gestion du dataset
│   ├── preprocessing.py    Preprocessing et représentation
│   ├── model.py            Définition des modèles
│   ├── train.py            Logique d'entraînement
│   ├── evaluate.py         Évaluation et métriques
│   └── utils.py            Fonctions utilitaires
├── notebooks/              Exploration des données
├── models/                 Modèle entraîné
├── data/                   Dataset (non versionné)
└── docs/
    └── PLAN.md             Répartition des tâches
```

## Équipe

La répartition des tâches est décrite dans `docs/PLAN.md`.
