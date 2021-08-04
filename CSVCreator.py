from datetime import datetime
import configparser

# get config info
config = configparser.ConfigParser()
config.read('config.ini')
first_line = config["DEFAULT"]['firstLine'] 

class CSVCreator:
    """
    Class who create the output CSV
    """
    def __init__(self, categoryName) : 
        """
        create an empty file
        """
        now = datetime.now()
        prefixe = now.strftime("%Y%m%d_%Hh%Mm%S") + "_" + categoryName
        self.csv = open(prefixe + "_BookScrapInfos.csv", "w+", encoding="utf-8")
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
    
    def close(self) :
        """
        close nicely the CSV
        """
        self.csv.close()
