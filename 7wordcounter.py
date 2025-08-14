# This is a Word Counter app built today(13/08/25)

print("Hi , Welcome to the Word Counter App")

print("\n")


def count_words(wordinput):
    return len(wordinput)


wordinput = input("Please input the word you want to count: ")
print("______________________________________________")
words_no = count_words(wordinput)
print(f"The total number of words inputed is: {words_no} ")
