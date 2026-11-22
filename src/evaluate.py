"""Calcul des métriques et comparaison avec le baseline de persistance."""


def compute_metrics(y_true, y_pred):
    """Calcule les métriques de régression entre valeurs réelles et prédites.

    Args:
        y_true (array-like): valeurs réelles de l'AQI du jour suivant.
        y_pred (array-like): valeurs prédites.

    Returns:
        dict: dictionnaire contenant les clés mae, rmse et r2.
    """
    raise NotImplementedError


def print_metrics(name, metrics):
    """Affiche les métriques d'un modèle sur une ligne lisible.

    Args:
        name (str): nom du modèle ou du baseline.
        metrics (dict): dictionnaire renvoyé par compute_metrics.
    """
    raise NotImplementedError


def compare_with_baseline(model_metrics, baseline_metrics):
    """Mesure l'écart de performance entre un modèle et le baseline.

    Args:
        model_metrics (dict): métriques du modèle.
        baseline_metrics (dict): métriques du baseline de persistance.

    Returns:
        float: amélioration relative de la MAE en pourcentage, positive lorsque
            le modèle fait mieux que le baseline.
    """
    raise NotImplementedError
