import json
import Task
import datetime
from UserView import *


class TaskManager:
    def __init__(self, filename):
        # Initialize a TaskManager with a JSON file for storing tasks
        self.filename = filename

    @classmethod
    def choose_from_menu(cls, username):
        while True:
            choice = UserView.user_menu()
            match int(choice):
                case 1:
                    Task.Task.create_task(username)
                case 2:
                    ...
                case 3:
                    cls.delete_task(username)
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

    @staticmethod
    def add_task_to_db(username, task):
        path = f"UserData/{username}/tasks.json"

        # Load the existing JSON file into a Python dictionary
        with open(path, 'r') as file:
            tasks = json.load(file)

        # Define the new user object
        new_task = task.to_dict()

        # Append the new user to the "users" list in the dictionary
        tasks["all_tasks"].append(new_task)

        # Write the updated dictionary back to the JSON file
        with open(f"UserData/{username}/tasks.json", 'w') as file:
            json.dump(tasks, file, indent=4)

    @classmethod
    def get_task(cls, username, title):
        """
          Retrieve a task by its title for a specific user.

          args:
              username (str): The username of the task owner.
              title (str): The title of the task to retrieve.

          return:
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
        return data["all_tasks"]

    @staticmethod
    def print_all_tasks(all_tasks):
        cnt = 1
        for task in all_tasks:
            print(f"\n{cnt} - {task['title']}")
            print(f"Description: {task['description']}")
            print(f"Due Date: {task['due_date']}")
            print(f"Priority: {task['priority']}")
            print(f"Status: {task['status']}\n")
            cnt += 1

    @staticmethod
    def list_tasks_titles(all_tasks):
        """
        list all tasks titles to choose from them

        args: all_tasks an array of objects (task)

        """
        # list tasks title to delete the one the user selects
        cnt = 0
        for task in all_tasks:
            cnt += 1
            print(f"{cnt} - {task['title']}")

    @classmethod
    def delete_task(cls, username):
        # an array which is the json file
        all_tasks = cls.get_user_tasks(username)

        if input("press 0 to cancel or 1 to continue: ") == str(0):
            return

        if not all_tasks:
            return print("No Tasks to delete!!")
        cls.list_tasks_titles(all_tasks)

        # choose the object you want to delete
        choice = int(check_number_in_range(1, len(all_tasks)))
        choice -= 1

        # filter the data
        filtered_data = [task for task in all_tasks if all_tasks[choice] != task]

        # initializing for the json file
        json_dict = {"all_tasks": filtered_data}

        # clear the json file
        path = f"UserData/{username}/tasks.json"
        empty_json_file(path)

        # put in the filtered data
        with open(path, 'w') as file:
            json.dump(json_dict, file, indent=4)

        print("Deleted Successfully!!")

    @classmethod
    def view_tasks(cls, username):
        all_tasks = cls.get_user_tasks(username)

        if not all_tasks:
            return print("No Tasks to delete")

        choice = UserView.view_task_options()

        match int(choice):
            case 1:
                cls.print_all_tasks(sorted(all_tasks, key=lambda x: int(x["priority"]), reverse=True))
            case 2:
                cls.print_all_tasks(sorted(all_tasks, key=lambda x: x["title"]))
            case 3:
                tasks_with_dates, tasks_without_dates = ([task for task in all_tasks if task["due_date"]],
                                                         [task for task in all_tasks if not task["due_date"]])

                # Print tasks with dates after sorting by date
                date_format = "%d/%m/%Y"
                cls.print_all_tasks(
                    sorted(tasks_with_dates, key=lambda x: datetime.strptime(x["due_date"], date_format)))

                # Print tasks without dates after sorting by title
                cls.print_all_tasks(sorted(tasks_without_dates, key=lambda x: x["title"]))

            case 4:
                return

def main():
    pass

if __name__ == '__main__':
    main()
