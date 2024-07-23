import numpy as np
import pandas as pd
import chardet
import simple_graph as pp
import database as db
# Lire le fichier en mode binaire
#with open('teams_2021-2022_stats.xlsx', 'rb') as f:
#    result = chardet.detect(f.read())

# Afficher l'encodage détecté
#print(result)
regular_season = pd.read_excel('teams_2021-2022_stats.xlsx')
#print(regular_season.head(5))

#pp.plot_data(regular_season)

donnee = db.database("teams_2021-2022_stats.xlsx")
print(donnee.show_columns())