import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

        df.at[index, 'score'] = round((croissance * 1.1 + besoins * 0.90) - risques * 0.70, 2)

    return df;

df = scoring()

# TODO : Classer les zones par priorité
# & Identifier la zone prioritaire

zone_score = df.groupby("zone")["score"].mean().round(2).sort_values(ascending=False)

# TODO : Convertir le dataframe en tableur csv (livrable final)
df.to_csv("decision_finale.csv", index=False)

# TODO : Tableau score moyen par zone
zone_stats = df.groupby("zone")[["croissance", "besoins", "risques"]].mean()

croissance_med = zone_stats["croissance"].median()
besoins_med    = zone_stats["besoins"].median()
risques_med    = zone_stats["risques"].median()

tick_labels = []

# Assigne le type de croissance/besoin/risques(haut ou bas) au df zone_stats pour chaque zones
for zone in zone_score.index:
    c = "Haute croissance" if zone_stats.loc[zone, "croissance"] >= croissance_med else "Faible croissance"
    b = "Haut besoin" if zone_stats.loc[zone, "besoins"] >= besoins_med else "Faible besoin"
    r = "Haut risque" if zone_stats.loc[zone, "risques"] >= risques_med else "Faible risque"
    tick_labels.append(f"{zone}\n{c}\n{b}\n{r}")

print(zone_stats)

plt.figure(figsize=(12, 8))
plt.bar(zone_score.index, zone_score.values, align='center')
plt.xticks(range(len(zone_score.index)), tick_labels, fontsize=8)

plt.title("Score moyen par zones.")
plt.ylabel("Score moyen")
plt.grid(True)
plt.tight_layout()
plt.savefig('score_par_region.png')
plt.close()

# TODO : BONUS 1: 