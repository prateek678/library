from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from main_window import Ui_MainWindow
from add_book_dialog import Ui_add_book_dialog as Ui_AddBook
from edit_dialog import Ui_edit_dialog
from delete_dialog import Ui_delete_dialog
from search_no_id import Ui_Dialog as Ui_search
from stylesheets import main_style_sheet
import MyFunctions as lib

class DeleteBook(QDialog,Ui_delete_dialog):
    def __init__(self,parent=None):
        super(DeleteBook,self).__init__(parent)
        self.ui = Ui_delete_dialog()
        self.ui.setupUi(self)
class SearchBook(QDialog,Ui_search):
    def __init__(self,parent=None):
        super(SearchBook,self).__init__(parent)
        self.ui = Ui_search()
        self.ui.setupUi(self)
class AddBook(QDialog,Ui_AddBook):
    def __init__(self,parent=None):
        super(AddBook,self).__init__(parent)
        self.ui = Ui_AddBook()
        self.ui.setupUi(self)
class EditBook(QDialog,Ui_edit_dialog):
    def __init__(self,parent=None):
        super(EditBook,self).__init__(parent)
        self.ui = Ui_edit_dialog()
        self.ui.setupUi(self)

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        lib.get_issued_book()
        self.new_book_btn.clicked.connect(self.show_add_book)
        self.load_issued_book()
        self.load_unissued_book()
        self.load_all_book()
        self.issued_edit_btn.clicked.connect(lambda : self.edit_book(self.issued_table))
        self.unissued_edit_btn.clicked.connect(lambda : self.edit_book(self.unissued_table))
        self.issued_delete_btn.clicked.connect(lambda :self.delete_book(self.issued_table))
        self.unissued_delete_btn.clicked.connect(lambda :self.delete_book(self.unissued_table))
        self.search_btn.clicked.connect(lambda: self.search_book(int(self.search_inout.text())))
        self.issued_refresh_btn.clicked.connect(lambda : self.load_issued_book())
        self.unissued_refresh_btn.clicked.connect(lambda : self.load_unissued_book())
        self.all_book_refresh_btn.clicked.connect(lambda : self.load_all_book())
        self.setStyleSheet(main_style_sheet)
        
    def save_existing_book(self,ui):
        book = {
            "Id" : int(ui.id_input.text()),
            "name" : ui.name_input.text(),
            "description" :ui.description_input.text(),
            "isbn" :ui.isbn_input.text(),
            "page_count" :int(ui.page_count_input.text()),
            "issued" :ui.yes.isChecked(),
            "author" :ui.author_input.text(),
            "year" :int(ui.year_input.text())
        }
        lib.update_book(book)
    def edit_book(self,table):
        selected_row = table.currentRow()
        if selected_row != -1:
            book_id = int(table.item(selected_row,0).text())
            book = lib.find_book(book_id)
            edit_dlg = EditBook(self)
            edit_dlg.ui.id_input.setValue(int(book.Id))
            edit_dlg.ui.name_input.setText(book.name)
            edit_dlg.ui.description_input.setText(book.description)
            edit_dlg.ui.isbn_input.setText(book.isbn)
            edit_dlg.ui.page_count_input.setValue(int(book.page_count))
            if book.issued:
                edit_dlg.ui.yes.setChecked(book.issued)
            else:
                edit_dlg.ui.no.setChecked(not(book.issued))
            edit_dlg.ui.author_input.setText(book.author)
            edit_dlg.ui.year_input.setValue(int(book.year))
            edit_dlg.ui.buttonBox.accepted.connect(
                lambda: self.save_existing_book(edit_dlg.ui))
            edit_dlg.exec()
            self.load_issued_book()
            self.load_unissued_book()
            self.load_all_book()
    def save_new_book(self,ui):
        new_book = {
            "Id" : int(ui.id_input.text()),
            "name" : ui.name_input.text(),
            "description" : ui.description_input.text(),
            "isbn" : ui.isbn_input.text(),
            "page_count" : int(ui.page_count_input.text()),
            "issued" : ui.yes.isChecked(),
            "author" : ui.author_input.text(),
            "year" : int(ui.year_input.text())
        }
        for attr in new_book:
           if new_book[attr] == None or str(new_book[attr]) == "":
               return False
        lib.add_book(new_book)
    def load_issued_book(self):
        books = lib.get_issued_book()
        self.issued_table.setRowCount(len(books))
        for index, book in enumerate(books):
            book = book.to_dict()
            for book_index,attr in enumerate(book):
                self.issued_table.setItem(index,book_index,QTableWidgetItem(str(book[str(attr)])))
                self.issued_table.item(index,book_index).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
    def load_unissued_book(self):
        books = lib.get_unissued_book()
        self.unissued_table.setRowCount(len(books))
        for index, book in enumerate(books):
            book = book.to_dict()
            for book_index,attr in enumerate(book):
                self.unissued_table.setItem(index,book_index,QTableWidgetItem(str(book[str(attr)])))
                self.unissued_table.item(index,book_index).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
    def load_all_book(self):
        books = lib.load_book()
        self.all_books_table.setRowCount(len(books))
        for index, book in enumerate(books):
            book = book.to_dict()
            for book_index,attr in enumerate(book):
                self.all_books_table.setItem(index,book_index,QTableWidgetItem(str(book[str(attr)])))
                self.all_books_table.item(index,book_index).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
    def show_add_book(self):
        input_dlg = AddBook(self)
        input_dlg.ui.buttonBox.accepted.connect(
            lambda: self.save_new_book(input_dlg.ui)
        )
        input_dlg.exec()
        self.load_issued_book()
        self.load_unissued_book()
        self.load_all_book()
    def delete_book(self,table):
        selected_row = table.currentRow()
        if selected_row != -1:
            book_id = int(table.item(selected_row,0).text())
            delete_dlg = DeleteBook(self)        
            delete_dlg.ui.buttonBox.accepted.connect(
                lambda:lib.delete_book(book_id))
            delete_dlg.exec()
            self.load_issued_book()
            self.load_unissued_book()
            self.load_all_book()
    def search_book(self,book_id):
        book = lib.find_book(book_id)
        if book != None:
            self.search_table.setRowCount(1)
            book = book.to_dict()
            for index,attr in enumerate(book):
                self.search_table.setItem(0,index,QTableWidgetItem(str(book[str(attr)])))
                self.search_table.item(0,index).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        else:
            self.search_no_id()
            #self.search_table.setRowCount(1)
            #self.search_table.setItem(0,0,QTableWidgetItem(str("ID doesnot exist")))
    def search_no_id(self):
        search_dlg = SearchBook(self)
        search_dlg.exec()
        
app = QApplication([])
window = MainWindow()
window.show()
app.exec()

