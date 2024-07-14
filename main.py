import numpy as np
import pandas as pd
import chardet

# Lire le fichier en mode binaire
with open('stats_regular.csv', 'rb') as f:
    result = chardet.detect(f.read())

# Afficher l'encodage détecté
print(result)
regular_season = pd.read_csv('stats_regular.csv', encoding=result['encoding'])
print(regular_season.head(5))

