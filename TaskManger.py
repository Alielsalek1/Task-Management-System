import json
import Task
from UserView import *

class TaskManager:

    def __init__(self, filename):
        # Initialize a TaskManager with a JSON file for storing tasks
        self.filename = filename

    @classmethod
    def choose_from_menu(cls, username):
        while True:
            choice = UserView.user_menu()
            match choice:
                case 1:
                    ...
                case 2:
                    ...
                case 3:
                    ...
                case 4:
                    ...
                case 5:
                    break

    @classmethod
    def instantiate_from_json(cls, json_data):
        task_data = json.load(json_data)
        task = Task.Task(
            title=task_data['title'],
            description=task_data['description'],
            due_date=task_data['due_date'],
            priority=task_data['priority'],
            status=task_data['status'],
        )
        return task

    # add the task to json file
    def add_task(self, task):

        # Load the existing JSON file into a Python dictionary
        with open(self.filename, 'r') as file:
            data = json.load(file)

        # Define the new user object
        new_task = task.to_dict()

        # Append the new user to the "users" list in the dictionary
        data['tasks'].append(new_task)

        # Write the updated dictionary back to the JSON file
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)


    def get_task(self, title):
        """
         Retrieve a task by its title.

         Args:
             title (str): The title of the task to retrieve.

         Returns:
             Task: An instance of the Task class representing the retrieved task, or None if not found.
         """
        with open(self.filename, 'r') as file:
            tasks = json.load(file)

        # Check if there are tasks in the JSON data.
        if tasks:
            # Create an instance of the Task class using the data from the JSON dictionary.
            return Task.Task(**tasks)
def main():
    pass

if __name__ == '__main__':
    main()
