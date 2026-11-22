"""Fonctions utilitaires : configuration, reproductibilité, sauvegarde du modèle."""


def load_config(config_path="configs/config.yaml"):
    """Charge le fichier de configuration YAML.

    Args:
        config_path (str): chemin du fichier de configuration.

    Returns:
        dict: contenu complet de la configuration.
    """
    raise NotImplementedError


def set_seed(seed=42):
    """Fixe les graines aléatoires pour rendre les résultats reproductibles.

    Args:
        seed (int): valeur de la graine.
    """
    raise NotImplementedError


def save_model(model, path):
    """Enregistre un modèle entraîné sur le disque.

    Args:
        model: estimateur scikit-learn entraîné.
        path (str): chemin du fichier de sortie, extension .pkl.
    """
    raise NotImplementedError


def load_model(path):
    """Charge un modèle enregistré précédemment.

    Args:
        path (str): chemin du fichier .pkl.

    Returns:
        L'estimateur chargé.
    """
    raise NotImplementedError
