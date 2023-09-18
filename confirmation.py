def is_not_digit(number):
    return not number.isdigit()


def check_range(minimum_val, maximum_val, number):
    while True:
        if is_not_digit(number) or int(number) < minimum_val or int(number) > maximum_val:
            print(f"Please type a digit from {minimum_val} to {maximum_val}")
            number = input()
        else:
            return number

def main():
    ...


if __name__ == "__main__":
    main()
