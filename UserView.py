from Book import *

class UserView:
    @staticmethod
    def main_menu():
        print("\nMenu:")
        print("         1: Login")
        print("         2: Sign Up")
        return int(check_range(1, 2, input("Enter a number in range 1 - 2: ")))

    @staticmethod
    # determine if you want to sign up as an admin or as a normal user
    def admin_or_user():
        print("\nMenu:")
        print("         1: Admin")
        print("         2: User")
        return int(check_range(1, 2, input("Enter a number in range 1 - 2 ").strip()))

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
    def book_reading_menu():
        print("\nMenu: ")
        print("         1: Next Page")
        print("         2: Previous Page")
        print("         3: Stop Reading")
        return check_range(1, 3, input("Enter a number between 1 & 3: ").strip())

    @staticmethod
    def print_book_name_and_page(curr_page, pages_cnt, book_name):
        print(book_name)
        print(f"{curr_page + 1} / {pages_cnt}\n")
        print(f"{Book.books[book_name].book_itself[curr_page]}")

def main():
    pass

if __name__ == "__main__":
    main()
