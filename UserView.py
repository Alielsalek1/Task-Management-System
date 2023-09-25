from InputValidators import *

class UserView:
    @staticmethod
    def main_menu():
        print("\nMenu: ")
        print("         1: Login")
        print("         2: Sign Up")
        return check_number_in_range(1, 2)

def main():
    pass

if __name__ == '__main__':
    main()