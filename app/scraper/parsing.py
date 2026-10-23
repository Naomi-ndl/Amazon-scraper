
from selenium.webdriver.common.by import By


def extraire_produits(driver):
    produits = driver.find_elements(
        By.CSS_SELECTOR,
        'div[data-component-type="s-search-result"]'
    )

    liste_produits = []

    for produit in produits:
        noms = produit.find_elements(
            By.CSS_SELECTOR, "h2"
        )

        prix_elements = produit.find_elements(
            By.CSS_SELECTOR, ".a-price .a-offscreen"
        )

        if noms and prix_elements:
            nom = noms[0].text.strip()
            prix = prix_elements[0].get_attribute("textContent").strip()

            if nom and prix:
                liste_produits.append([nom, prix])

    return liste_produits
