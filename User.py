from UserManger import *
from TaskManger import *

class User:
    def __init__(self, username, password):
        self._username = username
        self._password = password
        self._tasks = {}

        UserManger.add_user_to_db(username, password)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @classmethod
    def sign_up(cls):
        # get username
        username = verify_username(input("Enter your username or 0 to cancel: ").strip())
        if pressed_zero(username):
            return

        # get password
        password = verify_password(input("Enter your Password or 0 to cancel: ").strip())
        if pressed_zero(password):
            return

        # construct the user
        User(username, password)

    @staticmethod
    def valid_username(username):
        if pressed_zero(username):
            return str(0)

        # check if there is a directory with the username, so it has data, so it is valid
        while not check_in_files(username):
            username = input("Please Enter a valid username or 0 to cancel: ").strip()

            if pressed_zero(username):
                return str(0)

        return username

    @staticmethod
    def matched_passowrd(password, stored_password):
        ...

    @staticmethod
    def valid_password(username, password):
        if pressed_zero(password):
            return str(0)

        # get the password from the user's data
        stored_password = UserManger.get_hashed_password_from_db(username)

        # check the password matches
        while not bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
            password = input("re enter your password or 0 to cancel: ").strip()

            if pressed_zero(password):
                return str(0)

        return password

    @classmethod
    def log_in(cls):
        # get username
        username = cls.valid_username(input("Enter your username or 0 to cancel: ").strip())
        if pressed_zero(username):
            return

        # get password
        password = cls.valid_password(username, input("Enter your Password or 0 to cancel: ").strip())
        if pressed_zero(password):
            return

        TaskManager.choose_from_menu(username)

def main():
    pass

if __name__ == '__main__':
    main()
