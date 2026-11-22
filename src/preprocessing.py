"""Preprocessing et représentation des données.

Traitement des valeurs manquantes, construction des variables explicatives,
construction de la cible à l'horizon J+1 et découpage chronologique.
"""


def handle_missing_values(df, columns, strategy="interpolate", max_gap=3):
    """Traite les valeurs manquantes des colonnes d'une série temporelle.

    Args:
        df (pandas.DataFrame): série temporelle triée par date.
        columns (list): colonnes concernées.
        strategy (str): interpolate, ffill ou drop.
        max_gap (int): nombre maximal de jours consécutifs comblés.

    Returns:
        pandas.DataFrame: données dont les valeurs manquantes ont été traitées.
    """
    raise NotImplementedError


def add_lag_features(df, columns, lag_days):
    """Ajoute les valeurs des jours précédents comme nouvelles colonnes.

    Args:
        df (pandas.DataFrame): série temporelle triée par date.
        columns (list): colonnes à décaler.
        lag_days (list): décalages en jours, par exemple [1, 2, 3].

    Returns:
        pandas.DataFrame: données enrichies des colonnes nommées <colonne>_lag<k>.
    """
    raise NotImplementedError


def add_rolling_features(df, columns, windows):
    """Ajoute des moyennes glissantes calculées sur les jours précédents.

    Le jour courant est exclu de sa propre moyenne pour éviter toute fuite
    d'information vers la cible.

    Args:
        df (pandas.DataFrame): série temporelle triée par date.
        columns (list): colonnes à lisser.
        windows (list): tailles des fenêtres, par exemple [3, 7].

    Returns:
        pandas.DataFrame: données enrichies des colonnes nommées <colonne>_roll<w>.
    """
    raise NotImplementedError


def build_target(df, target_column="AQI"):
    """Construit la cible, c'est-à-dire l'AQI du jour suivant.

    Args:
        df (pandas.DataFrame): série temporelle triée par date.
        target_column (str): colonne de l'AQI du jour courant.

    Returns:
        pandas.DataFrame: données comportant une colonne target.
    """
    raise NotImplementedError


def build_feature_matrix(df, config):
    """Construit le jeu de données complet à partir de la configuration.

    Applique le traitement des valeurs manquantes, ajoute les décalages et les
    moyennes glissantes, construit la cible et retire les lignes incomplètes.
    La colonne de l'AQI du jour courant est conservée parmi les variables
    explicatives, car elle sert de base au baseline de persistance.

    Args:
        df (pandas.DataFrame): série temporelle triée d'une ville.
        config (dict): configuration du projet.

    Returns:
        tuple: (X, y, feature_names) où X est un DataFrame des variables
            explicatives, y une Series contenant l'AQI du jour suivant et
            feature_names la liste des colonnes de X.
    """
    raise NotImplementedError


def chronological_split(X, y, test_size=0.2, val_size=0.1):
    """Découpe les données en entraînement, validation et test par ordre de date.

    Les observations ne sont pas mélangées : l'entraînement porte sur les dates
    les plus anciennes et le test sur les plus récentes.

    Args:
        X (pandas.DataFrame): variables explicatives ordonnées par date.
        y (pandas.Series): cible.
        test_size (float): proportion finale réservée au test.
        val_size (float): proportion réservée à la validation.

    Returns:
        tuple: (X_train, X_val, X_test, y_train, y_val, y_test).
    """
    raise NotImplementedError
