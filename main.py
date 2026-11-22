"""Point d'entrée de l'entraînement.

Exécute le pipeline complet : chargement des données, preprocessing,
entraînement, évaluation puis enregistrement du modèle.

    python main.py
    python main.py --config configs/config.yaml
"""

import argparse


def parse_args():
    """Lit les arguments de la ligne de commande.

    Returns:
        argparse.Namespace: arguments analysés, dont le chemin de configuration.
    """
    parser = argparse.ArgumentParser(description="Entraînement du modèle AQI J+1.")
    parser.add_argument("--config", default="configs/config.yaml",
                        help="Chemin du fichier de configuration.")
    return parser.parse_args()


def main():
    """Enchaîne les étapes du pipeline d'entraînement.

    Charge la configuration, construit le jeu de données de la ville étudiée,
    découpe les données par ordre de date, entraîne le modèle, compare ses
    performances au baseline de persistance sur le jeu de test et enregistre le
    modèle à l'emplacement indiqué par la configuration.
    """
    raise NotImplementedError


if __name__ == "__main__":
    main()
