# Projet Python L2 : Amazon Scraper

## 1. Présentation du projet

Ce projet consiste à faire du web scraping sur Amazon avec Python. Le but est de récupérer des informations sur des produits, principalement leur nom et leur prix, puis de sauvegarder les informations dans des fichiers.

Pour réaliser ce projet, j’ai utilisé Selenium pour ouvrir le site Amazon et récupérer les informations des produits affichés.

## 2. Objectif du projet

Les objectifs de ce projet sont :

- Apprendre à faire du web scraping avec Python.
- Utiliser Selenium pour récupérer des informations sur un site web.
- Extraire le nom et le prix des produits.
- Enregistrer les données dans un fichier CSV.
- Utiliser une base de données SQLite pour stocker les produits.
- Organiser le code en plusieurs fichiers pour faciliter sa compréhension.

## 3. Technologies et outils utilisés

- **Python** : langage utilisé pour écrire le programme.
- **Selenium** : bibliothèque utilisée pour ouvrir le navigateur et récupérer les informations sur Amazon.
- **Google Chrome** : navigateur utilisé pour accéder au site.
- **SQLite** : base de données utilisée pour enregistrer les produits.
- **CSV** : format de fichier utilisé pour sauvegarder les données.
- **Visual Studio Code** : éditeur utilisé pour écrire et exécuter le code.
- **Git et GitHub** : outils utilisés pour enregistrer les versions du projet et le partager en ligne.

## 4. Bibliothèques Python utilisées

### Selenium

Selenium permet d'ouvrir le navigateur, d'accéder à une page web et de rechercher les éléments qui contiennent les informations des produits.

Dans le projet, j'utilise notamment :
- `webdriver` pour lancer le navigateur.
- `By` pour rechercher les éléments dans la page.
- `WebDriverWait` pour attendre le chargement des éléments.
- `expected_conditions` pour définir les conditions d'attente.

### SQLite

Le module `sqlite3` permet de créer la base de données, de créer la table des produits et d'enregistrer les informations récupérées.

### CSV

Le module `csv` permet d'écrire les noms et les prix des produits dans le fichier `data.csv`.

### pathlib

Le module `pathlib` permet de gérer les chemins des dossiers et des fichiers du projet dans `config.py`.

### Modules utilisés dans le projet

Le projet utilise aussi les imports Python pour relier les différents fichiers entre eux. Par exemple, `main.py` importe la fonction principale du scraper.

## 5. Fonctionnement du programme

Le programme fonctionne en plusieurs étapes :

1. Le programme ouvre Amazon avec Selenium.
2. Il attend que les résultats de recherche soient présents sur la page.
3. Il récupère le nom et le prix des produits.
4. Les données récupérées sont transmises au reste du programme.
5. Les produits sont organisés avec les classes `Produit` et `Depot`.
6. Les informations sont enregistrées dans le fichier CSV.
7. Les informations sont également enregistrées dans la base de données SQLite.

## 6. Organisation des fichiers

```text
amazon_scraper/
├── app/
│   ├── controllers/
│   │   └── scraping_controller.py
│   ├── models/
│   │   ├── produit.py
│   │   └── depot.py
│   ├── scraper/
│   │   ├── amazon_scraper.py
│   │   ├── driver.py
│   │   └── parsing.py
│   ├── views/
│   │   ├── console_view.py
│   │   └── export_view.py
│   └── database.py
├── data/
│   ├── data.csv
│   └── amazon.db
├── config.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 7. Rôle des principaux fichiers

- `main.py` : permet de lancer le programme.
- `config.py` : définit les chemins des dossiers utilisés.
- `driver.py` : crée le navigateur Chrome et l'attente Selenium.
- `parsing.py` : récupère le nom et le prix des produits sur la page.
- `scraping_controller.py` : lance le scraping et gère le navigateur.
- `amazon_scraper.py` : organise les étapes principales du programme.
- `produit.py` : contient la classe `Produit`.
- `depot.py` : contient la classe `Depot` qui permet de regrouper les produits.
- `export_view.py` : permet d'exporter les données dans le fichier CSV.
- `database.py` : permet de créer la base SQLite et d'enregistrer les produits.
- `data.csv` : contient les produits exportés.
- `amazon.db` : contient la base de données SQLite.
- `requirements.txt` : contient la liste des bibliothèques nécessaires.
- `.gitignore` : indique les fichiers et dossiers que Git ne doit pas envoyer, comme l'environnement virtuel et les fichiers Python temporaires.

## 8. Installation du projet

Il faut avoir Python, Google Chrome et Visual Studio Code installés.

Ouvrir le terminal dans le dossier du projet, puis installer les dépendances avec la commande :

```bash
pip install -r requirements.txt
```

## 9. Exécution du programme

Pour lancer le scraper, exécuter la commande suivante dans le terminal :

```bash
python main.py
```

Le programme ouvre Chrome, accède à Amazon, récupère les informations des produits et les enregistre dans les fichiers prévus.

Si le programme demande d'appuyer sur Entrée avant de fermer Chrome, il faut revenir au terminal et appuyer sur Entrée.

## 10. Stockage des données

Les données sont sauvegardées dans le dossier `data`.

- `data.csv` contient le nom et le prix des produits. Il peut être ouvert avec Excel ou un autre tableur.
- `amazon.db` est une base de données SQLite. Elle peut être consultée avec une extension comme SQLite Viewer dans Visual Studio Code.

## 11. Difficultés rencontrées

Pendant le développement, j'ai rencontré des difficultés pour récupérer les produits avec les sélecteurs Selenium. Au début, le programme ne récupérait pas correctement les noms et les prix. J'ai donc ajusté les sélecteurs utilisés pour rechercher les éléments sur la page.

J'ai aussi appris à organiser le code dans plusieurs fichiers et à enregistrer les données dans une base de données SQLite.

## 12. Conclusion

Ce projet m'a permis de pratiquer Python et de découvrir le web scraping avec Selenium. J'ai aussi appris à sauvegarder les données dans un fichier CSV et dans une base de données SQLite. Enfin, j'ai utilisé Git et GitHub pour suivre les modifications du projet et partager le code.


