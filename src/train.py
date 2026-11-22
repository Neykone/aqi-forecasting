"""Entraînement des modèles et recherche des hyperparamètres."""


def build_pipeline(model):
    """Assemble un pipeline composé d'une standardisation puis du modèle.

    Les étapes sont nommées scaler et model, ce dernier nom correspondant au
    préfixe utilisé dans les grilles d'hyperparamètres.

    Args:
        model: estimateur scikit-learn.

    Returns:
        sklearn.pipeline.Pipeline: pipeline non entraîné.
    """
    raise NotImplementedError


def train_model(X_train, y_train, config):
    """Entraîne le modèle en recherchant ses hyperparamètres.

    La recherche utilise une validation croisée adaptée aux séries temporelles,
    dont le nombre de découpages est donné par la configuration.

    Args:
        X_train (pandas.DataFrame): variables explicatives d'entraînement.
        y_train (pandas.Series): cible d'entraînement.
        config (dict): configuration du projet.

    Returns:
        tuple: (best_estimator, best_params) où best_estimator est le pipeline
            entraîné avec les meilleurs hyperparamètres et best_params le
            dictionnaire de ces hyperparamètres.
    """
    raise NotImplementedError
