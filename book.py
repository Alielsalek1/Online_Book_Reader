from confirmation import *

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
        is_available(isbn, cls.taken_isbns)

        while not isbn.isdigit():
            isbn = input("Please Enter a valid ISBN with digits only & no spaces:\n").strip()

            # check if the ISBN is unique
            is_available(isbn, cls.taken_isbns)

        return isbn

    @classmethod
    # verify that a book title is letters only and unique
    def verify_title(cls, title):
        # verify title input as letters only as it might be false regex pattern, but it will be unique
        name = verify_name(title)

        # checking that the title letters only and also unique
        while name in cls.taken_titles:
            name = verify_name(title)
            is_available(title, cls.taken_titles)

        return title

    @staticmethod
    # Input a Book pages
    def pages_input(book_itself):
        for page_number in range(len(book_itself)):
            book_itself[page_number] = input(f"Enter Page # {page_number + 1}: ")

    @classmethod
    def add_book(cls):
        # adding ISBN & Title to hash-set to be unique
        isbn = cls.verify_isbn(input("Enter ISBN (no spaces): ").strip())
        cls.taken_isbns.add(isbn)
        title = cls.verify_title(input("Enter Title: ").strip())
        cls.taken_titles.add(title)

        author_name = verify_name(input("Enter Author Name: ").strip())
        number_of_pages = verify_num(input("Enter number of pages (no spaces): ").strip())

        book_itself = [""] * int(number_of_pages)
        cls.pages_input(book_itself)

        # constructing the book and adding it to the dictionary of books
        book = Book(isbn, number_of_pages, title, author_name, book_itself)
        Book.books.add_book(book)

    @staticmethod
    def book_reading_menu():
        print("\nMenu: ")
        print("         1: Next Page")
        print("         2: Previous Page")
        print("         3: Stop Reading")
        return check_range(1, 3, input("Enter a number between 1 & 3: ").strip())

    @staticmethod
    # print the current page data
    def print_book_name_and_page(curr_page, pages_cnt, book_name):
        print(book_name)
        print(f"{curr_page + 1} / {pages_cnt}\n")
        print(f"{Book.books[book_name].book_itself[curr_page]}")

    @classmethod
    # cycling between next and previous pages
    def cycle_pages(cls, user, book_name):
        while True:
            choice = int(Book.book_reading_menu())
            if choice == 1:
                cls.book_next_page(user, book_name)
            elif choice == 2:
                cls.book_prev_page(user, book_name)
            else:
                return

    @staticmethod
    def list_available_new_books(user):
        cnt = 1
        available_books = []

        # iterate on all the books and pick the user didn't start
        for book_title in Book.books.books.keys():

            # check that the book is not in the user history
            if book_title not in user.current_books.keys():
                available_books.append(book_title)
                print(f"{cnt} - {book_title}")
                cnt += 1

        return available_books

    @classmethod
    # read the book
    def read_book(cls, user, book_name):
        pages_cnt = Book.books[book_name].number_of_pages
        curr_page = user.current_books[book_name]

        # print current book number and page
        cls.print_book_name_and_page(curr_page, pages_cnt, book_name)

        # go through the book pages
        cls.cycle_pages(user, book_name)

    @classmethod
    def book_next_page(cls, user, book_name):
        pages_cnt = cls.books[book_name].number_of_pages
        curr_page = user.current_books[book_name]

        # check if you are in the last page, so you can't read further
        if curr_page == int(pages_cnt) - 1:
            return print("No further pages to read!")

        curr_page += 1
        # modify the page to the next one
        user.modify_books(user, book_name, curr_page)

        # print the book page
        cls.print_book_name_and_page(curr_page, pages_cnt, book_name)

    @classmethod
    def book_prev_page(cls, user, book_name):
        pages_cnt = cls.books[book_name].number_of_pages
        curr_page = user.current_books[book_name]

        # check if you are in the first page, so you cannot go back
        if int(curr_page) == 0:
            return print("There is no previous page as this is the first one")

        curr_page -= 1
        # modify the page to the next one
        user.modify_books(user, book_name, curr_page)

        # print the book page
        cls.print_book_name_and_page(curr_page, pages_cnt, book_name)

def main():
    pass

if __name__ == "__main__":
    main()
