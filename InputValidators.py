import re
import os
from datetime import datetime

# a function to check if the input number is in range a minimum and a maximum value
def check_number_in_range(minimum, maximum):
    number = input(f"Enter a number in range {minimum} - {maximum}: ").strip()

    while (not number.isdigit()) or int(number) > maximum or int(number) < minimum:
        number = input("Please Enter a valid number: \n").strip()

    return number

# check if the username is in the files
def check_in_files(username):
    # initializing the directory
    file_path = "UserData"
    usernames = os.listdir(file_path)

    # checking if the username is present in the directory
    if username in usernames:
        return True
    return False

# a function to check the username starts with a letter then digits and is unique
def verify_username(username):
    # check if it is unique before matching the regex pattern
    while check_in_files(username):
        username = input("Please Enter another username as this one is taken: ").strip()

    pattern = re.compile(r"^[a-zA-Z]+\w*$")
    while not pattern.match(username):
        username = input("Please Enter a valid username starting with a letter: ").strip()
        while check_in_files(username):
            username = input("Please Enter another username as this one is taken: ").strip()

    return username

# verify the password has no spaces
def verify_password(password):
    pattern = re.compile(r"^\S$")
    while pattern.match(password):
        password = input("Please Enter your password without whitespaces: ").strip()
    return password

def verify_argument_not_empty(input_str):
    while not input_str:
        print("This argument can't be empty: ")
        input_str = input().strip()
    return input_str


def main():
    pass

if __name__ == '__main__':
    main()
