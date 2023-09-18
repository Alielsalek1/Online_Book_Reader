from confirmation import *

def menu1():
    print("Menu:")
    print("         1: Login")
    print("         2: Sign Up")
    choice = input()
    return check_range(1, 2, choice)


def main():
    choice = menu1()






if __name__ == "__main__":
    main()
