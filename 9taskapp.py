# This is a task reminder app being made today  16/08/2025

import json
import os
import threading
import time


FILENAME = "task_app.json"

# Load tasks from file if it exists
if os.path.exists(FILENAME):
    try:
        with open(FILENAME, "r") as file:
            taskdetails = json.load(file)
    except (json.JSONDecodeError, ValueError):
        taskdetails = []
else:
    taskdetails = []


def set_timer(seconds, task):
    def timer_thread():
        print(f"Timer set for {seconds} seconds.")
        time.sleep(seconds)
        print(f"⏰ Its time for '{task}'! Alert!")

    t = threading.Thread(target=timer_thread)
    t.start()


def addtask():
    task = input("What is the task you want to add: ")
    set_timer_choice = input(
        "Do you want to set a timer for this task? (Yes/No): ").strip().lower()
    if set_timer_choice == "yes":
        try:
            seconds = int(input("How many seconds should the timer last?: "))
            set_timer(seconds, task)
        except ValueError:
            print("Invalid input for seconds. No timer set.")
    taskdetails.append(task)
    save_taskdetails()
    print(f"Task '{task}' has been successfully added")


def listtasks():
    if not taskdetails:
        print("No tasks available")
    else:
        print("Your ongoing tasks are: ")
        for index, details in enumerate(taskdetails):
            print(f"Task #{index + 1}. {details}")


def deletetask():
    listtasks()
    try:
        tasktodelete = int(
            input("Enter the index of the task to delete: ")) - 1
        if tasktodelete >= 0 and tasktodelete < len(taskdetails):
            removed = taskdetails.pop(tasktodelete)
            save_taskdetails()
            print(f"Task '{removed}' has been deleted")
        else:
            print(f"Task '#{tasktodelete + 1}' not found")
    except ValueError:
        print("Invalid input")


def save_taskdetails():
    with open(FILENAME, "w") as file:
        json.dump(taskdetails, file)


print("Welcome to the Tasks App")


if __name__ == "__main__":
    print("")
    while True:
        print("Please select one of the following functions")
        print("_______________________________________________")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. List all ongoing tasks")
        print("4. Exit the app")

        try:
            task_choice = int(input("What is your choice: "))
        except ValueError:
            print("Invalid input, please enter a number.")
            continue

        if task_choice == 1:
            addtask()
        elif task_choice == 2:
            deletetask()
        elif task_choice == 3:
            listtasks()
        elif task_choice == 4:
            break
        else:
            print(f"{task_choice} is an invalid input, please try again")

print("Thank you for using the Tasks App")
