from InputValidators import *
from User import *

class UserManger:
    @staticmethod
    def sign_up():
        username = verify_username(input("Enter your username (no spaces): ").strip())
        password = verify_password(input("Enter your password (no spaces): ").strip())
        User(username, password)


def main():
    pass

if __name__ == '__main__':
    main()
