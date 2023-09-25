import os
import json

class User:
    @staticmethod
    def create_user(username, password):
        # credentials of the user to be stored as a json file
        data = {
            "username": username,
            "password": password
        }

        # creating the string data to be ready to be added to directory
        json_data = json.dumps(data, indent=4)

        # creating a directory holding the username to store his data
        file_path = os.path.join("UserData", username)
        os.mkdir(file_path)

        # creating empty tasks json file to read a list of tasks
        tasks_file = os.path.join(file_path, "tasks.json")
        with open(f"{tasks_file}", 'w') as file:
            file.write('{}')

        # Path for storing credentials
        credentials_file = os.path.join(file_path, "Credentials.json")

        # Save credentials to json file
        with open(f"{credentials_file}", 'w') as file:
            file.write(json_data)

    def __init__(self, username, password):
        self._username = username
        self._password = password
        self._tasks = {}

        self.create_user(username, password)

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

def main():
    pass

if __name__ == '__main__':
    main()
