import re
from globals import *

# check if the given string is all letters
def is_not_digit(number):
    return not number.isdigit()

# check if a given integer is an integer and in range between 2 numbers
def check_range(minimum_val, maximum_val, number):
    while True:
        if is_not_digit(number) or int(number) < minimum_val or int(number) > maximum_val:
            print(f"Please type a digit from {minimum_val} to {maximum_val} ")
            number = input()
        else:
            return number

# verifying the name to be letters only and spaces allowed between them
def verify_name(name):
    pattern = re.compile(r"^[a-zA-Z\s'-]+$")
    while not pattern.match(name):
        name = input("Please enter your name using english letters only:\n")
    return name

# verifying the username to start with a letter and continue with letters and digits only
def verify_username(username):
    pattern = re.compile(r"^[a-zA-Z][0-9a-zA-z]*$")
    while not pattern.match(username.strip()):
        username = input("Please enter your username with no spaces,"
                         " starting with letters and no special characters:\n")
        if username.strip() in taken_user_names:
            username = input("Please enter another username as this one is taken:\n")
    return username

# verifying the password to not contain whitespaces at all
def verify_password(password):
    pattern = re.compile(r"^.*\s+.*$")
    while pattern.match(password.strip()):
        password = input("Please enter your password without whitespaces:\n")
    return password

def main():
    ...

if __name__ == "__main__":
    main()
