from Modules.Category import Category
from Modules.Book import Book
from Modules.Scrap import Scrap
from Modules.CSVCreator import CSVCreator
import configparser
from datetime import datetime
import os

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
    now = datetime.now()
    workingDirectory = "./" + now.strftime("%Y%m%d_%Hh%Mm%S") + "_BookScrap/"
    os.mkdir(workingDirectory) # create a unic working directory
    myScrap = Scrap("scrapping a book site", UrlToScrap)
    allCategories = myScrap.getCategories(workingDirectory)
    # print(allCategories)
    for index, category in enumerate(allCategories) :
        # print(category)
        if index < testlimit : # limit to test
            myCSVCategory = CSVCreator(category.name, workingDirectory)
            myScrap.getBooksFromCategory(category)
            print(category.books)
            for book in category.books :
                bookInfos = myScrap.getBookInfos(book["Book url"], category)
                newBook = Book(bookInfos)
                myCSVCategory.addBookAsLine(newBook)
                myCSVCategory.addBookAsPic(newBook)
            myCSVCategory.close()
        else :
            break

