
class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

    def afficher(self):
        print("Nom :", self.nom)
        print("Prix :", self.prix)

    def vers_liste(self):
        return [self.nom, self.prix]
