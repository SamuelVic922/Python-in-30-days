
# This is a code to check if the user is eligible to drive

x = int(input("What age are you: "))
y = input("What is your gender: ")

kidtitle = ""

if x > 18:
    if y == "Male":
        title = "Sir"
    elif y == "Female":
        title = "Ma"
    else:
        title = ""
    print(f"You are eligible to drive {title}")
elif x == 18:
    if y == "Male":
        kidtitle = "bruh"
    else:
        kidtitle = "sis"
    print(f"Right on time {kidtitle}, you are eligible to drive")
elif x == 17:
    print(f"You are not eligible to drive yet , wait 1 more year")
else:
    print("You are not eligible to drive kiddo")
