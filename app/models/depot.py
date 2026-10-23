
class Depot:
    def __init__(self):
        self.produits = []

    def ajouter_produit(self, produit):
        self.produits.append(produit)

    def afficher_produits(self):
        for produit in self.produits:
            produit.afficher()

    def obtenir_produits(self):
        return self.produits

    def vers_listes(self):
        listes = []

        for produit in self.produits:
            listes.append(produit.vers_liste())

        return listes
