import InputValidators
import TaskManger


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

    @classmethod
    def create_task(cls, username):
        # Prompt the user to input a task title and validate it to ensure it's not empty
        task_title = InputValidators.verify_argument_not_empty(
            input("Please enter a task title or 0 to cancel: ").strip())
        if InputValidators.pressed_zero(task_title):
            return

        # Prompt the user to input a task description and validate it to ensure it's not empty
        task_description = InputValidators.verify_argument_not_empty(
            input("Please enter the task's description or 0 to cancel: ").strip())
        if InputValidators.pressed_zero(task_description):
            return

        # Prompt the user to input a due date in the format DD/MM/YYYY or 0 to skip and validate it
        task_due_date = InputValidators.verify_due_date(
            input("Enter the task's due date (DD/MM/YYYY) or 0 to skip: ").strip())

        # Prompt the user to input a task priority within range of 1 to 10
        print("Please Enter Task Priority: ")
        task_priority = InputValidators.check_number_in_range(1, 10)

        # Create an instance of the TaskManager class, providing the path to the user's task data file
        task_manager = TaskManger.TaskManager(f"UserData/{username}/tasks.json")

        # Create a Task object using the collected information
        task = Task(task_title, task_description, str(task_due_date), task_priority)

        # Add the created task to the user's task database
        task_manager.add_task_to_db(username, task)

    @staticmethod
    def truncate_text(text, max_length = 20):
        return text[:max_length] + "..." if len(text) > max_length else text

    @classmethod
    def edit_task(cls, username):
        task_manager = TaskManger.TaskManager(f"UserData/{username}/tasks.json")

        # Retrieve all tasks for the user
        all_tasks = task_manager.get_user_tasks(username)

        # Check if there are tasks to edit
        if not all_tasks:
            return print("No Tasks to edit")

        # List the titles of all tasks
        task_manager.list_tasks_titles(all_tasks)

        # Prompt the user to choose a task to edit
        choice = int(InputValidators.check_number_in_range(1, len(all_tasks)))
        choice -= 1

        # Get the selected task object
        task = Task(**all_tasks[choice])

        print("Editing Task:")

        # Prompt the user to edit the task title or 0 to skip
        new_task_title = InputValidators.verify_argument_not_empty(
            input(f"Enter a new task title ({cls.truncate_text(task.title)}) or 0 to skip: ").strip())
        if InputValidators.pressed_zero(new_task_title):
            new_task_title = task.title

        # Prompt the user to edit the task description or press 0 to skip
        new_task_description = InputValidators.verify_argument_not_empty(
            input(f"Enter a new task description ({cls.truncate_text(task.description)}) or 0 to skip: ").strip())
        if InputValidators.pressed_zero(new_task_description):
            new_task_description = task.description

        # Prompt the user to edit the due date or press 0 to skip
        new_task_due_date = InputValidators.verify_due_date(
            input(
                f"Enter a new due date ({task.due_date}) or 0 to skip: ").strip())
        new_task_due_date = task.due_date if not new_task_due_date else new_task_due_date

        # Prompt the user to edit the task priority or press 0 to skip
        print(f"Enter a new task priority ({task.priority}).")
        new_task_priority = InputValidators.check_number_in_range(1, 10)

        while True:
            # Prompt the user to mark the task as completed or not
            is_task_completed = input(f"Mark this task as completed (y/n)? ").strip().lower()
            if is_task_completed in ("y", "n"):
                is_task_completed = "Completed" if is_task_completed == "y" else "Incomplete"
                break
            else:
                print("Please enter 'y' for yes or 'n' for no.")

        new_task = Task(new_task_title, new_task_description, str(new_task_due_date), int(new_task_priority), is_task_completed)

        # Save the updated task back to the user's task database
        task_manager.update_task_in_db(username, task ,new_task)

        print("Task updated successfully!")

    def __str__(self):
        # Get a string representation of the task
        return self.get_details()


def main():
    pass


if __name__ == main:
    main()
