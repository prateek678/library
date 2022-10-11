class Book:
    def __init__(self,Id,name,description,isbn,page_count,issued,author,year):
        self.Id = Id
        self.name = name
        self.description = description
        self.isbn = isbn
        self.page_count = page_count
        self.issued = issued
        self.author = author
        self.year = year
    def to_dict(self):
        dictonary = {
            "Id" : self.Id,
            "name" : self.name,
            "description" : self.description,
            "isbn" : self.isbn,
            "page_count" : self.page_count,
            "issued" : self.issued,
            "author" : self.author,
            "year" : self.year
        }
        #print (dictonary)
        return dictonary
        #print(book.to_dict())