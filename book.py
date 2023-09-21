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

    def __init__(self):
        self._isbn = 0
        self._number_of_pages = 0
        self._title = ""
        self._author_name = ""

def main():
    ...

if __name__ == "__main__":
    main()
