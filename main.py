import pandas as pd

# les placeholders sont actuellement sales
epi = pd.read_csv("epidemie_nettoye.csv")
dr = pd.read_csv("drones_nettoye.csv")

# fusion
# df["score"] = 
# classement

df.to_csv("decision_finale.csv", index=False)