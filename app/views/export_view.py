
import csv


def exporter_csv(produits, chemin_fichier):
    with open(chemin_fichier, "w", newline="", encoding="utf-8-sig") as fichier:
        writer = csv.writer(fichier)

        writer.writerow(["Nom du produit", "Prix"])

        for produit in produits:
            writer.writerow(produit)

    print("Exportation terminee !")
