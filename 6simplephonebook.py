# Today(06/08/2025) , I am building a simple phonebook

import json
import os

FILENAME = "phonebook.json"

# Load tasks from file if it exists
if os.path.exists(FILENAME):
    try:
        with open(FILENAME, "r") as file:
            phonedetails = json.load(file)
    except (json.JSONDecodeError, ValueError):
        phonedetails = []
else:
    phonedetails = []

print("Welcome to The Phonebook app , accurately saving your details")
print("\n")


def addphonedetails():
    name = input("What is the name of the user: ")
    number = input("What is the phone number of the user: ")
    details = name, number
    phonedetails.append(details)
    save_phonedetails()
    print(f"Phone details for {name} has been successfully added")


def listphonedetails():
    if not phonedetails:
        print("No phone details available")
    else:
        print("Your phone details are: ")
        for index, details in enumerate(phonedetails):
            print(f"Task #{index + 1}. {details}")


def deletephonedetails():
    listphonedetails()
    try:
        detailtodelete = int(
            input("Enter the index of the detail to delete: ")) - 1
        if detailtodelete >= 0 and detailtodelete < len(phonedetails):
            removed = phonedetails.pop(detailtodelete)
            save_phonedetails()
            print(f"Task '{removed}' has been deleted")
        else:
            print(f"Task '#{detailtodelete + 1}' not found")
    except ValueError:
        print("Invalid input")


def searchphonedetails():
    search_name = input("Enter the name to search for: ").strip().lower()
    found = False
    for name, number in phonedetails:
        if name.strip().lower() == search_name:
            print(f"Found: Name: {name}, Number: {number}")
            found = True
    if not found:
        print("No details found for that name.")


def save_phonedetails():
    with open(FILENAME, "w") as file:
        json.dump(phonedetails, file)


if __name__ == "__main__":
    print("")
    while True:
        print("Please select one of the following functions")
        print("------------------------------------------------")

        print("1. Add new phone details")
        print("2. Delete phone details")
        print("3. List existing phone detail")
        print("4. Search phone details by name")
        print("5. Close Program")

        try:
            choice = int(input("What is your choice: "))
        except ValueError:
            print("Invalid input, please enter a number.")
            continue

        if (choice == 1):
            addphonedetails()
        elif (choice == 2):
            deletephonedetails()
        elif (choice == 3):
            listphonedetails()
        elif choice == 4:
            searchphonedetails()
        elif (choice == 5):
            break
        else:
            print(f" '{choice}' is not a valid input, Try again")

print("Thank you for using the phonebook app")
