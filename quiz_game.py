def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print("----")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter (A, B, C or D): ")
        guess = guesses.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num = question_num + 1

    display_score(correct_guesses, guess)


def check_answer(answer, guess):
    if answer == guess:
        print("correct")
        return 1
    else:
        print("wrong")
        return 0


def display_score(correct_guesses, guesses):
    print("-----")
    print("Results")
    print("--------")
    print("Answers: ", end="")


def play_again():
    pass


questions = {
    "Who created python?: ": "A",
    "What  year was Python created?: ": "B",
    "question 3: ": "C",
    "question 4: ": "A"
}

options = [["A. Guido van Rossum", "B. sadfgs", "C. fadgfgs", "D. fadgfsas"],
           ["qweqwe222", "B. 1991", "C. fad222fgs", "D. fadg222sas"],
           ["sad333", "B. s3333fgs", "C. fad333gs", "D. fad333fsas"],
           ["asfsdf444", "B. sa444gs", "C. fa444fgs", "D. fa444sas"]]

new_game()
