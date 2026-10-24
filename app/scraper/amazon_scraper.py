
from app.database import creer_base, enregistrer_produits
from app.controllers.scraping_controller import lancer_scraping
from app.models.produit import Produit
from app.models.depot import Depot
from app.views.export_view import exporter_csv
from config import DATA_DIR


def main():
    url = "https://www.amazon.com/s?k=bluetooth+headphones"

    donnees = lancer_scraping(url)
    creer_base()
    enregistrer_produits(donnees)

    depot = Depot()

    for donnee in donnees:
        produit = Produit(donnee[0], donnee[1])
        depot.ajouter_produit(produit)

    fichier_csv = DATA_DIR / "data.csv"

    exporter_csv(depot.vers_listes(), fichier_csv)

    print("Nombre de produits trouves :", len(depot.obtenir_produits()))
    print("Fichier CSV cree :", fichier_csv)


if __name__ == "__main__":
    main()
