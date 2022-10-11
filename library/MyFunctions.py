import json
from book import Book

def load_book():
    try:
        file = open("books.dat", "r")
        book_dict = json.loads(file.read())
        books = []
        for book in book_dict:
            book_obj = Book(book['Id'], book['name'], book['description'], book['isbn'], book['page_count'], book['issued'], book['author'], book['year'])
            books.append(book_obj)
        return books
    except:
        return[]

def save_book(books):
    json_book = []
    for book in books:
        json_book.append(Book.to_dict(book))
    try:
        file = open("books.dat","w")
        file.write(json.dumps(json_book, indent= 4))
    except:
        return []

def update_book(book):
    book = Book(book['Id'], book['name'], book['description'], book['isbn'], book['page_count'], book['issued'], book['author'], book['year'])
    books = load_book()
    if book != None:
        books = list(filter(lambda bk:int(bk.Id) != int(book.Id),books))
        books.append(book)
        save_book(books)
def delete_book(id):
    books = load_book()
    books = list(filter(lambda bk:int(id) != int(bk.Id),books))
    save_book(books)
def add_book(book):
    books = load_book()
    new_book = Book(book['Id'], book['name'], book['description'], book['isbn'], book['page_count'], book['issued'], book['author'], book['year'])
    books.append(asign_valid_id(books,new_book))
    save_book(books)

def asign_valid_id(books,new_book):
    book_ids = []
    for book in books:
        book_ids.append(int(book.Id))
    if list(filter(lambda id: id == int(new_book.Id),book_ids)) == [] :
        return new_book
    else:
        new_book.Id = int(max(book_ids) +1)
        return new_book
    
def get_issued_book():
    books = load_book()
    return(list(filter(lambda book:book.issued == True,books)))

def get_unissued_book():
    books = load_book()
    return(list(filter(lambda book:book.issued == False,books)))   

def find_book(book_id):
    books = load_book()
    for book in books:
        if int(book.Id) == int(book_id):
            return book
    return None