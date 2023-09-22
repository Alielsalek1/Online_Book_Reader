from confirmation import *

class Book:
    class BookSet:
        def __init__(self):
            self.books = {}

        def __getitem__(self, key):
            return self.books[key]

        def add_book(self, book):
            self.books[book.isbn] = book

    # Avoid repetition of books and ISBNS'
    taken_titles = set()
    taken_isbns = set()

    # a hash-map to store books the key is isbn and the value is the book
    books = BookSet()

    def __init__(self, isbn, number_of_pages, title, author_name, book_itself):
        self._isbn = isbn
        self._number_of_pages = number_of_pages
        self._title = title
        self._author_name = author_name
        self._book_itself = book_itself

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, value):
        self._isbn = value

    @property
    def number_of_pages(self):
        return self._number_of_pages

    @number_of_pages.setter
    def number_of_pages(self, value):
        self._number_of_pages = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def author_name(self):
        return self._author_name

    @author_name.setter
    def author_name(self, value):
        self._author_name = value

    @property
    def book_itself(self):
        return self._book_itself

    @book_itself.setter
    def book_itself(self, value):
        self._book_itself = value

    # verify the ISBN is digits only and unique
    @staticmethod
    def verify_isbn(isbn):
        is_available(isbn, Book.taken_isbns)

        while not isbn.isdigit():
            isbn = input("Please Enter a valid ISBN with digits only & no spaces:\n").strip()
            is_available(isbn, Book.taken_isbns)
        return isbn

    # verify that a book title is letters only and unique
    @staticmethod
    def verify_title(title):
        name = verify_name(title)
        while name in Book.taken_titles:
            name = verify_name(title)
            is_available(title, Book.taken_titles)
        return title

    # Input a Book pages
    @staticmethod
    def pages_input(book_itself):
        for page_number in range(len(book_itself)):
            book_itself[page_number] = input(f"Enter Page # {page_number + 1}: ")

    @staticmethod
    def add_book():
        # inputs and adding ISBN & Title to hash-set to be unique
        isbn = Book.verify_isbn(input("Enter ISBN (no spaces): ").strip())
        Book.taken_isbns.add(isbn)
        title = Book.verify_title(input("Enter Title: ").strip())
        Book.taken_titles.add(title)
        author_name = verify_name(input("Enter Author Name: ").strip())
        number_of_pages = verify_num(input("Enter number of pages (no spaces): ").strip())
        book_itself = [""] * int(number_of_pages)
        Book.pages_input(book_itself)

        # constructing the book and adding it to the dictionary of books
        book = Book(isbn, number_of_pages, title, author_name, book_itself)
        Book.books.add_book(book)

def main():
    ...

if __name__ == "__main__":
    main()
