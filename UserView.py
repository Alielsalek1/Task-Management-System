from InputValidators import *

class UserView:
    @staticmethod
    def main_menu():
        print("\nMenu: ")
        print("         1: Login")
        print("         2: Sign Up")
        return check_number_in_range(1, 2)

    @staticmethod
    def user_menu():
        print("\nMenu: ")
        print("         1: add a Task")
        print("         2: Edit a Task")
        print("         3: delete a Task")
        print("         4: view all Tasks")
        print("         5: Logout")
        return check_number_in_range(1, 5)

def main():
    pass

if __name__ == '__main__':
    main()
