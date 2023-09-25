import re
from User import *

# a function to check if the input number is in range a minimum and a maximum value
def check_number_in_range(minimum, maximum):
    number = input(f"Enter a number in range {minimum} - {maximum}: ").strip()

    while (not number.isdigit()) or int(number) > maximum or int(number) < maximum:
        number = input("Please Enter a valid number\n").strip()

    return number

# a function to check the username starts with a letter then digits and is unique
def verify_username(username):
    pattern = re.compile(r"^[a-zA-Z]+\w*$")
    while not pattern.match(username):
        username = input("Please Enter a valid username starting with a letter: ").strip()
        User.check_unique(username)
    return username

# verify the password has no spaces
def verify_password(password):
    pattern = re.compile(r"\S")
    while not pattern.match(password):
        password = input("Please Enter your password without whitespaces: ").strip()
    return password

def main():
    pass

if __name__ == '__main__':
    main()