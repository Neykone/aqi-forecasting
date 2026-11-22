"""Chargement du dataset Air Quality Data in India et sélection d'une ville."""


def load_data(path, date_column="Date"):
    """Lit le fichier CSV brut et convertit la colonne de date.

    Args:
        path (str): chemin du fichier CSV, par exemple data/city_day.csv.
        date_column (str): nom de la colonne contenant les dates.

    Returns:
        pandas.DataFrame: données brutes, colonne de date au format datetime.
    """
    raise NotImplementedError


def filter_city(df, city, city_column="City"):
    """Ne conserve que les lignes correspondant à une ville.

    Args:
        df (pandas.DataFrame): données de toutes les villes.
        city (str): ville à conserver.
        city_column (str): nom de la colonne des villes.

    Returns:
        pandas.DataFrame: sous-ensemble correspondant à la ville.
    """
    raise NotImplementedError


def sort_by_date(df, date_column="Date"):
    """Trie les observations par date croissante.

    Args:
        df (pandas.DataFrame): données d'une ville.
        date_column (str): nom de la colonne de date.

    Returns:
        pandas.DataFrame: données triées, index réinitialisé.
    """
    raise NotImplementedError


def get_city_series(path, city, date_column="Date", city_column="City"):
    """Enchaîne la lecture du fichier, la sélection de la ville et le tri par date.

    Args:
        path (str): chemin du fichier CSV brut.
        city (str): ville à étudier.
        date_column (str): nom de la colonne de date.
        city_column (str): nom de la colonne des villes.

    Returns:
        pandas.DataFrame: série temporelle de la ville, triée par date.
    """
    raise NotImplementedError
