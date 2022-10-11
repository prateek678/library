import my_functions
import os
books = []
want_exit = False
while not want_exit:
    my_functions.print_options()
    x= input(">")
    if x == 'x':
        want_exit= True
    elif x == '1':
        os.system("cls")
        books.append(my_functions.create_book())
        input('command executed ......press any key to continue')
    elif x == '2':
        my_functions.save_books(books)
        input("books saved locally ...press any key to continue..")
        os.system("cls")
    elif x == '3':
       books = my_functions.load_book()
       os.system("cls")
    elif x== '4':
        my_functions.issue_book(books)
    elif x== '5':
        my_functions.return_book(books)
    elif x== '6':
        my_functions.update_book(books)
    elif x== '7':
        my_functions.show_all_books(books)
    elif x== '8':
        my_functions.show_book(books)
    else:
        input("not valid option ..... press enter to continue...")
    os.system("cls")

