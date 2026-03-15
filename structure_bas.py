import sqlite3

# 1. Connexion à TA base de données
connecte = sqlite3.connect("base_de_donnée.db")
curseur = connecte.cursor()

# 2. Fonction pour voir tes colonnes (pour t'aider dans tes SELECT)
def voir_structure_table(table):
    print(f"\n--- Colonnes de la table : {table} ---")
    curseur.execute(f"PRAGMA table_info({table})")
    for col in curseur.fetchall():
        print(f"Nom colonne : {col[1]}") # col[1] c'est le nom exact dans la DB

# 3. Tu appelles cette fonction pour chaque table
voir_structure_table("Geographiques_et_climatiques")
voir_structure_table("Qualite_Air")
voir_structure_table("Socio_economiques")

# 4. Maintenant tu peux écrire tes SELECT avec les VRAIS noms
# curseur.execute("SELECT ... FROM ...")

connecte.close()