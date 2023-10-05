import re

def pressed_zero(choice):
    return choice == str(0)

# check availability of an item in its hash-set
def is_available(value, taken):
    while value in taken or not value:
        value = input("Please Enter another valid one as this one is taken or 0 to cancel:\n").strip()
    return value

# verifying the input is all numbers and no whitespace between them
def verify_num(number):
    while not number.isdigit():
        number = input("Please Enter a valid digit with no spaces or 0 to cancel:\n").strip()
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
    if pressed_zero(name):
        return str(0)
    pattern = re.compile(r"^[a-zA-Z\s'-]+$")
    while not pattern.match(name) or not name:
        name = input("Please enter a valid name using english letters only or 0 to cancel:\n").strip()
        if pressed_zero(name):
            return str(0)
    return name

# verifying the password to not contain whitespaces at all
def verify_password(password):
    if pressed_zero(password):
        return str(0)
    pattern = re.compile(r"^.*\s+.*$")
    while pattern.match(password) or not password:
        password = input("Please enter your password without whitespaces or 0 to cancel:\n").strip()
        if pressed_zero(password):
            return str(0)
    return password

def main():
    pass

if __name__ == "__main__":
    main()