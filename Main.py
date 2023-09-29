from User import *
from UserView import *

def system_run():
    choice = UserView.main_menu()
    if int(choice) == int(1):
        User.log_in()
    else:
        User.sign_up()

def main():
    while True:
        system_run()

if __name__ == '__main__':
    main()