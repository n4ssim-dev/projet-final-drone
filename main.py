import pandas as pd
import numpy as np

epi = pd.read_csv("epidemie_nettoye.csv")
dr = pd.read_csv("drones_nettoye.csv")

# Fusionner les données nettoyés en un tableau
df = pd.merge(epi, dr, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), indicator=False, validate=None)

# TODO : Création d'une fonction de scoring
def scoring():
    df['score'] = np.nan
    # urgence = (croissance * besoin) / risques

    # ratio urgence / risque(risque)
    for index, row in df.iterrows():
        croissance = df.at[index, 'croissance']
        besoins = df.at[index, 'besoins']
        risques = df.at[index, 'risques']

        df.at[index, 'score'] = round((croissance * besoins) / risques, 1)

    return df;

df = scoring()

# TODO : Classer les zones par priorité
# TODO : Identifier la zone prioritaire

# Rend un dictionnaire incluant la somme des scores 
def zone_score(dataframe):
    scores = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
        'E': 0
    }

    for _, row in dataframe.iterrows():
        zone = row['zone']
        if zone in scores:
            scores[zone] += round(row['score'] / 10) # Moyenne par zone

    return scores

zone_score = zone_score(dataframe=df)
print(zone_score)


# TODO : Convertir le dataframe en tableur csv (livrable final)
df.to_csv("decision_finale.csv", index=False)