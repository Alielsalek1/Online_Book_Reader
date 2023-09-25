from UserView import *

class ReadingSession:
    @staticmethod
    # check if you read all books or your history is empty
    def cannot_read(user, cmp):
        if len(user.current_books.keys()) == cmp:
            return True
        return False

    @classmethod
    def choose_and_read_book(cls, user, available_books, new):
        # choose the book that you want to start reading
        choice = verify_num(input("Enter the number of the Book you want to read: ").strip())
        selected_book_name = available_books[int(choice) - int(1)]

        # if you are reading a new book set it to page 1
        if new == 1:
            user.modify_books(user, selected_book_name, 0)

        # start reading your book
        cls.read_book(user, selected_book_name)

    @classmethod
    def read_a_new_book(cls, user):
        # check if user has all books in history and no books to open
        if cls.cannot_read(user, len(Book.books.books.keys())):
            return print("Looks like you have all books opened and can't read a new book")

        # list new books to read
        print("Our current book collection:")
        available_books = user.list_available_new_books()

        # choose and read a book
        cls.choose_and_read_book(user, available_books, int(1))

    @classmethod
    # cycling between next and previous pages
    def cycle_pages(cls, user, book_name):
        while True:
            choice = int(UserView.book_reading_menu())
            if choice == 1:
                cls.book_next_page(user, book_name)
            elif choice == 2:
                cls.book_prev_page(user, book_name)
            else:
                return

    @classmethod
    def continue_reading(cls, user):
        # check if user doesn't have a book to continue
        if cls.cannot_read(user, 0):
            return print("no books to continue reading")

        # making a list of book titles (keys)
        available_books = list(user.current_books.keys())

        # list books to complete reading
        print("Books to continue reading: ")
        for book_num in range(len(available_books)):
            print(f"{book_num + 1} - {available_books[book_num]}")

        # choose and read a book
        cls.choose_and_read_book(user, available_books, int(0))

    @staticmethod
    def book_prev_page(user, book_name):
        pages_cnt = Book.books[book_name].number_of_pages
        curr_page = user.current_books[book_name]

        # check if you are in the first page, so you cannot go back
        if int(curr_page) == 0:
            return print("There is no previous page as this is the first one")

        curr_page -= 1
        # modify the page to the next one
        user.modify_books(user, book_name, curr_page)

        # print the book page
        UserView.print_book_name_and_page(curr_page, pages_cnt, book_name)

    @staticmethod
    def book_next_page(user, book_name):
        pages_cnt = Book.books[book_name].number_of_pages
        curr_page = user.current_books[book_name]

        # check if you are in the last page, so you can't read further
        if curr_page == int(pages_cnt) - 1:
            return print("No further pages to read!")

        curr_page += 1
        # modify the page to the next one
        user.modify_books(user, book_name, curr_page)

        # print the book page
        UserView.print_book_name_and_page(curr_page, pages_cnt, book_name)

    @classmethod
    # read the book
    def read_book(cls, user, book_name):
        pages_cnt = Book.books[book_name].number_of_pages
        curr_page = user.current_books[book_name]

        # print current book number and page
        UserView.print_book_name_and_page(curr_page, pages_cnt, book_name)

        # go through the book pages
        cls.cycle_pages(user, book_name)

def main():
    pass

if __name__ == "__main__":
    main()
