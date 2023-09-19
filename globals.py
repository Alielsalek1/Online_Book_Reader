from user import User
class UserSet:
    def __init__(self):
        self.users = {}

    def __getitem__(self, key):
        return self.users[key]

    def add_user(self, user):
        self.users[user.username] = user

# global variables and making global class lists for memory and time efficiency
taken_user_names = set()
users = UserSet()
admins = UserSet()
books = []
