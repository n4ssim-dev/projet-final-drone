import pandas as pd
import numpy as np

df = pd.read_csv("epidemie.csv", sep=',', encoding="utf-8-sig")


# nettoyer dates
df['date'] = pd.to_datetime(df['date'].str.strip(), format='mixed', errors='coerce')
df['zone'] = df['zone'].str.strip().str.upper() # supprimer espaces et mettre en Maj

# Source - https://stackoverflow.com/a/25835810
# Posted by Thomas
# Retrieved 2026-05-12, License - CC BY-SA 3.0

# supprimer doublons
df = df.drop_duplicates(subset=['date','zone','infectes'])

# trier par zone + date (zone en premier pour le calcul des variations par zone)
df = df.sort_values(['zone', 'date'], ascending=[True, True])

# ajouter une valeur à une case vide en faisant la moyenne des infectés
df['infectes'] = df['infectes'].replace('', np.nan)
df['infectes'] = pd.to_numeric(df['infectes'], errors='coerce')
df['infectes'] = round(df['infectes'].fillna(df['infectes'].mean()))

#changer les valeurs négative en utilisant la méthode abs dans la colonnes souhaité
df['infectes'] = df['infectes'].abs()

#définir les colonnes pour le moment vides
df['variation'] = np.nan
df['croissance'] = np.nan

# calcul des variations et taux de croissance géométrique par zone
zones = df["zone"].unique()

for z in zones:
    df_z = df[df["zone"] == z].sort_values("date")

    I_debut = df_z["infectes"].iloc[0]
    I_fin = df_z["infectes"].iloc[-1]
    n = len(df_z) - 1
    croissance = (I_fin / I_debut) ** (1 / n) if n > 0 and I_debut != 0 else 1

    df.loc[df["zone"] == z, "croissance"] = round(croissance, 4)
    df.loc[df["zone"] == z, "variation"] = df_z["infectes"].diff().reindex(df_z.index).round()

    print(f"Zone {z} : croissance moyenne = {croissance:.4f} par jour")

df.to_csv("epidemie_nettoye.csv", index=False)
