class Task:

    def __init__(self, title, description, due_date, priority, status=False):
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
    def update(self, title=None, description=None, due_date=None, priority=None, status=None):
        # Update task attributes if new values are provided
        if title is not None:
            self.title(title)
        if description is not None:
            self.description(description)
        if due_date is not None:
            self.due_date(due_date)
        if priority is not None:
            self.priority(priority)
        if status is not None:
            self.status(status)

    def mark_completed(self):
        self.status = True

    def mark_incomplete(self):
        self.status = False

    def get_details(self):
        # Get a formatted string containing task details
        status_str = "Completed" if self.status else "Incomplete"
        return (
            f"Title: {self.title}\n"
            f"Description: {self.description}\n"
            f"Due Date: {self.due_date}\n"
            f"Priority: {self.priority}\n"
            f"Status: {status_str}"
        )

    def to_dict(self):
        # Define a method to convert an object instance to a dictionary.
        return {"title": self.title,
                "description": self.description,
                "due_date": self.due_date,
                "priority": self.priority,
                "status": self.status
        }

    def __str__(self):
        # Get a string representation of the task
        return self.get_details()

def main():
    pass

if __name__ == main:
    main()