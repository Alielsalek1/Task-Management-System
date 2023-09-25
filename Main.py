from UserView import *
from UserManger import *


def system_run():
    choice = UserView.main_menu()
    if int(choice) == 1:
        ...
    else:
        UserManger.sign_up()


def main():
    while True:
        system_run()

if __name__ == '__main__':
    main()