from confirmation import *
from user import *
from admin import *

def menu1():
    print("Menu:")
    print("         1: Login")
    print("         2: Sign Up")
    choice = input("Enter a number in range 1 - 2")
    return check_range(1, 2, choice)

def admin_or_user():
    print("Menu")
    print("         1: Admin")
    print("         2: User")
    choice = input("Enter a number in range 1 - 2")
    return check_range(1, 2, choice)

def curr_holder(user_type):
    if user_type == 1:
        return Admin()
    return User()

def sign_up():
    curr_user = curr_holder(admin_or_user())

    name = input("Enter your Name: ")
    ...

    user_name = input("Enter your User name (no spaces): ")
    ...

    email = input("Enter your email: ")
    ...

    password = input("Enter your Password (no spaces): ")
    ...

    ...

def main():
    choice = menu1()






if __name__ == "__main__":
    main()
