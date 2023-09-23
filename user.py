from book import *

class User:
    class UserSet:
        def __init__(self):
            self.users = {}

        def __getitem__(self, key):
            return self.users[key]

        def add_user(self, user):
            self.users[user.username] = user
    # Avoid repetition of usernames
    taken_user_names = set()

    # a hash-map for users and another for admins
    users = UserSet()
    admins = UserSet()

    def __init__(self, name, username, passowrd):
        self._name = name
        self._username = username
        self._password = passowrd
        self._current_books = {}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def current_books(self):
        return self._current_books

    @staticmethod
    # an updator for Books hashmap
    def modify_books(self, key, value):
        self._current_books[key] = value

    @classmethod
    # take usernames so every username is unique
    def take_username(cls, username):
        cls.taken_user_names.add(username)

    @classmethod
    def normal_user_panel(cls, user):
        while True:
            choice = User.view_normal_user_menu()
            if choice == 1:
                cls.view_profile(user)
            elif choice == 2:
                cls.read_a_new_book(user)
            elif choice == 3:
                cls.continue_reading(user)
            else:
                break

    @classmethod
    def admin_panel(cls, admin):
        while True:
            choice = cls.view_admin_menu()
            if choice == 1:
                admin.view_profile()
            elif choice == 2:
                Book.add_book()
            else:
                break

    @staticmethod
    # determine if you want to sign up as an admin or as a normal user
    def admin_or_user():
        print("\nMenu:")
        print("         1: Admin")
        print("         2: User")
        return int(check_range(1, 2, input("Enter a number in range 1 - 2 ").strip()))

    @staticmethod
    def view_profile(user):
        print(f"\nName: {user.name}")
        print(f"User name: {user.username}")

    @classmethod
    # verifying the username to start with a letter and continue with letters and digits only
    def verify_username(cls, username):
        # user maybe right according to regex but taken, so we check before the while loop
        is_available(username, cls.taken_user_names)

        pattern = re.compile(r"^[a-zA-Z][0-9a-zA-z]*$")
        while not pattern.match(username):
            # the username is doesn't match the pattern
            username = input("Please enter your username with no spaces,"
                             " starting with letters and no special characters:\n").strip()

            # check if username is unique
            is_available(username, cls.taken_user_names)

        return username

    @staticmethod
    # verifying if the entered username is registered for login
    def check_username(username, current_hash_map):
        while current_hash_map.users.get(username) is None:
            username = input("Please Enter an existing username:\n").strip()
        return username

    @staticmethod
    # verifying if the entered password matches the user password
    def check_password(name, passa, current_hash_map):
        while passa != current_hash_map.users[name].password:
            passa = input("Password is incorrect: \n").strip()
        return passa

    @classmethod
    # check if username and password are in the list of admins or users
    def is_valid_user(cls, curr_hash_map):
        name = cls.check_username(input("Enter your user name: ").strip(), curr_hash_map)
        cls.check_password(name, input("Enter your Password: ").strip(), curr_hash_map)
        return name

    @classmethod
    # if the user is an admin(1) append him to admins else he is a normal user
    def add_user(cls, curr_user, user_type):
        if user_type == 1:
            cls.admins.add_user(curr_user)
        else:
            cls.users.add_user(curr_user)

    @classmethod
    def sign_up(cls, user_type):
        name = verify_name(input("Enter your Name: ").strip())

        # adding username to hash-map to be unique
        username = cls.verify_username(input("Enter you Username (no spaces): ").strip())
        cls.take_username(username)

        password = verify_password(input("Enter your Password (no spaces): ").strip())

        # adding the user
        cls.add_user(cls(name, username, password), user_type)

    @classmethod
    def log_in(cls):
        # know if the user signing up is a normal user or an admin
        user_type = cls.admin_or_user()

        # admin log in
        if user_type == 1:
            name = cls.is_valid_user(cls.admins)
            cls.admin_panel(cls.admins[name])

        # normal user log in
        else:
            name = cls.is_valid_user(cls.users)
            cls.normal_user_panel(cls.users[name])

    @staticmethod
    def view_normal_user_menu():
        print("\nMenu: ")
        print("         1: View Profile")
        print("         2: Read a new Book")
        print("         3: Continue Reading")
        print("         4: Logout")
        return int(check_range(1, 4, input("Enter a number in range 1 - 4: ").strip()))

    @staticmethod
    def view_admin_menu():
        print("\nMenu: ")
        print("         1: View Profile")
        print("         2: Add a Book")
        print("         3: Logout")
        return int(check_range(1, 3, input("Enter a number in range 1 - 3: ").strip()))

    @staticmethod
    # check if you read all books or your history is empty
    def cannot_read(user, cmp):
        if len(user.current_books.keys()) == cmp:
            return True
        return False

    @staticmethod
    def choose_and_read_book(available_books, user, new):
        # choose the book that you want to start reading
        choice = verify_num(input("Enter the number of the Book you want to read: ").strip())
        selected_book_name = available_books[int(choice) - int(1)]

        # if you are reading a new book set it to page 1
        if new == 1:
            User.modify_books(user, selected_book_name, 0)

        # start reading your book
        Book.read_book(user, selected_book_name)

    @classmethod
    def read_a_new_book(cls, user):
        # check if user has all books in history and no books to open
        if cls.cannot_read(user, len(Book.books.books.keys())):
            return print("Looks like you have all books opened and can't read a new book")

        # list new books to read
        print("Our current book collection:")
        available_books = Book.list_available_new_books(user)

        # choose and read a book
        cls.choose_and_read_book(available_books, user, int(1))

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
        cls.choose_and_read_book(available_books, user, 0)

def main():
    pass

if __name__ == "__main__":
    main()