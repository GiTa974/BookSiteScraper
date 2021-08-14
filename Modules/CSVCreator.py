import configparser
import urllib.request

# get config info
config = configparser.ConfigParser()
config.read('config.ini')
first_line = config["DEFAULT"]['firstLine'] 

class CSVCreator:
    """
    Class who create the output CSV and a folder by category to store book illustration
    """
    def __init__(self, categoryName, subFolderName) : 
        """
        create an empty file
        """
        prefixe = categoryName
        # prefixe = now.strftime("%Y%m%d_%Hh%Mm%S") + "_" + categoryName
        self.csv = open(subFolderName + prefixe + "_BookScrapInfos.csv", "w+", encoding="utf-8")
        self.subFolderName = subFolderName
        # first line if needed in config.ini
        if first_line == "True" :
            self.csv.write("product_page_url" + ";" + "universal_ product_code (upc)" + ";"  + "title" + ";"  + "price_including_tax" + ";"  + "price_excluding_tax" + 
                ";" + "number_available" + ";" + "product_description" + ";" + "category" + ";" + "review_rating" + ";" + "image_url" + "\n")
    
    # @staticmethod      
    def addBookAsLine(self, book) :
        """
        write data from book object
        """
        self.csv.write(book.URL + ";" + book.UPC + ";"  + book.name + ";"  + book.price_inc_vat + ";"  + book.price_no_vat + ";"  + book.available + ";" + book.description + ";" + 
            book.category + ";" + book.rating + ";" + book.imgURL + "\n")
    
    def addBookAsPic(self, book) :
        """
        write pic of the book in the subfolder
        """
        extension = "." + book.imgURL.split(".")[-1]
        picName = book.URL.split("/")[-2] + extension
        # picName = picName.replace("\:", "_").replace("\#", "_").replace("\/", "_").replace("\\", "_").replace("\(", "_").replace("\)", "_").replace("\[", "_").replace("\]", "_").replace("\&", "_")
        urllib.request.urlretrieve(book.imgURL, self.subFolderName + book.category + "/" + picName)
    
    def close(self) :
        """
        close nicely the CSV
        """
        self.csv.close()
