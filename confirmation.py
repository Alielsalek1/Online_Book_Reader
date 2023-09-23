import re

# verifying the input is all numbers and no whitespace between them
def verify_num(number):
    while not number.isdigit():
        number = input("Please Enter a valid digit with no spaces in between:\n").strip()
    return number

# check if a given integer is an integer and in range between 2 numbers
def check_range(minimum_val, maximum_val, number):
    while True:
        # check if it is even a digit and in range both numbers
        if (not number.isdigit()) or int(number) < minimum_val or int(number) > maximum_val:
            print(f"Please type a digit from {minimum_val} to {maximum_val} ")
            number = input().strip()
        else:
            return number

# verifying the name to be letters only and spaces allowed between them
def verify_name(name):
    pattern = re.compile(r"^[a-zA-Z\s'-]+$")
    while not pattern.match(name):
        name = input("Please enter the name using english letters only:\n").strip()
    return name

# verifying the password to not contain whitespaces at all
def verify_password(password):
    pattern = re.compile(r"^.*\s+.*$")
    while pattern.match(password.strip()):
        password = input("Please enter your password without whitespaces:\n").strip()
    return password

# check availability of an item in its hash-set
def is_available(value, taken):
    while value in taken:
        value = input("Please Enter another as this one is taken:\n").strip()

def main():
    pass

if __name__ == "__main__":
    main()