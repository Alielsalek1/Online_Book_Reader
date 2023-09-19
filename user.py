class User:
    def __init__(self):
        self._name = ""
        self._username = ""
        self._password = ""
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

def main():
    ...

if __name__ == "__main__":
    main()
