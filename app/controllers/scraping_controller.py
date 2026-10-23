
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from app.scraper.driver import creer_driver
from app.scraper.parsing import extraire_produits


def lancer_scraping(url):
    driver, wait = creer_driver()

    try:
        driver.get(url)

        wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, 'div[data-component-type="s-search-result"]')
            )
        )

        produits = extraire_produits(driver)

        return produits

    finally:
        input("Appuie sur Entrée pour fermer Chrome...")
        driver.quit()
