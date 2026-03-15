#Problématique: Comment le niveau de vie impacte la qualité de l’aire  
#Objectif: Extraire des tables depuis la base donnée

#Etape du code: 
#Import de la bibliotec Sqlite3
import sqlite3

#Initialisation variable "connecte", qui vas ce connecter à la base de donné
connecte = sqlite3.connect("base_de_donnée.db")
#Initialisation du curseur qui permet de parcourir et traiter le résultat de l’exécution d’une requête.
curseur = connecte.cursor()

#Permet de recrée les vue si on modifie la requete 
curseur.execute("DROP VIEW IF EXISTS Vue_Montauban")
curseur.execute("DROP VIEW IF EXISTS Vue_Narbonne")


#Extraction des attribus des tables: Geographiques_et_climatiques,Qualite_Air et ocio_economiques
#Q -> Qualité de l'aire, S: Socio_economique, G: Geographiques_et_climatiques
curseur.execute(
# 1/SELECT --> Selection des attribus
# 2/FROM --> Selection de la table Geographiques_et_climatiques
# 3/JOIN --> Jointure entre les table Geographiques_et_climatiques, Qualite_Air et Socio_economiques
#4/WHERE --> ,condition sur les attribue nom_com,typologie, influence
"""
SELECT Q.nom_com AS Ville,Q.nom_station , Q.influence , Q.valeur_poll, Q.nom_poll, G.population, Q.typologie,
S."evolution_annuelle_moy_de_la_population_entre_2017_et_ 2023_en_pourcentage", S.population_municipale_2023
FROM Geographiques_et_climatiques G
JOIN Qualite_Air Q ON G.id_Geographique_et_climatiques = Q.id_Geographique_et_climatiques
JOIN Socio_economiques S ON G.code_insee_com = S.code_insee_com
WHERE Q.typologie = 'Urbaine' AND Q.influence = 'Fond';

"""
)

#Extraction des donnees
resultats = curseur.fetchall()
print("\ndonnees affichee")

#Creation d'une VUE MONTAUBAN 
curseur.execute(
#CREATE --> creation de la vue Montauban 
#SELECT --> selection des attribue 
#FROM --> selection de la table Qualité de l'aire
#WHERE --> contidion pour afficher que les donner de la ville montauban 
"""
CREATE VIEW Vue_Montauban AS
SELECT Q.nom_com, Q.valeur_poll, Q.nom_poll, S.niveau_vie_median_2021, S.population_municipale_2023
FROM Qualite_Air Q
JOIN Socio_economiques S ON Q.nom_com = S.nom_com
WHERE Q.nom_com = 'Montauban'

"""
)

#Creation d'une VUE NARBONNE 
curseur.execute(
#CREATE --> creation de la vue Narbonne 
#SELECT --> selection des attribue 
#FROM --> selection de la table Qualité de l'aire
#WHERE --> contidion pour afficher que les donner de la ville Narbonne 
"""
CREATE VIEW Vue_Narbonne AS
SELECT Q.nom_com, Q.valeur_poll, Q.nom_poll, S.niveau_vie_median_2021, S.population_municipale_2023
FROM Qualite_Air Q
JOIN Socio_economiques S ON Q.nom_com = S.nom_com
WHERE Q.nom_com = 'Narbonne'

"""
)

#Extraction des donnees sur les vues ( modifie les select si besoin de donnee specifique )
curseur.execute("SELECT * from Vue_Montauban")
Montauban = curseur.fetchall()

curseur.execute("SELECT * from Vue_Narbonne")
Narbonna = curseur.fetchall()


# Valider les créations de vues dans le fichier .db
connecte.commit()
print("\nVues créées avec succès.")

#Fermer
connecte.close()

