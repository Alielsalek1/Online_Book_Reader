class Book:
    class BookSet:
        def __int__(self):
            self.books = {}

        def __getitem__(self, key):
            return self.books[key]

        def add_user(self, book):
            self.books[book.isbn] = book

    # Avoid repetition of books and ISBNS'
    taken_books = set()
    taken_isbns = set()

    # Store all Books
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



def main():
    ...

if __name__ == "__main__":
    main()
