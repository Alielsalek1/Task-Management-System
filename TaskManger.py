from Task import Task
from UserView import *
import json

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
                    Task.create_task(username)
                case 2:
                    Task.edit_task(username)
                case 3:
                    Task.delete_task(username)
                case 4:
                    cls.view_tasks(username)
                case 5:
                    break

    @classmethod
    def get_task(cls, username, all_tasks):
        """
           Retrieve a specific task for a given user.

           Args:
                cls (class): The class itself.
                username (str): The username of the user for whom to retrieve the task.
                all_tasks (list of dicts): a list of all objects we have

           Returns:
                Task object: An instance of the Task class representing the selected task.

            Note:
                This method assumes that the 'UserData' directory and 'tasks.json' already exists.
           """
        task_manager = TaskManager(f"UserData/{username}/tasks.json")

        # List the titles of all tasks
        task_manager.list_tasks_titles(all_tasks)

        # Prompt the user to choose a task to edit
        choice = int(check_number_in_range(1, len(all_tasks)))
        choice -= 1

        # Return the selected task object
        return Task(**all_tasks[choice])

    @classmethod
    def add_task_to_db(cls, username, task):
        path = f"UserData/{username}/tasks.json"

        # Get all the user's tasks from the JSON file
        all_tasks = cls.get_user_tasks(username)

        # Append the new task to the existing list of tasks
        all_tasks.append(task.to_dict())

        # Write the updated dictionary back to the JSON file
        Task.write_to_json_file(path, all_tasks)

    @classmethod
    def delete_task_from_db(cls, username, required_task, all_tasks):
        path = f"UserData/{username}/tasks.json"

        # filter the data
        filtered_data = [task for task in all_tasks if task["title"] != required_task.title]

        # write the data back
        Task.write_to_json_file(path, filtered_data)

    @classmethod
    # return an array with tasks
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
        cnt = 0
        for task in all_tasks:
            cnt += 1
            print(f"{cnt} - {task['title']}")

    @staticmethod
    def sort_by_due_date(all_tasks):
        tasks_with_dates, tasks_without_dates = ([task for task in all_tasks if task["due_date"]],
                                                 [task for task in all_tasks if not task["due_date"]])
        date_format = "%d/%m/%Y"
        # Add tasks with date to the list first sorted by date, then Add tasks without dates sorted by title
        tasks = sorted(tasks_with_dates, key=lambda x: datetime.strptime(x["due_date"], date_format))
        tasks = [*tasks , *sorted(tasks_without_dates, key=lambda x: x["title"])]
        return tasks

    @classmethod
    def view_tasks(cls, username):
        all_tasks = cls.get_user_tasks(username)

        if not all_tasks:
            return print("No Tasks to view")

        choice = UserView.view_task_menu()
        match int(choice):
            case 1:
                cls.print_all_tasks(sorted(all_tasks, key=lambda x: int(x["priority"]), reverse=True))
            case 2:
                cls.print_all_tasks(sorted(all_tasks, key=lambda x: x["title"]))
            case 3:
                cls.print_all_tasks(cls.sort_by_due_date(all_tasks))
            case 4:
                return

def main():
    pass

if __name__ == '__main__':
    main()