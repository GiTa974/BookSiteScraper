import requests
from bs4 import BeautifulSoup
from Modules.Category import Category
import configparser
import os


config = configparser.ConfigParser()
config.read('config.ini')

UrlToScrap = config["DEFAULT"]['urlToScrap'] 

class Scrap:
    """
    Scrap objects like Books and Categories
    """
    def __init__(self, name, UrlToScrap):
        self.name = name
        self.url = UrlToScrap
        self.books = []
    
    # @staticmethod
    def getCategories(self, subFolder):
        """
        Get categories from home page
        """
        allCategories = []
        ## Boucle qui rempli le tableau
        homePage = requests.get(self.url)
        soupHomePage = BeautifulSoup(homePage.text, 'lxml')
        # print(soupAccueil.text)
        listeOfListe = soupHomePage.findAll('li')
        for item in listeOfListe :
            try :
                a = item.find('a')
                print(a)
                link = a['href']
                print(link)
                if link.find("category") > -1 :
                    print("debut if")
                    name = link.split("/books/")[1].split("/index.html")[0].split("_")[0]
                    print('name ok')
                    url = self.url + link
                    print('debut new cat')
                    newCategory = Category(name, url)
                    # newCategory = self.getBooksFromCategory(newCategory)
                    allCategories.append(newCategory)
                    os.mkdir(subFolder + newCategory.name) # Create a folder to store book's picture
            except :
                print("none")
        print(len(allCategories))
        return allCategories
    
    @staticmethod
    def getBooksFromCategory(Category):
        """
        Loop get books in the category
        """
        current_url = Category.url
        next_exists = True
        storagePath = "catalogue/"
        # ## Récuperation des url des livres dans la category
        while next_exists :
            categoryPage = requests.get(current_url)
            soupCategory = BeautifulSoup(categoryPage.text, 'lxml')
            for item in soupCategory.find_all("article", {"class": "product_pod"}):
                for a in item.find_all("a") :
                    # print(a['href'], a.get_text())
                    BookUrl = UrlToScrap + storagePath + a['href'].split("../")[-1]
                    # self.books.append({'Book url' : BookUrl, 'category' : Category["name"]})
                Category.books.append({'Book url' : BookUrl, 'category' : Category.name})
                try : 
                    next_page_relative = page_text.find("li", {"class": "next"}).a["href"]
                    current_url = category_root + next_page_relative
                except :
                    next_exists = False
    
    @staticmethod
    def getBookInfos(URL, Category):
        """
        get needed infos of a book from its url
        """
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

        # get book image url
        img = soupBook.find_all("div", {"class": "item active"})
        image = img[0].find('img')
        urlImg = image['src']
        BookDict["image url"] = UrlToScrap + urlImg.split('../../')[1]
        # get description the paragraph after the div with id product_description
        try :
            description = soupBook.find("div", {"id": "product_description"}).findNext('p').contents[0]
        except :
            description = "none"
        if len(description) > 100 :
            BookDict["description"] = description[:100].replace("\r\n"," ").replace(";",",").replace("\""," ").replace("\'"," ")
        else :
            BookDict["description"] = description.replace("\r\n"," ").replace(";",",").replace("\""," ").replace("\'"," ")
        # get rating
        try :
            if len(soupBook.find("p", {"class": "star-rating One"}).parent.find("h1")) > 0 :
                rating = "1"
        except :
            try :
                if len(soupBook.find("p", {"class": "star-rating Two"}).parent.find("h1")) > 0 :
                    rating = "2"
            except :
                try :
                    if len(soupBook.find("p", {"class": "star-rating Three"}).parent.find("h1")) > 0 :
                        rating = "3"
                except :
                    try :
                        if len(soupBook.find("p", {"class": "star-rating Four"}).parent.find("h1")) > 0 :
                            rating = "4"
                    except :
                        try :
                            if len(soupBook.find("p", {"class": "star-rating Five"}).parent.find("h1")) > 0 :
                                rating = "5"
                        except :
                            rating = "none"
        BookDict["rating"] = rating
        return BookDict