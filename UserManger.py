from TaskManger import *
from User import *

class UserManger:
    @staticmethod
    def sign_up():
        # get username
        username = verify_username(input("Enter your username or 0 to cancel: ").strip())
        if username == str(0):
            return

        # get password
        password = verify_password(input("Enter your Password or 0 to cancel: ").strip())
        if password == str(0):
            return

        User(username, password)

    @staticmethod
    def valid_username(username):
        if go_back(username):
            return str(0)

        # check if there is a directory with the username, so it has data, so it is valid
        while not check_in_files(username):
            username = input("Please Enter a valid username or 0 to cancel: ").strip()
            if go_back(username):
                return str(0)

        return username

    @staticmethod
    def valid_password(username, password):
        if go_back(password):
            return str(0)

        # opening the json file to check the password matches the one the user gave us
        file_path = f"UserData/{username}/Credentials.json"
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        # check the password matches
        while password != data["password"]:
            password = input("re enter your password or 0 to cancel: ").strip()
            if go_back(password):
                return str(0)

        return password

    @classmethod
    def log_in(cls):
        # get username
        username = cls.valid_username(input("Enter your username or 0 to cancel: ").strip())
        if go_back(username):
            return

        # get password
        password = cls.valid_password(username, input("Enter your Password or 0 to cancel: ").strip())
        if go_back(password):
            return

        TaskManager.choose_from_menu(username)

def main():
    pass

if __name__ == '__main__':
    main()
