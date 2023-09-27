from TaskManger import *
from User import *

class UserManger:
    @staticmethod
    def sign_up():
        # get username
        username = input("Enter your username or 0 to cancel: ").strip()
        if username == str(0):
            return
        username = verify_username(username)

        # get password
        password = input("Enter your Password or 0 to cancel: ").strip()
        if password == str(0):
            return
        password = verify_password(password)

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
        # get username
        username = input("Enter your username or 0 to cancel: ").strip()
        if username == str(0):
            return
        username = cls.valid_username(username)

        # get password
        password = input("Enter your Password or 0 to cancel: ").strip()
        if password == str(0):
            return
        cls.valid_password(username, password)

        TaskManager.choose_from_menu(username)

def main():
    pass

if __name__ == '__main__':
    main()
