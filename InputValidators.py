import re
import os

# a function to check if the input number is in range a minimum and a maximum value
def check_number_in_range(minimum, maximum):
    number = input(f"Enter a number in range {minimum} - {maximum}: ").strip()

    while (not number.isdigit()) or int(number) > maximum or int(number) < maximum:
        number = input("Please Enter a valid number\n").strip()

    return number

# check if the username is unique
def check_unique(username):
    # initializing the directory
    file_path = "UserData"
    usernames = os.listdir(file_path)

    # checking if the username is present in the directory
    while username in usernames:
        username = input("Please Enter another username as this one is taken: ").strip()
    return username

# a function to check the username starts with a letter then digits and is unique
def verify_username(username):
    # check if it is unique before matching the regex pattern
    username = check_unique(username)

    pattern = re.compile(r"^[a-zA-Z]+\w*$")
    while not pattern.match(username):
        username = input("Please Enter a valid username starting with a letter: ").strip()
        username = check_unique(username)
    return username

# verify the password has no spaces
def verify_password(password):
    pattern = re.compile(r"^\S$")
    while pattern.match(password):
        password = input("Please Enter your password without whitespaces: ").strip()
    return password

def main():
    pass

if __name__ == '__main__':
    main()
