"""Preprocessing et représentation des données.

Traitement des valeurs manquantes, construction des variables explicatives,
construction de la cible à l'horizon J+1 et découpage chronologique.
"""

import pandas as pd


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
    df = df.copy()
    # Une colonne demandée dans la config peut être absente du fichier.
    present = [c for c in columns if c in df.columns]

    if strategy == "interpolate":
        df[present] = df[present].interpolate(method="linear", limit=max_gap)
    elif strategy == "ffill":
        df[present] = df[present].ffill(limit=max_gap)
    elif strategy == "drop":
        # Attention : supprimer des jours casse la continuité des décalages.
        df = df.dropna(subset=present)
    else:
        raise ValueError(f"Stratégie inconnue : {strategy}")

    return df


def add_lag_features(df, columns, lag_days):
    """Ajoute les valeurs des jours précédents comme nouvelles colonnes.

    Args:
        df (pandas.DataFrame): série temporelle triée par date.
        columns (list): colonnes à décaler.
        lag_days (list): décalages en jours, par exemple [1, 2, 3].

    Returns:
        pandas.DataFrame: données enrichies des colonnes nommées <colonne>_lag<k>.
    """
    df = df.copy()
    for col in columns:
        if col not in df.columns:
            continue
        for k in lag_days:
            df[f"{col}_lag{k}"] = df[col].shift(k)
    return df


def add_rolling_features(df, columns, windows):
    """Ajoute des moyennes glissantes calculées sur les derniers jours.

    La moyenne porte sur le jour courant et les jours précédents, tous connus
    au moment de prédire l'AQI du lendemain.

    Args:
        df (pandas.DataFrame): série temporelle triée par date.
        columns (list): colonnes à lisser.
        windows (list): tailles des fenêtres, par exemple [3, 7].

    Returns:
        pandas.DataFrame: données enrichies des colonnes nommées <colonne>_roll<w>.
    """
    df = df.copy()
    for col in columns:
        if col not in df.columns:
            continue
        for w in windows:
            # Fenêtre non centrée : center=True ferait entrer le lendemain.
            df[f"{col}_roll{w}"] = df[col].rolling(window=w).mean()
    return df


def build_target(df, target_column="AQI"):
    """Construit la cible, c'est-à-dire l'AQI du jour suivant.

    Args:
        df (pandas.DataFrame): série temporelle triée par date.
        target_column (str): colonne de l'AQI du jour courant.

    Returns:
        pandas.DataFrame: données comportant une colonne target.
    """
    df = df.copy()
    df["target"] = df[target_column].shift(-1)
    return df


def build_feature_matrix(df, config):
    """Construit le jeu de données complet à partir de la configuration.

    La cible est construite avant le traitement des valeurs manquantes, pour
    qu'elle corresponde toujours à une mesure réelle. Ensuite les trous courts
    sont comblés, les décalages et les moyennes glissantes sont ajoutés, et les
    lignes encore incomplètes sont retirées. La colonne de l'AQI du jour
    courant reste parmi les variables explicatives, car elle sert de base au
    baseline de persistance.

    Args:
        df (pandas.DataFrame): série temporelle triée d'une ville.
        config (dict): configuration du projet.

    Returns:
        tuple: (X, y, feature_names) où X est un DataFrame des variables
            explicatives, y une Series contenant l'AQI du jour suivant et
            feature_names la liste des colonnes de X.
    """
    pcfg = config["preprocessing"]
    target_col = config["data"]["target_column"]

    base_cols = [c for c in pcfg["features"] + [target_col] if c in df.columns]

    df = build_target(df, target_col)
    df = handle_missing_values(df, base_cols, pcfg["missing_value_strategy"], pcfg["max_gap"])
    df = add_lag_features(df, base_cols, pcfg["lag_days"])
    df = add_rolling_features(df, base_cols, pcfg["rolling_windows"])

    feature_names = list(base_cols)
    for col in base_cols:
        feature_names += [f"{col}_lag{k}" for k in pcfg["lag_days"]]
        feature_names += [f"{col}_roll{w}" for w in pcfg["rolling_windows"]]

    # Le filtre ne porte que sur les colonnes utilisées : les polluants non
    # retenus, souvent très incomplets, ne font pas supprimer de lignes.
    df = df.dropna(subset=feature_names + ["target"]).reset_index(drop=True)

    X = df[feature_names]
    y = df["target"]
    return X, y, feature_names


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
    n = len(X)
    n_test = int(n * test_size)
    n_val = int(n * val_size)
    n_train = n - n_val - n_test

    X_train, y_train = X.iloc[:n_train], y.iloc[:n_train]
    X_val, y_val = X.iloc[n_train:n_train + n_val], y.iloc[n_train:n_train + n_val]
    X_test, y_test = X.iloc[n_train + n_val:], y.iloc[n_train + n_val:]

    return X_train, X_val, X_test, y_train, y_val, y_test