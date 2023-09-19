from confirmation import *
from admin import *
from globals import *

# choose either to login or to sign up
def menu1():
    print("Menu:")
    print("         1: Login")
    print("         2: Sign Up")
    return int(check_range(1, 2, input("Enter a number in range 1 - 2 ")))

# determine if you want to sign up as an admin or as a normal user
def admin_or_user():
    print("Menu:")
    print("         1: Admin")
    print("         2: User")
    return int(check_range(1, 2, input("Enter a number in range 1 - 2 ")))

def log_in():
    # know if the user signing up is a normal user or an admin
    user_type = admin_or_user()

    # admin log in
    if user_type == 1:
        name = check_username(input("Enter your user name: "), admins)
        check_password(name, input("Enter your Password: "), admins)
        admin_panel(admins[name])

    # normal user log in
    else:
        name = check_username(input("Enter your user name: "), users)
        check_password(name, input("Enter your Password: "), users)

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
        admins.add_user(curr_user)
    else:
        users.add_user(curr_user)

def admin_menu():
    print("Menu: ")
    print("         1: View Profile")
    print("         2: Add a Book")
    print("         3: Logout")
    return int(check_range(1, 3, input("Enter a number in range 1 - 3: ")))

def admin_panel(admin):
    choice = admin_menu()
    if choice == 1:
        admin.view_profile()
    elif choice == 3:
        ...
    else:
        main()

def system_run():
    choice = menu1()
    if choice == 1:
        log_in()
    else:
        sign_up()

def main():
    while True:
        system_run()

if __name__ == "__main__":
    main()
