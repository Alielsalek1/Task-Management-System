# Task Management System

Welcome to the Task Management System project! This application allows users to manage tasks, including adding, editing, deleting, and viewing tasks. The project is written in Python 3 and uses Object-Oriented Programming (OOP) principles.

## Features

- **User Authentication**: Users can sign up and log in securely using their credentials.
- **Task Management**: Users can perform various operations on their tasks, including:
  - Adding tasks with the following details:
    - Title
    - Description
    - Priority
    - Due Date
    - Status
  - Editing tasks to update any of the details.
  - Deleting tasks to remove unwanted tasks.
  - Viewing tasks sorted by priority, due date, or alphabetically.

## File Storage

All user data is stored using JSON files. Each user has their own directory containing two essential files:

1. `credentials.json`: Stores user account information, including usernames and hashed passwords.

2. `tasks.json`: Stores the tasks associated with the user. Each task is stored as a JSON object with the following attributes:
   - `id`: Unique identifier for the task.
   - `title`: Title of the task.
   - `description`: Description of the task.
   - `priority`: Priority level of the task.
   - `due_date`: Due date of the task.
   - `status`: Status of the task ("Incomplete", "Completed").

## Contributing

Contributions to this project are welcome! If you'd like to contribute, please follow these steps:

1. **Fork the repository.**
2. **Create a new branch** for your feature or bug fix.
3. **Make your changes** and commit them.
4. **Push your changes** to your fork.
5. **Create a pull request** to the original repository.
