# Today(21/08/2025) ,  We are building an Email Validator App

from email_validator import validate_email as validate_email_address, EmailNotValidError

print("Welcome to the Email Validator App!")


def email_validator():
    email = input("Enter an email address you would like to validate: ")

    try:
        validate_email_address(email)
        print(f"The address '{email}' is valid")
    except EmailNotValidError:
        print(f"The address '{email}' is NOT valid")


email_validator()
