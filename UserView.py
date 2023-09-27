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
        print("         1: Add a Task")
        print("         2: Edit a Task")
        print("         3: Delete a Task")
        print("         4: View all Tasks")
        print("         5: Logout")
        return check_number_in_range(1, 5)

    @staticmethod
    def view_task_options():
        print("\nMenu: ")
        print("         1: Sort by Priority")
        print("         2: Sort by Name")
        print("         3: Sort by Due Date")
        print("         4: Cancel")
        return check_number_in_range(1, 4)

def main():
    pass

if __name__ == '__main__':
    main()
