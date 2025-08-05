# Today(4/8/25) , we are building a To-do List

import json
import os

FILENAME = "tasks.json"

# Load tasks from file if it exists
if os.path.exists(FILENAME):
    with open(FILENAME, "r") as file:
        tasks = json.load(file)
else:
    tasks = []


def addtask():
    task = input("Enter a task: ")
    tasks.append(task)
    save_tasks()
    print(f"Task '{task}' added successfully")


def listtask():
    if not tasks:
        print("No task available")
    else:
        print("Your tasks are: ")
        for index, task in enumerate(tasks):
            print(f"Task #{index + 1}. {task}")


def deletetask():
    listtask()
    try:
        tasktodelete = int(input("Enter the number of task to delete: ")) - 1
        if tasktodelete >= 0 and tasktodelete < len(tasks):
            removed = tasks.pop(tasktodelete)
            save_tasks()
            print(f"Task '{removed}' has been deleted")
        else:
            print(f"Task '#{tasktodelete + 1}' not found")
    except ValueError:
        print("Invalid input")


def save_tasks():
    with open(FILENAME, "w") as file:
        json.dump(tasks, file)


if __name__ == "__main__":
    print("Welcome to the To-Do list app")
    while True:
        print("\n")
        print("Please select one of the following functions")
        print("--------------------------------------------------")
        print("1. Add New Task")
        print("2. Delete a Task")
        print("3. List Tasks")
        print("4. Close")

        choice = int(input("Enter your choice: "))

        if (choice == 1):
            addtask()
        elif (choice == 2):
            deletetask()
        elif (choice == 3):
            listtask()
        elif (choice == 4):
            break
        else:
            print(f" '{choice}' is not a valid input, Try again")

print("Goodbye from the app")
