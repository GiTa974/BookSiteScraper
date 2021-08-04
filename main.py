from Category import Category
from Book import Book
from Scrap import Scrap
from CSVCreator import CSVCreator
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

UrlToScrap = config["DEFAULT"]['urlToScrap'] # passer dans config file
testlimit = config["DEFAULT"]['limitation'] # passer dans config file
if testlimit == "True" : 
    testlimit = 3
else :
    testlimit = 1000000


## Main boucle
if __name__ == "__main__":
    myScrap = Scrap("scrapping a book site", UrlToScrap)
    allCategories = myScrap.getCategories()
    # print(allCategories)
    # myScrap.getBooksFromCategory(allCategories[0])
    for index, category in enumerate(allCategories) :
        # print(category)
        if index < testlimit : # limit to test
            myCSVCategory = CSVCreator(category.name)
            myScrap.getBooksFromCategory(category)
            print(category.books)
            for book in category.books :
                # print("current book is : " + str(book))
                bookInfos = myScrap.getBookInfos(book["Book url"], category)
                # print("book infos : " + str(bookInfos))
                newBook = Book(bookInfos)
                # print(newBook)
                myCSVCategory.addBookAsLine(newBook)
            myCSVCategory.close()
        else :
            break

