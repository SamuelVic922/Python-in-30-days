xname = input("What is your name: ")
print("Hello to you " + xname + "")

y = input("Are you feeling happy today: ")
if y == "Yes":
    print("I am glad to hear that")
else:
    x = input("I'm sorry to hear about that, Would you like to talk about it?: ")
    if x == "Yes":
        x1 = input("Wonderful , I'm listening: ")
        print("I'm so sorry to hear that , but you need to get over it and be happy , I wish you well and I love you")
    elif x == "No":
        print("Oh , Okay , It hurt a bit , But please speak to someone , Or GOD")
    else:
        print(
            "I do not recognize Your Input , please answer Yes/No in the same format shown")

print(f"Thanks for using Our App {xname} ")
