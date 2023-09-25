from User import *
from InputValidators import *

class UserManger:
    @staticmethod
    def sign_up():
        username = verify_username(input("Enter your username (no spaces): ").strip())
        password = verify_password(input("Enter your password (no spaces): ").strip())
        User.users.add_user(User(username, password))

def main():
    pass

if __name__ == '__main__':
    main()