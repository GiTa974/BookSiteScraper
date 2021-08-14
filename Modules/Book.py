class Book:
    """
    Class for create a book from the dict generated in Scrap module
    """
    def __init__(self, bookInfos):
        self.URL = bookInfos["url"]
        self.UPC = bookInfos["UPC"]
        self.name = bookInfos["title"]
        self.price_inc_vat = bookInfos["Price (incl. tax)"]
        self.price_no_vat = bookInfos["Price (excl. tax)"]
        if bookInfos["Availability"].find("In stock") > -1 :
            self.available = bookInfos["Availability"].split("(")[1].split(" ")[0]
        else :
            self.available = "0"
        self.description = bookInfos["description"]
        self.category = bookInfos["category"]
        self.rating = bookInfos["rating"]
        self.imgURL = bookInfos["image url"]