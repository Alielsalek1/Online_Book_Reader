from confirmation import *
from user import *
from admin import *
from globals import *

# choose either to login or to sign up
def menu1():
    print("Menu:")
    print("         1: Login")
    print("         2: Sign Up")
    choice = input("Enter a number in range 1 - 2 ")
    return check_range(1, 2, choice)

# determine if you want to sign up as an admin or as a normal user
def admin_or_user():
    print("Menu")
    print("         1: Admin")
    print("         2: User")
    choice = input("Enter a number in range 1 - 2 ")
    return check_range(1, 2, choice)

def log_in():
    ...

def sign_up():
    # know if the user signing up is a normal user or an admin
    user_type = admin_or_user()
    curr_user = User()

    # set values to class user using setter
    curr_user.name = verify_name(input("Enter your Name: ")).strip()

    # adding a username and appending it to a hash set to prevent username repetition
    curr_user.username = verify_username(input("Enter you Username (no spaces): "))
    taken_user_names.add(curr_user.username)

    curr_user.password = verify_password(input("Enter your Password (no spaces): "))

    # if the user is an admin(1) append him to admins else he is a normal user
    if user_type == 1:
        admins.append(curr_user)
    else:
        users.append(curr_user)

def main():
    choice = menu1()
    if choice == 1:
        log_in()
    else:
        sign_up()

if __name__ == "__main__":
    main()
