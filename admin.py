from user import *

class Admin:
    @staticmethod
    def view_admin_menu():
        print("Menu: ")
        print("         1: View Profile")
        print("         2: Add a Book")
        print("         3: Logout")
        return int(check_range(1, 3, input("Enter a number in range 1 - 3: ").strip()))

def main():
    ...

if __name__ == "__main__":
    main()
