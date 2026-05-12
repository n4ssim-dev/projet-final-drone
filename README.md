# Projet Final — Déploiement de drones en contexte épidémique

Outil d'aide à la décision pour prioriser le déploiement de drones médicaux par zone géographique, en fonction de la croissance épidémique, des besoins et des risques.

## Lancer le projet

**1. Installer les dépendances**
```bash
pip install -r requirements.txt
```

**2. Nettoyer les données épidémiques**
```bash
python epidemie.py
```
Lit `epidemie.csv`, nettoie les données (doublons, valeurs manquantes, dates) et calcule le taux de croissance géométrique par zone. Produit `epidemie_nettoye.csv`.

**3. Lancer l'analyse principale**
```bash
python main.py
```
Fusionne les données épidémiques et drones, calcule un score de priorité par zone, produit `decision_finale.csv` et le graphique `score_par_region.png`.

## Formule de scoring

```
score = (croissance × 1.1 + besoins × 0.90) − risques × 0.70
```

## Livrables

| Fichier | Description |
|---|---|
| `epidemie_nettoye.csv` | Données épidémiques nettoyées avec taux de croissance |
| `decision_finale.csv` | Tableau complet avec scores par zone |
| `score_par_region.png` | Graphique — score moyen par zone |

## Arborescence

```
.
├── epidemie.csv          # Données brutes épidémiques
├── drones_nettoye.csv    # Données drones nettoyées
├── epidemie.py           # Nettoyage & calcul de croissance
├── main.py               # Scoring & visualisation
└── requirements.txt
```

## Dépendances

- Python 3
- pandas, numpy, matplotlib
