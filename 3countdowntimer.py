# Creating a countdown timer using For Loops

import time

print("Countdown of 10 seconds")

timer = int(input("Enter the countdown timer in seconds: "))

for x in range(timer, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)


print("TIME IS UP!")
print(
    f"Your total time spent was {int(timer/3600)} hours , {int(timer / 60) % 60} minutes and {timer % 60} seconds")


# Now Let's also create a Calculator

z = input("Choose an operator (+, -, *, /): ")

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

if z == "+":
    result = a + b
    print(round(result, 3))
elif z == "-":
    result = a - b
    print(round(result, 3))
elif z == "*":
    result = a * b
    print(round(result, 3))
elif z == "/":
    result = a / b
    print(round(result, 3))
else:
    print(f"{z} is not a valid operator , please choose from (+, -, *, /)")
