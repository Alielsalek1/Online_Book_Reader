from admin import *

# choose either to login or to sign up
def menu1():
    print("Menu:")
    print("         1: Login")
    print("         2: Sign Up")
    return int(check_range(1, 2, input("Enter a number in range 1 - 2: ")))

def log_in():
    # know if the user signing up is a normal user or an admin
    user_type = User.admin_or_user()

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
    User.sign_up(User.admin_or_user())

def admin_menu():
    return Admin.view_admin_menu()

def admin_panel(admin):
    choice = admin_menu()
    if choice == 1:
        admin.view_profile()
    elif choice == 2:
        ...

def normal_user_menu():
    return User.view_normal_user_menu()

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
