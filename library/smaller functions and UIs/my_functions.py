from book import Book
import json
def print_options():
    print("     options ")
    print("---------------")
    print("1- create new book")
    print("2-save books locally")
    print("3-load books from the disk")
    print("4-issue book")
    print("5-return a book")
    print("6-update a book")
    print("7-show all books")
    print("8-show book")
def input_book_info():
    Id = input("id= ")
    name = input("name= ")
    description = input("description= ")
    isbn = input("isbn= ")
    page_count = input("page_count= ")
    issued = input("issued(y for yes and any thing else for no)= ")
    if (issued.lower() == 'y'):
        issued = True
    else:
        issued= False
    author = input("author= ")
    year = input("year= ")
    return{
        "Id" : Id,
        "name" : name,
        "description" : description,
        "isbn" : isbn,
        "page_count" : page_count,
        "issued" : issued,
        "author" : author,
        "year" : year

    }

def create_book():
    print("input the book details: ")
    book_input = input_book_info()
    book = Book(book_input['Id'], book_input['name'], book_input['description'], book_input['isbn'], book_input['page_count'], book_input['issued'], book_input['author'], book_input['year'])
    book.to_dict()
    return book

def save_books(books):
    json_books = []
    for book in books:
        json_books.append(book.to_dict())
        try:
            file = open("books.txt", "w")
            file.write(json.dumps(json_books, indent=4))
        except:
            print("we had an error saving the book")
def load_book():
    try:
        file = open("books.txt", "r")
        loaded_books = json.loads(file.read())
        books = []
        for book in loaded_books:
            new_obj = Book(book['Id'], book['name'], book['description'], book['isbn'], book['page_count'], book['issued'], book['author'], book['year']) 
            books.append(new_obj)
        input("books loaded successfully...press enter to continue...")
        return books
    except:
        print("the file doesnot exist or an error occured during saving ")

def find_book(books,id):
    for index, book in enumerate(books):
        if id == book.Id:
            return index
    return None

def issue_book(books):
    Id = input("enter the id of the book: ")
    index = find_book(books,Id)
    if index != None:
        books[index].issued = True
        input("book issued....press enter to continue..")
        return books
    else:
        print("no book with the given id!")
        return books

def return_book(books):
    Id = input("enter the id of the book: ")
    index = find_book(books,Id)
    if index != None:
        books[index].issued = False
        input("book returned....press enter to continue...")
        return books
    else:
        print("no book with the given id!")
        return books

def update_book(books):
    Id = input("enter the id of the book you wanna update: ")
    index = find_book(books,Id)
    if index != None:
        new_book = create_book()
        old_book = books[index]
        books[index] = new_book
        del old_book
        input("book updated successfully....press enter to continue..")
    else:
        input("sorry, can't find the book with the given id...press enter to continue")

def show_all_books(books):
    for book in books:
        print(book.to_dict())
    input("press inter to continue...")

def show_book(books):
    Id = input("enter the id of the book: ")
    index = find_book(books,Id)
    print(books[index].to_dict())
    input("press enter to continue...")
