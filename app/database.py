
import sqlite3
from config import DATA_DIR


def creer_base():
    chemin_db = DATA_DIR / "amazon.db"

    connexion = sqlite3.connect(chemin_db)

    curseur = connexion.cursor()

    curseur.execute("""
        CREATE TABLE IF NOT EXISTS produits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            prix TEXT NOT NULL
        )
    """)

    connexion.commit()
    connexion.close()


def enregistrer_produits(produits):
    chemin_db = DATA_DIR / "amazon.db"

    connexion = sqlite3.connect(chemin_db)
    curseur = connexion.cursor()

    curseur.executemany("""
        INSERT INTO produits (nom, prix)
        VALUES (?, ?)
    """, produits)

    connexion.commit()
    connexion.close()
