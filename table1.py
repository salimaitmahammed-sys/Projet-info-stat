import sqlite3
import csv

# Connexion à la base SQLite
conn = sqlite3.connect("ma_base.db")
cur = conn.cursor()

# Création de la table
cur.execute("""
CREATE TABLE IF NOT EXISTS utilisateur (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT,
    age INTEGER,
    email TEXT
)
""")

# Lecture du fichier CSV
with open("utilisateurs.csv", newline="", encoding="utf-8") as fichier:
    lecteur = csv.reader(fichier)
    next(lecteur)  # saute l'en-tête

    for ligne in lecteur:
        cur.execute(
            "INSERT INTO utilisateur (nom, age, email) VALUES (?, ?, ?)",
            ligne
        )

# Validation et fermeture
conn.commit()
conn.close()

print("CSV importé avec succès ✅")