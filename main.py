from user import *

# choose either to login or to sign up
def menu1():
    print("Menu:")
    print("         1: Login")
    print("         2: Sign Up")
    return int(check_range(1, 2, input("Enter a number in range 1 - 2: ")))

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
        name = User.is_valid_user(User.admins)
        admin_panel(User.admins[name])

    # normal user log in
    else:
        name = User.is_valid_user(User.users)
        normal_user_panel(User.users[name])

def sign_up():
    # know if the user signing up is a normal user or an admin
    User.sign_up(admin_or_user())

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
    elif choice == 2:
        ...

def normal_user_menu():
    print("Menu: ")
    print("         1: View Profile")
    print("         2: Read a new Book")
    print("         3: Continue Reading")
    print("         4: Logout")
    return int(check_range(1, 4, input("Enter a number in range 1 - 4: ")))

def normal_user_panel(user):
    choice = normal_user_menu()
    if choice == 1:
        user.view_profile()
    elif choice == 2:
        ...
    elif choice == 3:
        ...

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
