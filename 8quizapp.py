# This is a quiz app where the app gives questions and the user answers , then a score is given after , with highest score and difficulty level

import json


def load_questions_and_highscore(difficulty):
    filename = f"{difficulty}_questions.json"
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        questions = data["questions"]
        highscore = data["highscore"]
        return questions, highscore
    except FileNotFoundError:
        print(f"No questions found for {difficulty} difficulty.")
        return [], 0


def save_highscore(difficulty, new_highscore):
    filename = f"{difficulty}_questions.json"
    with open(filename, "r") as file:
        data = json.load(file)
    data["highscore"] = new_highscore
    with open(filename, "w") as file:
        json.dump(data, file, indent=2)


name = input("What is your name: ")
print(f"Welcome to the Quiz app {name}")

age = int(input("And how old are you: "))


if age <= 10:
    difficulty = "easy"
elif age <= 18:
    difficulty = "medium"
elif age > 18:
    difficulty = "hard"
else:
    print(f"{age} is an invalid input")

questions, highscore = load_questions_and_highscore(difficulty)

score = 0

for q in questions:
    user_answer = input(q["question"] + " ")
    if user_answer.strip().lower() == q["answer"].strip().lower():
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is: {q['answer']}\n")

print(f"Quiz finished! Your score is {score} out of {len(questions)}.")
print(f"The highest score for {difficulty} difficulty is {highscore}.")

if score > highscore:
    print(f"Congratulations {name}! You set a new high score!")
    save_highscore(difficulty, score)
