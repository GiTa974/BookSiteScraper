# BookSiteScraper

CONTEXTE :
Projet n°2 de la formation 
intitulé : Utilisez les bases de Python pour l'analyse de marché
Ce projet consiste à Scrapper un site de livre dans le cadre de ma formation, le site a été spécialement fourni par le formateur : http://books.toscrape.com/

ARCHITECTURE :
|_|_ BOOK SCRAPPING
   |_ BookScrapper.py
   |_ requirements.txt
   |_ readME.md
   |_ config.ini
   |_|_ Modules
	  |_ Book.py
	  |_ Category.py
	  |_ CSVCreator.py
	  |_ Scrap.py

INSTALLATION :
créer un dossier de travail et positionner l'invite de commande dans ce dossier
créer un environnement virtuel python 3 :
py venv -m ./
activer l'environnement virtuel:
./scripts/activate
Si sous Windows la commande retourne une erreur de type droit, il faut autoriser, ouvrir un invite de commande powershell en administrateur et lancer les commandes suivantes :
Set-ExecutionPolicy Unrestricted -Force
fermer la fenetre powershell en administrateur, et revenir sur la fenetre d'invite de commande dans le dossier
activer l'environnement virtuel qui devrait focntionner maintenant :
./scripts/activate
une fois l'environnement virtuel activer, installer les paquets nécessaires au bon fonctionnement du script :
pip install -r requirements.txt
Les paquets étant correctement installés, lancer le scrapping avec la commande :
py ./BookScrapper.py
Les données devraient se collecter dans un dossier nommé :
YYYY-MM-DD_HH_MM_SS_scrapping etc

FONCTIONNEMENT :
Tout d'abord le script récupére les catégories (nom, url) de livres sur la page d'accueil : http://books.toscrape.com/
Ensuite il passe sur chaque url de catégorie pour récupérer les urls de chaque livres
Pour chaque catégories il créé un CSV et un dossier images
Enfin avec les urls des livres il récupére : 
			* product_page_url
			* universal_ product_code (upc)
			* title
			* price_including_tax
			* price_excluding_tax
			* number_available
			* product_description
			* category
			* review_rating
			* image_url
			* image en jpg
Il pousse ces données dans le csv et l'illustration dans le dossier image de la catégorie.