"""Script de test et d'inférence, indépendant de l'entraînement.

Charge le modèle déjà enregistré et montre son utilisation sur de nouveaux
exemples. Ne relance pas l'entraînement.

    python test.py
    python test.py --config configs/config.yaml --n 5
"""

import argparse


def parse_args():
    """Lit les arguments de la ligne de commande.

    Returns:
        argparse.Namespace: arguments analysés, dont le chemin de configuration
            et le nombre d'exemples à prédire.
    """
    parser = argparse.ArgumentParser(description="Inférence de l'AQI J+1.")
    parser.add_argument("--config", default="configs/config.yaml",
                        help="Chemin du fichier de configuration.")
    parser.add_argument("--n", type=int, default=5,
                        help="Nombre d'exemples les plus récents à prédire.")
    return parser.parse_args()


def main():
    """Charge le modèle enregistré et affiche ses prévisions.

    Reconstruit les variables explicatives de la ville étudiée, sélectionne les
    exemples les plus récents et affiche pour chacun l'AQI du jour courant, la
    prévision du modèle, celle du baseline de persistance et la valeur réelle.
    """
    raise NotImplementedError


if __name__ == "__main__":
    main()
