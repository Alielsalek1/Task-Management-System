from InputValidators import *
import json

class UserManger:
    @staticmethod
    def get_password_from_db(username):
        # opening the json file to check the password matches the one the user gave us
        with open(f"UserData/{username}/Credentials.json", 'r') as json_file:
            data = json.load(json_file)

        return data["password"]

    @staticmethod
    def empty_tasks_json_file(path):
        with open(path, 'w') as file:
            file.write('{"all_tasks": []}')

    @classmethod
    # creating empty tasks JSON file to read a list of tasks
    def create_tasks_json(cls, file_path):
        tasks_file = os.path.join(file_path, "tasks.json")
        cls.empty_tasks_json_file(tasks_file)

    @staticmethod
    # convert a JSON file to a string
    def get_json_data(username, password):
        # credentials of the user to be stored as a json file
        data = {
            "username": username,
            "password": password
        }

        # creating the string data to be ready to be added to directory
        return json.dumps(data, indent=4)

    @staticmethod
    def create_username_dir(file_path):
        # creating a directory holding the username to store his data
        os.mkdir(file_path)

    @staticmethod
    def create_credentials(file_path, json_data):
        # Path for storing credentials
        credentials_file = os.path.join(file_path, "Credentials.json")

        # Save credentials to json file
        with open(f"{credentials_file}", 'w') as file:
            file.write(json_data)

    @classmethod
    def add_user_to_db(cls, username, password):
        """
        Adds a new user to the database.

        This method creates a directory with the user's username as the directory name.
        Inside this directory, two files are created:
        - 'credentials.json': Contains the user's username and password.
        - 'tasks.json': An empty JSON file to store the user's tasks.

        Args:
            username (str): The user's username.
            password (str): The user's password.

        Returns:
            None

        Note:
            This method assumes that the 'UserData' directory already exists.
        """
        # get the data as a string
        json_data = cls.get_json_data(username, password)

        # create the file_path and create username directory
        file_path = os.path.join("UserData", username)
        cls.create_username_dir(file_path)

        # create the tasks.json file
        cls.create_tasks_json(file_path)

        # create the credentials.json file and fill it with our json_data
        cls.create_credentials(file_path, json_data)

def main():
    pass

if __name__ == '__main__':
    main()
