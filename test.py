import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/'
categories_urls = []
categories = []

accueil = requests.get(url)
soup = BeautifulSoup(accueil.text, 'lxml')
liste = soup.findAll('li')
print(liste)
print(len(liste))
for item in liste :
    try :
        a = item.find('a')
        link = a['href']
        print(link)
        if link.find("category") > -1 :
            categories_urls.append(link)
    except :
        print("none")
print(categories_urls)
for categories_url in categories_urls :
    print(categories_url)
print(len(categories_urls))

# remove "_"
categories = []
categoriesNum = []
for categories_url in categories_urls :
    try :
        categories.append(categories_url.split("/books/")[1].split("/index.html")[0].split("_")[0])
        categoriesNum.append(categories_url.split("/books/")[1].split("/index.html")[0].split("_")[1])
    except :
        print("not a category")
print(categories)
print(categoriesNum)

# Test get info book
url = 'http://books.toscrape.com/catalogue/code-name-verity-code-name-verity-1_680/'
book001 = requests.get(url)
soupBook001 = BeautifulSoup(book001.text, 'lxml')
soupBook001 = BeautifulSoup(soupBook001.findAll('tr'), 'lxml')
infos = soupBook001.findAll('tr')
UPC = soupBook001.find('th').find_next_sibling()

for info in infos :
    print(str(info) + " fin")


for info in soupBook001.find_all('tr'):
    print(info.get('td'))

rows = iter(soupBook001.find('table').find_all('tr'))
BookDict = {}
title=soupBook001.findAll('h1')[0].text
BookDict[(]"title" : title]
for row in rows:
    for cell in row.find_all('th'):
        print(cell.text)
        key = cell.text
    for cell in row.find_all('td'):
        print(cell.text)
        value = cell.text
    BookDict[key] = value

print(BookDict)

url = "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
url2scrap = 'http://books.toscrape.com/'
storagePath = "catalogue/"
categoryPage = requests.get(url)
soupCategory = BeautifulSoup(categoryPage.text, 'lxml')

soupCategory.find_all("article", {"class": "product_pod"})
for item in soupCategory.find_all("article", {"class": "product_pod"}):
    for a in item.find_all("a") :
        # print(a['href'], a.get_text())
        print(url2scrap + storagePath + a['href'].split("../")[-1])


# pour apeler les proprietes de book
class Book:
    """
    """
    def __init__(self):
        # self.URL = BookDict["url"]
        # self.name = BookDict["title"]
        # self.UPC = BookDict["UPC"]
        # self.price = BookDict["Price (excl. tax)"]
        self.name = "title"
        self.category = "category"
        self.URL = "url"
        self.UPC = "UPC"
        self.price = "Price (excl. tax)"
        print("lol")

book = Book()
for item in dir(book):
    if not item.startswith("__"):
        print(item)

# Pour recuperer toutes les pages de la catégorie
category_url = "https://books.toscrape.com/catalogue/category/books/fiction_10/index.html"
category_root = category_url.split("index.html")[0]
current_category_url = category_url
array_of_category_url = [category_url]
next_exists = True
while next_exists :
    page = requests.get(current_category_url)
    page_text = BeautifulSoup(page.text, 'lxml')
    try : 
        next_page_relative = page_text.find("li", {"class": "next"}).a["href"]
        current_category_url = category_root + next_page_relative
        array_of_category_url.append(current_category_url)
    except :
        next_exists = False


# recup lien image du livre :
url = 'http://books.toscrape.com/catalogue/code-name-verity-code-name-verity-1_680/'
book001 = requests.get(url)
soupBook001 = BeautifulSoup(book001.text, 'lxml') 
img = soupBook001.find_all("div", {"class": "item active"})
image = img[0].find('img')
urlImg = image['src']
# reponse : '../../media/cache/65/9a/659ada7d88e3bda8db70f7e5312a39e2.jpg'
# reality : 'https://books.toscrape.com/media/cache/65/9a/659ada7d88e3bda8db70f7e5312a39e2.jpg'

def getBookInfos(URL, Category):
## Boucle qui récupére les infos du livre sur sa page 
bookWebPage = requests.get(url)
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
description = soupBook.find("div", {"id": "product_description"}).findNext('p').contents[0]
BookDict["description"] = description.replace("\r\n"," ")
return BookDict