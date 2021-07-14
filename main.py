import requests
from bs4 import BeautifulSoup
from datetime import datetime

UrlToScrap = 'http://books.toscrape.com/'

class Category:
    """
    """
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.books = []

class Book:
    """
    """
    def __init__(self, bookInfos):
        # self.URL = BookDict["url"]
        # self.name = BookDict["title"]
        # self.UPC = BookDict["UPC"]
        # self.price = BookDict["Price (excl. tax)"]
        self.name = bookInfos["title"]
        self.category = bookInfos["category"]
        self.URL = bookInfos["url"]
        self.UPC = bookInfos["UPC"]
        self.price = bookInfos["Price (excl. tax)"]

class Scrap:
    """
    """
    def __init__(self, name, UrlToScrap):
        self.name = name
        self.url = UrlToScrap
        self.books = []
    
    # @staticmethod
    def getCategories(self):
        """
        Fonction qui scrap la page d accueil et qui return un liste des categories avec leurs urls
        """
        allCategories = []
        ## Boucle qui rempli le tableau
        accueil = requests.get(self.url)
        soupAccueil = BeautifulSoup(accueil.text, 'lxml')
        # print(soupAccueil.text)
        listeOfListe = soupAccueil.findAll('li')
        for item in listeOfListe :
            try :
                a = item.find('a')
                # print(a)
                link = a['href']
                if link.find("category") > -1 :
                    name = link.split("/books/")[1].split("/index.html")[0].split("_")[0]
                    url = self.url + link
                    newCategory = Category(name, url)
                    # newCategory = self.getBooksFromCategory(newCategory)
                    allCategories.append(newCategory)
            except :
                print("none")
        # newCategory = Category("Roman", "google.com/roman")
        # newCategory = self.getBooksFromCategory(newCategory) 
        # allCategories.append(newCategory)
        # print(allCategories)
        return allCategories
    
    @staticmethod
    def getBooksFromCategory(Category):
        ## Boucle qui récupère les url des livres de la catégorie
        # print(Category.url)
        url = Category.url
        # ## Récuperation des informations du livre
        categoryPage = requests.get(url)
        storagePath = "catalogue/"
        soupCategory = BeautifulSoup(categoryPage.text, 'lxml')
        soupCategory.find_all("article", {"class": "product_pod"})
        for item in soupCategory.find_all("article", {"class": "product_pod"}):
            for a in item.find_all("a") :
                # print(a['href'], a.get_text())
                BookUrl = UrlToScrap + storagePath + a['href'].split("../")[-1]
                # self.books.append({'Book url' : BookUrl, 'category' : Category["name"]})
            Category.books.append({'Book url' : BookUrl, 'category' : Category.name})
    
    @staticmethod
    def getBookInfos(URL, Category):
        ## Boucle qui récupére les infos du livre sur sa page 
        bookWebPage = requests.get(URL)
        # print(URL)
        soupBook = BeautifulSoup(bookWebPage.text, 'lxml')
        rows = iter(soupBook.find('table').find_all('tr'))
        BookDict = {"url" : URL}
        title=soupBook.findAll('h1')[0].text
        # print(title)
        BookDict["title"] = title
        BookDict["category"] = Category.name
        for row in rows:
            for cell in row.find_all('th'):
                # print(cell.text)
                key = cell.text
            for cell in row.find_all('td'):
                # print(cell.text)
                value = cell.text
            BookDict[key] = value
        return BookDict

class CSVCreator:
    """
    Class qui cree le CSV
    """
    def __init__(self) : 
        """
        creation du fichier vierge
        """
        now = datetime.now()
        prefixe = now.strftime("%Y%m%d_%Hh%Mm%S")
        self.csv = open(prefixe + "_BookScrapInfos.csv", "w+", encoding="utf-8")
        self.csv.write("book.name" + ";" + "book.category" + ";"  + "book.URL" + ";"  + "book.UPC" + ";"  + "book.price" + "\n")
    
    # @staticmethod      
    def addBookAsLine(self, book) :
        ## for book in category.books:
        ## On crée le csv qui s'appelle "category.name"
        ## On insère les informations de chaque livre dans le csv de la catégory
        self.csv.write(book.name + ";" + book.category + ";"  + book.URL + ";"  + book.UPC + ";"  + book.price + "\n")
    
    def close(self) :
        """
        """
        self.csv.close()
    
    # @staticmethod      
    def createCsvFromCategory(self, category):
        ## for book in category.books:
            ## On crée le csv qui s'appelle "category.name"
            ## On insère les informations de chaque livre dans le csv de la catégory
        print('lol')

## Main boucle
myScrap = Scrap("scrapping a book site", UrlToScrap)
allCategories = myScrap.getCategories()
myResults = CSVCreator()
# print(allCategories)
# myScrap.getBooksFromCategory(allCategories[0])
for index, category in enumerate(allCategories) :
    if index < 10000 :
        myScrap.getBooksFromCategory(category)
        print(category.books)
        for book in category.books :
            # print("current book is : " + str(book))
            bookInfos = myScrap.getBookInfos(book["Book url"], category)
            # print("book infos : " + str(bookInfos))
            newBook = Book(bookInfos)
            # print(newBook)
            myResults.addBookAsLine(newBook)
    else :
        break

myResults.close()

        # CSVCreator.createCsvFromCategory(category)