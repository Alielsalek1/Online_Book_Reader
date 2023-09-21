import re

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
