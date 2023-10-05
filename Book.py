from confirmations import *

class Book:
    class BookSet:
        def __init__(self):
            self.books = {}

        def __getitem__(self, key):
            return self.books[key]

        def add_book(self, book):
            self.books[book.title] = book
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

    @classmethod
    # verify the ISBN is digits only and unique
    def verify_isbn(cls, isbn):
        # ISBN might be digits(True) but not unique, so we confirm before looping
        isbn = is_available(isbn, cls.taken_isbns)
        if pressed_zero(isbn):
            return str(0)
        while not isbn.isdigit():
            isbn = input("Please Enter a valid ISBN with digits only & no spaces or 0 to cancel:\n").strip()

            # check if the ISBN is unique
            isbn = is_available(isbn, cls.taken_isbns)
            if pressed_zero(isbn):
                return str(0)

        return isbn

    @classmethod
    # verify that a book title is letters only and unique
    def verify_title(cls, title):
        if pressed_zero(title):
            return str(0)

        # verify title input as letters only as it might be false regex pattern, but it will be unique
        title = verify_name(title)
        if pressed_zero(title):
            return str(0)

        # checking that the title letters only and also unique
        while title in cls.taken_titles:
            title = verify_name(title)
            title = is_available(title, cls.taken_titles)
            if pressed_zero(title):
                return str(0)
        return title

    @staticmethod
    # Input a Book pages
    def pages_input(book_itself):
        for page_number in range(len(book_itself)):
            book_itself[page_number] = input(f"Enter Page # {page_number + 1}: ")

    @classmethod
    def add_book(cls):
        # adding ISBN & Title to hash-set to be unique
        isbn = cls.verify_isbn(input("Enter ISBN (no spaces) or 0 to cancel: ").strip())
        if pressed_zero(isbn):
            return

        title = cls.verify_title(input("Enter Title or 0 to cancel: ").strip())
        if pressed_zero(title):
            return

        author_name = verify_name(input("Enter Author Name or 0 to cancel: ").strip())
        if pressed_zero(author_name):
            return
        number_of_pages = verify_num(input("Enter number of pages (no spaces) or 0 to cancel: ").strip())
        if pressed_zero(number_of_pages):
            return

        book_itself = [""] * int(number_of_pages)
        cls.pages_input(book_itself)

        # make the ISBN & title unique
        cls.taken_titles.add(title)
        cls.taken_isbns.add(isbn)
        # constructing the book and adding it to the dictionary of books
        book = Book(isbn, number_of_pages, title, author_name, book_itself)
        Book.books.add_book(book)

def main():
    pass

if __name__ == "__main__":
    main()