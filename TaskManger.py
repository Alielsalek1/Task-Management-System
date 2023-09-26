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

    def add_task_to_db(self, username, task):

        # Load the existing JSON file into a Python dictionary
        with open(self.filename, 'r') as file:
            tasks = json.load(file)

        # Define the new user object
        new_task = task.to_dict()

        # Append the new user to the "users" list in the dictionary
        tasks[new_task["title"]] = new_task

        # Write the updated dictionary back to the JSON file
        with open(f"UserData/{username}/tasks.json", 'w') as file:
            json.dump(tasks, file, indent=4)

    @classmethod
    def get_task(cls, username, title):
        """
          Retrieve a task by its title for a specific user.

          Args:
              username (str): The username of the task owner.
              title (str): The title of the task to retrieve.

          Returns:
              Task or None: An instance of the Task class representing the retrieved task
                           if found for the specified user, or None if not found.
          """
        with open(f"UserData/{username}/tasks.json", 'r') as file:
            tasks = json.load(file)

        # Check if there are tasks in the JSON data.
        for task in tasks:
            if task.title == title:
                return Task.Task(**task)

    @classmethod
    # a function that return an array with tasks
    def get_user_tasks(cls, username):
        # getting the array inside the json file
        path = f"UserData/{username}/tasks.json"
        with open(path, 'r') as file:
            data = json.load(file)
        return data

    @staticmethod
    def print_all_tasks(all_tasks):
        for task in all_tasks:
            print(task["title"])
            print(f"Description: {task['description']}")
            print(f"Due Date: {task['due_date']}")
            print(f"Priority: {task['priority']}")
            print(f"Status: {task['status']}")

    @staticmethod
    def list_tasks_description(all_tasks):
        # list tasks title to delete the one the user selects
        cnt = 0
        for task in all_tasks:
            cnt += 1
            print(f"1 - {task['title']}")
        return cnt

    @classmethod
    def delete_task(cls, username):
        # an array which is the json file
        all_tasks = cls.get_user_tasks(username)

        # choose the object you want to delete
        choice = check_number_in_range(1, cls.list_tasks_description(all_tasks))
        choice -= 1

        # filter the data
        filtered_data = [task for task in all_tasks if all_tasks[choice] != task]

        # clear the json file
        path = f"UserData/{username}/tasks.json"
        empty_json_file(path)

        # put in the filtered data
        with open(path, 'w') as file:
            json.dump(filtered_data, file, indent=4)

    @classmethod
    def view_tasks(cls, username):
        all_tasks = cls.get_user_tasks(username)
        choice = UserView.view_task_options()

        match choice:
            case 1:
                cls.print_all_tasks(sorted(all_tasks, key=lambda x: x["priority"]))
            case 2:
                cls.print_all_tasks(sorted(all_tasks, key=lambda x: x["title"]))
            case 3:
                ...



def main():
    pass

if __name__ == '__main__':
    main()
