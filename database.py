import numpy as np
import pandas as pd


class database:
    def __init__(self, file_path, sheet_name="team 2021-2022 stats regular"):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self._load_data()

    def _load_data(self):
        # Charger le fichier Excel dans un DataFrame pandas
        self.df = pd.read_excel(self.file_path, sheet_name=self.sheet_name)
        # Dynamiquement créer des attributs pour chaque colonne
        for column in self.df.columns:
            setattr(self, column, self.df[column])

    def get_column(self, column_name):
        # Retourner la colonne demandée si elle existe
        if column_name in self.df.columns:
            return getattr(self, column_name)
        else:
            raise ValueError(f"La colonne {column_name} n'existe pas dans la base de données.")

    def reload_data(self):
        # Recharger les données depuis le fichier Excel
        self._load_data()

    def show_columns(self):
        # Afficher les colonnes disponibles
        return self.df.columns.tolist()
