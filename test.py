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


