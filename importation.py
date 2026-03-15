import sqlite3
import csv

# 1. Connexion à la base
db = sqlite3.connect("base_de_donnée.db")
curseur = db.cursor()

def importer_donnees(nom_fichier, table):
    with open(nom_fichier, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            # row est maintenant un dictionnaire : {'nom_colonne': 'valeur'}
            
            # On récupère les noms de colonnes du dictionnaire (les clés)
            # On les entoure de doubles guillemets pour gérer les espaces/tirets
            colonnes = ', '.join([f'"{col}"' for col in row.keys()])
            
            # On génère le même nombre de '?' que de colonnes
            placeholders = ', '.join(['?'] * len(row))
            
            # Construction de la requête SQL
            sql = f'INSERT INTO {table} ({colonnes}) VALUES ({placeholders})'
            
            # On insère les valeurs du dictionnaire dans la base
            curseur.execute(sql, tuple(row.values()))
            
    db.commit()
    print(f"Importation terminée pour {table}")

# 2. Exécution pour chaque fichier
# DictReader lit automatiquement les noms des colonnes dans le CSV
importer_donnees('donnees_geo_climatiques.csv', 'Geographiques_et_climatiques')
importer_donnees('mesures_occitanie_journaliere_pollution.csv', 'Qualite_Air')
importer_donnees('donnees_socio_economiques.csv', 'Socio_economiques')

db.close()
print("Tout est en place !")