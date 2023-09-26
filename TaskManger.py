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
                    Task.Task.create_task(username)
                case 2:
                    ...
                case 3:
                    ...
                case 4:
                    cls.view_tasks(username)
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

    @classmethod
    def add_task_to_db(cls,username, task):

        # Load the existing JSON file into a Python dictionary
        with open(f"UserData/{username}/tasks.json", 'r') as file:
            tasks = json.load(file)

        # Define the new user object
        new_task = task.to_dict()

        # Append the new user to the "users" list in the dictionary
        tasks[new_task["title"]] = new_task

        # Write the updated dictionary back to the JSON file
        with open(f"UserData/{username}/tasks.json", 'w') as file:
            json.dump(tasks, file, indent=4)

    @classmethod
    def get_task(cls, username , title):
        """
         Retrieve a task by its title.

         Args:
             username (str): The username of the task owner.
             title (str): The title of the task to retrieve.

         Returns:
             Task: An instance of the Task class representing the retrieved task, or None if not found.
         """
        with open(f"UserData/{username}/tasks.json", 'r') as file:
            tasks = json.load(file)

        # Check if there are tasks in the JSON data.
        if tasks:
            # Create an instance of the Task class using the data from the JSON dictionary.
            return Task.Task(**tasks)

    @classmethod
    # a function that return an array with tasks
    def get_user_tasks(cls, username):
        # getting the array inside the json file
        path = f"UserData/{username}/tasks.json"
        with open(path, 'r') as file:
            data = json.load(file)
        return data

    @staticmethod
    def print_user_tasks(all_tasks):
        for task in all_tasks:
            print(task["title"])
            print(f"Description: {task['description']}")
            print(f"Due Date: {task['due_date']}")
            print(f"Priority: {task['priority']}")
            print(f"Status: {task['status']}")

    @classmethod
    def view_tasks(cls, username):
        all_tasks = cls.get_user_tasks(username)
        choice = UserView.view_task_options()

        match choice:
            case 1:
                cls.print_user_tasks(sorted(all_tasks, key=lambda x: x["priority"]))
            case 2:
                cls.print_user_tasks(sorted(all_tasks, key=lambda x: x["title"]))
            case 3:
                date_format = "%d/%m/%Y"
                cls.print_user_tasks(sorted(all_tasks, key=lambda x: datetime.strptime(x["date"], date_format)))

def main():
    pass

if __name__ == '__main__':
    main()
