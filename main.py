from user import *

def menu1():
    print("\nMenu:")
    print("         1: Login")
    print("         2: Sign Up")
    return int(check_range(1, 2, input("Enter a number in range 1 - 2: ")))

def system_run():
    choice = menu1()
    if choice == 1:
        User.log_in()
    else:
        User.sign_up(User.admin_or_user())

def main():
    while True:
        system_run()

if __name__ == "__main__":
    main()