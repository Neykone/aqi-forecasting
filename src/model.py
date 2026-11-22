"""Définition des modèles et du baseline de persistance."""


def get_model_and_grid(config):
    """Construit l'estimateur demandé et sa grille d'hyperparamètres.

    Le type de modèle et les grilles sont lus dans la section model de la
    configuration. Les clés de la grille sont préfixées par model__ car
    l'estimateur est utilisé dans un Pipeline.

    Args:
        config (dict): configuration du projet.

    Returns:
        tuple: (model, param_grid) où model est un estimateur scikit-learn non
            entraîné et param_grid un dictionnaire d'espaces de recherche.
    """
    raise NotImplementedError


def persistence_baseline(X, target_column="AQI"):
    """Prédit l'AQI du jour suivant en recopiant l'AQI du jour courant.

    Référence imposée par le sujet, à laquelle les modèles sont comparés.

    Args:
        X (pandas.DataFrame): variables explicatives contenant l'AQI du jour courant.
        target_column (str): nom de la colonne de l'AQI du jour courant.

    Returns:
        numpy.ndarray: prédictions du baseline.
    """
    raise NotImplementedError
