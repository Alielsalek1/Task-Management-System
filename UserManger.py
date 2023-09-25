from InputValidators import *
from TaskManger import *
from User import *

class UserManger:
    @staticmethod
    def sign_up():
        username = verify_username(input("Enter your username (no spaces): ").strip())
        password = verify_password(input("Enter your password (no spaces): ").strip())
        User(username, password)

    @staticmethod
    def valid_username(username):
        # check if there is a directory with the username, so it has data, so it is valid
        while not check_in_files(username):
            username = input("Please Enter a valid username: ").strip()

        return username

    @staticmethod
    def valid_password(username, password):
        # opening the json file to check the password matches the one the user gave us
        file_path = f"UserData/{username}/Credentials.json"
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        # check the password matches
        while password != data["password"]:
            password = input("Invalid Password!").strip()

    @classmethod
    def log_in(cls):
        username = cls.valid_username(input("Enter your username: ").strip())
        cls.valid_password(username, input("Enter your Password: ").strip())
        TaskManager.choose_from_menu(username)

def main():
    pass

if __name__ == '__main__':
    main()
