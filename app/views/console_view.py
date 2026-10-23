
def afficher_message(message):
    print(message)


def afficher_produits(produits):
    if len(produits) == 0:
        print("Aucun produit trouve.")
    else:
        for produit in produits:
            print(produit)
