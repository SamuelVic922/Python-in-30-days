# I am building a Tip generator for todays project (05/08/2025)

bill = float(input("What id your total bill: $ "))

print("Note , Your tip is 15% of the total bill")

y = input("Do you wish to go on(Yes/No): ")


def calcbill():
    totaltip = bill * 0.15
    print(f"Your tip is ${round(totaltip, 2)} cents")
    totalbill = totaltip + bill
    print(f"Your total bill including tip is ${totalbill} cents")


if (y == "Yes"):
    calcbill()
elif (y == "No"):
    print("Payment cancelled")
else:
    print(f"{y} is not a valid answer")
