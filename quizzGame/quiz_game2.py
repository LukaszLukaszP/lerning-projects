from Question import Question
question_prompts = [
    "What color are bannanas?\n(a) yellow\n(b) red\n(c) black\n\n",
    "What color are oranges?\n(a) yellow\n(b) orange\n(c) black\n\n",
    "What color are strawberries?\n(a) orange\n(b) red\n(c) black\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer =  input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got", str(score) + "/" + str(len(questions)))

run_test(questions)