import re
import os
from datetime import datetime

def go_back(argument):
    if argument == str(0):
        return True
    return False

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
        username = input("Please Enter another username as this one is taken or 0 to cancel: ").strip()

    pattern = re.compile(r"^[a-zA-Z]+\w*$")
    while not pattern.match(username):

        if go_back(username):
            return str(0)

        username = input("Please Enter a valid username starting with a letter or 0 to cancel: ").strip()

        if go_back(username):
            return str(0)

        while check_in_files(username):
            username = input("Please Enter another username as this one is taken or 0 to cancel: ").strip()

            if go_back(username):
                return str(0)

    return username

# verify the password has no spaces
def verify_password(password):

    if go_back(password):
        return str(0)

    while ' ' in password:
        password = input("Please Enter your password without whitespaces or 0 to cancel: ").strip()

        if go_back(password):
            return str(0)

    return password

def verify_argument_not_empty(input_str):
    while not input_str:
        print("This argument can't be empty: ")
        input_str = input().strip()
    return input_str

def empty_json_file(path):
    with open(path, 'w') as file:
        file.write('{"all_tasks": []}')

def verify_due_date(date_str):
    """
      Verify and parse a due date string.

      Args:
          date_str (str): The input date string in the format DD/MM/YYYY or '0' to skip.

      Returns:
          datetime or None: A datetime object representing the due date if valid,
          or None if the input is '0' indicating no due date.

      Raises:
          ValueError: If the input date string is in an invalid format.

      """
    while True:
        if date_str == "0":
            return None  # Return None to indicate no due date

        try:
            due_date = datetime.strptime(date_str, "%d/%m/%Y")
            formatted_due_date = due_date.strftime("%d/%m/%Y")
            return formatted_due_date

        except ValueError:
            date_str = input("Invalid date format. Please use (DD/MM/YYYY) or enter 0 to skip: ")


def main():
    pass

if __name__ == '__main__':
    main()