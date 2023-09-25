from User import *
from UserView import *

def system_run():
    choice = UserView.main_menu()
    if choice == 1:
        User.log_in()
    else:
        User.sign_up(User.admin_or_user())

def main():
    while True:
        system_run()

if __name__ == "__main__":
    main()
