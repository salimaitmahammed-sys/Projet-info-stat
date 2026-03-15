import sqlite3

# Connexion à la base existante
db = sqlite3.connect("base_de_donnée.db")
curseur = db.cursor()

# Requête de jointure pour extraire les données rurales de fond
# Correction de la requête SELECT
requete = """
SELECT 
    Q.nom_com AS Ville, 
    Q.nom_station, 
    Q.influence, 
    Q.valeur_poll, 
    Q.nom_poll, 
    G.population, 
    Q.typologie,
    S."evolution_annuelle_moy_de_la_population_entre_2017_et_ 2023_en_pourcentage", 
    S.population_municipale_2023
FROM Geographiques_et_climatiques G
JOIN Qualite_Air Q ON G.id_Geographique_et_climatiques = Q.id_Geographique_et_climatiques
JOIN Socio_economiques S ON G.code_insee_com = S.code_insee_com
WHERE Q.typologie = 'Urbaine' AND Q.influence = 'Fond';
"""

curseur.execute(requete)

# Exécution et récupération
curseur.execute(requete)
resultats = curseur.fetchall()

# Affichage des résultats
for ligne in resultats:
    print(ligne)

# Fermeture
db.close()
