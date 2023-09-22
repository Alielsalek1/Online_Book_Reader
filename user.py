from confirmation import *

class User:
    # users either admins or normal users
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
        self._current_books = []

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

    def view_profile(self):
        print(f"\nName: {self.name}")
        print(f"User name: {self.username}\n")

    # take usernames so every username is unique
    @staticmethod
    def take_username(username):
        User.taken_user_names.add(username)

    @staticmethod
    # determine if you want to sign up as an admin or as a normal user
    def admin_or_user():
        print("Menu:")
        print("         1: Admin")
        print("         2: User")
        return int(check_range(1, 2, input("Enter a number in range 1 - 2 ")))

    # check if the username is already taken by another users
    @staticmethod
    def is_available_username(username):
        if username.strip() in User.taken_user_names:
            username = input("Please enter another username as this one is taken:\n")
        return username

    @staticmethod
    # verifying the username to start with a letter and continue with letters and digits only
    def verify_username(username):
        # user maybe right according to regex but taken, so we check before the while loop
        User.is_available_username(username)

        pattern = re.compile(r"^[a-zA-Z][0-9a-zA-z]*$")
        while not pattern.match(username.strip()):
            # check if the
            username = input("Please enter your username with no spaces,"
                             " starting with letters and no special characters:\n")
            User.is_available_username(username)
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

    @staticmethod
    # check if username and password are in the list of admins or users
    def is_valid_user(curr_hash_map):
        name = User.check_username(input("Enter your user name: "), curr_hash_map)
        User.check_password(name, input("Enter your Password: "), curr_hash_map)
        return name

    @staticmethod
    def sign_up(user_type):
        # set values to class user using setter
        name = verify_name(input("Enter your Name: ")).strip()

        # adding a username and appending it to a hash set to prevent username repetition
        username = User.verify_username(input("Enter you Username (no spaces): "))
        User.take_username(username)

        password = verify_password(input("Enter your Password (no spaces): "))

        curr_user = User(name, username, password)

        # if the user is an admin(1) append him to admins else he is a normal user
        if user_type == 1:
            User.admins.add_user(curr_user)
        else:
            User.users.add_user(curr_user)

    @staticmethod
    def view_normal_user_menu():
        print("Menu: ")
        print("         1: View Profile")
        print("         2: Read a new Book")
        print("         3: Continue Reading")
        print("         4: Logout")
        return int(check_range(1, 4, input("Enter a number in range 1 - 4: ")))

def main():
    ...

if __name__ == "__main__":
    main()
