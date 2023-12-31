from ReadingSession import *
from UserView import *

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

    def normal_user_panel(self):
        while True:
            choice = UserView.view_normal_user_menu()
            if choice == 1:
                self.view_profile()
            elif choice == 2:
                ReadingSession.read_a_new_book(self)
            elif choice == 3:
                ReadingSession.continue_reading(self)
            else:
                break

    def admin_panel(self):
        while True:
            choice = UserView.view_admin_menu()
            if choice == 1:
                self.view_profile()
            elif choice == 2:
                Book.add_book()
            else:
                break

    def view_profile(self):
        print(f"\nName: {self.name}")
        print(f"User name: {self.username}")

    @classmethod
    # verifying the username to start with a letter and continue with letters and digits only
    def verify_username(cls, username):
        # user maybe right according to regex but taken, so we check before the while loop
        username = is_available(username, cls.taken_user_names)
        if pressed_zero(username):
            return str(0)
        pattern = re.compile(r"^[a-zA-Z][0-9a-zA-z]*$")
        while not pattern.match(username):
            # the username doesn't match the pattern
            username = input("Please enter your username with no spaces,"
                             " starting with letters and no special characters: or 0 to cancel\n").strip()
            # check if the username is unique
            username = is_available(username, cls.taken_user_names)
            if pressed_zero(username):
                return str(0)
        return username

    @staticmethod
    # verifying if the entered username is registered for login
    def check_username(username, current_hash_map):
        if pressed_zero(username):
            return str(0)
        while current_hash_map.users.get(username) is None:
            username = input("Please Enter an existing username or 0 to cancel:\n").strip()
            if pressed_zero(username):
                return str(0)
        return username

    @staticmethod
    # verifying if the entered password matches the user password
    def check_password(name, password, current_hash_map):
        if pressed_zero(password):
            return str(0)
        while password != current_hash_map.users[name].password:
            password = input("Password is incorrect or 0 to cancel: \n").strip()
            if pressed_zero(password):
                return str(0)
        return password

    @classmethod
    # check if username and password are in the list of admins or users
    def is_valid_user(cls, curr_hash_map):
        name = cls.check_username(input("Enter your username or 0 to cancel: ").strip(), curr_hash_map)
        if pressed_zero(name):
            return str(0)
        password = cls.check_password(name, input("Enter your Password or 0 to cancel: ").strip(), curr_hash_map)
        if pressed_zero(password):
            return str(0)
        return name

    # if the user is an admin(1) append him to admins else he is a normal user
    def add_user(self, user_type):
        if user_type == 1:
            self.admins.add_user(self)
        else:
            self.users.add_user(self)

    @classmethod
    def sign_up(cls, user_type):
        if user_type == int(3):
            return
        name = verify_name(input("Enter your Name or 0 to cancel: ").strip())
        if pressed_zero(name):
            return
        username = cls.verify_username(input("Enter you Username (no spaces) or 0 to cancel: ").strip())
        if pressed_zero(username):
            return
        password = verify_password(input("Enter your Password (no spaces) or 0 to cancel: ").strip())
        if pressed_zero(password):
            return
        # adding username to hash-map to be unique
        cls.take_username(username)
        # adding the user
        cls.add_user(cls(name, username, password), user_type)

    @classmethod
    def log_in(cls):
        # know if the user signing up is a normal user or an admin
        user_type = UserView.admin_or_user()

        # admin log in
        if user_type == int(1):
            name = cls.is_valid_user(cls.admins)
            if pressed_zero(name):
                return
            cls.admin_panel(cls.admins[name])

        # normal user log in
        elif user_type == int(2):
            name = cls.is_valid_user(cls.users)
            if pressed_zero(name):
                return
            cls.normal_user_panel(cls.users[name])
        else:
            return

    def list_available_new_books(self):
        cnt = 1
        available_books = []

        # iterate on all the books and pick the user didn't start
        for book_title in Book.books.books.keys():

            # check that the book is not in the user history
            if book_title not in self.current_books.keys():
                available_books.append(book_title)
                print(f"{cnt} - {book_title}")
                cnt += 1

        return available_books

def main():
    pass

if __name__ == "__main__":
    main()