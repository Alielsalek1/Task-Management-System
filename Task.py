from UserManger import *
from InputValidators import *
import TaskManger as TM


class Task:
    def __init__(self, title, description, due_date, priority, status="Incomplete"):
        # Initialize a Task object with provided attributes
        self._title = title
        self._description = description
        self._due_date = due_date
        self._priority = priority
        self._status = status

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        self._due_date = due_date

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, priority):
        self._priority = priority

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    def get_details(self):
        # Get a formatted string containing task details
        return (
            f"Title: {self.title}\n"
            f"Description: {self.description}\n"
            f"Due Date: {self.due_date}\n"
            f"Priority: {self.priority}\n"
            f"Status: {self.status}"
        )

    def to_dict(self):
        # Define a method to convert an object instance to a dictionary.
        return {"title": self.title,
                "description": self.description,
                "due_date": self.due_date,
                "priority": self.priority,
                "status": self.status
                }

    @staticmethod
    def cancel_message():
        return input("Press 0 to cancel or anything to continue: ")

    @classmethod
    def create_task(cls, username):
        # Prompt the user to input a task title and validate it to ensure it's not empty
        task_title = verify_argument_not_empty(
            input("Please enter a task title or 0 to cancel: ").strip())
        if pressed_zero(task_title):
            return

        # Prompt the user to input a task description and validate it to ensure it's not empty
        task_description = verify_argument_not_empty(
            input("Please enter the task's description or 0 to cancel: ").strip())
        if pressed_zero(task_description):
            return

        # Prompt the user to input a due date in the format DD/MM/YYYY or 0 to skip and validate it
        task_due_date = verify_due_date(input("Enter the task's due date (DD/MM/YYYY) or 0 to skip: ").strip())

        # Prompt the user to input a task priority within range of 1 to 10
        print("Please Enter Task Priority: ")
        task_priority = check_number_in_range(1, 10)

        # Create an instance of the TaskManager class, providing the path to the user's task data file
        task_manager = TM.TaskManager(f"UserData/{username}/tasks.json")

        # Create a Task object using the collected information
        task = Task(task_title, task_description, str(task_due_date), task_priority)

        # Add the created task to the user's task database
        task_manager.add_task_to_db(username, task)

    @staticmethod
    def truncate_text(text, max_length=20):
        return text[:max_length] + "..." if len(text) > max_length else text

    @staticmethod
    def is_task_completed():
        while True:
            # Prompt the user to mark the task as completed or not
            status = input(f"Mark this task as completed (y/n)? ").strip().lower()

            if status in ("y", "n"):
                status = "Completed" if status == "y" else "Incomplete"
                return status
            else:
                print("Please enter 'y' for yes or 'n' for no.")

    @classmethod
    def edit_task(cls, username):
        all_tasks = TM.TaskManager.get_user_tasks(username)
        # check if there are no tasks to access
        if not all_tasks:
            return print("No tasks available")

        # if you want ot cancel
        if pressed_zero(cls.cancel_message()):
            return

        old_task = TM.TaskManager.get_task(username, all_tasks)

        print("Editing Task:")

        # Prompt the user to edit the task title or 0 to skip
        new_task_title = verify_argument_not_empty(
            input(f"Enter a new task title ({cls.truncate_text(old_task.title)}) or 0 to skip: ").strip())
        if pressed_zero(new_task_title):
            new_task_title = old_task.title

        # Prompt the user to edit the task description or press 0 to skip
        new_task_description = verify_argument_not_empty(
            input(f"Enter a new task description ({cls.truncate_text(old_task.description)}) or 0 to skip: ").strip())
        if pressed_zero(new_task_description):
            new_task_description = old_task.description

        # Prompt the user to edit the due date or press 0 to skip
        new_task_due_date = verify_due_date(
            input(f"Enter a new due date ({old_task.due_date}) or 0 to skip: ").strip())
        new_task_due_date = old_task.due_date if not new_task_due_date else new_task_due_date

        # Prompt the user to edit the task priority or press 0 to skip
        print(f"Enter a new task priority ({old_task.priority}).")
        new_task_priority = check_number_in_range(1, 10)

        # task status completed or not completed
        status = cls.is_task_completed()

        # construct new task
        new_task = Task(new_task_title, new_task_description, str(new_task_due_date), int(new_task_priority), status)

        # delete the old task
        TM.TaskManager.delete_task_from_db(username, old_task, all_tasks)

        # Save the updated task back to the user's task database
        TM.TaskManager.add_task_to_db(username, new_task)

        print("Task updated successfully!!")

    # Write the data back to the JSON file
    @staticmethod
    def write_to_json_file(path, tasks_list):
        # put in the filtered data
        with open(path, 'w') as file:
            json.dump({"all_tasks": tasks_list}, file, indent=4)

    @classmethod
    def delete_task(cls, username):
        all_tasks = TM.TaskManager.get_user_tasks(username)

        # check if there are no tasks to access
        if not all_tasks:
            return print("No tasks available")

        # if you want ot cancel
        if pressed_zero(cls.cancel_message()):
            return

        # Retrieve the required task and all tasks for the user
        required_task = TM.TaskManager.get_task(username, all_tasks)

        # Delete the task from the database
        TM.TaskManager.delete_task_from_db(username, required_task, all_tasks)

        print("Deleted Successfully!!")

    def __str__(self):
        # Get a string representation of the task
        return self.get_details()


def main():
    pass


if __name__ == main:
    main()
