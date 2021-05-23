"""
This is the math_test package. This package contains 4 functions:
-----------------------------------------------------------
ask_question(anything, type_of_question, correct_answer)
    Type your question in place of anything. It should be in string value! Then specify the type_of_question which can be str and int. Then type the correst_answer correctly in a correct datatype!
-----------------------------------------------------------
reset_all()
    Try this function to reset all the scores!
-----------------------------------------------------------
say_score()
    Try this function to print the score obtained!
-----------------------------------------------------------
calculate_result()
    Try this function to calculate the score!
"""

questions = []
correct_answers = []
answers = []
score = 0


def ask_question(anything, type_of_question, correct_answer):
    """
    Just asks a specified question to the user and check if it is a correct answer as specified. If the answer is correct then it increases the score by 1!
    """
    global questions
    global correct_answers
    global answers
    global score
    questions.append(anything)
    correct_answers.append(correct_answer)
    answer = str(len(questions)) + ".   " + anything + ": "
    answer = input(answer)
    while len(answer) <= 0:
        print("Wrong Input Given!")
        answer = str(len(questions)) + anything
        answer = input(answer)
    if type_of_question == str:
        try:
            answer = answer.strip()
        except ValueError as error:
            print(f"Error: {error}")
    if type_of_question == int:
        try:
            answer = int(answer)
        except ValueError as error:
            print(f"Error: {error}")
    if answer == correct_answer:
        print("Correct Answer!")
        score += 1
    elif answer != correct_answer:
        print("Wrong Answer!")
        if score > 0:
            score -= 1
        else:
            print(f"Your score is {score}")
    else:
        print("Wrong Input!")
    answers.append(answer)


def reset_all():
    """
    Resets all the score and lists!
    """
    global questions
    global score
    global answers
    global correct_answers
    score = 0
    questions.clear()
    answers.clear()
    correct_answers.clear()


def say_score():
    """
    Just prints the score in the console!
    """
    print(f"Your score is {score}")


def calculate_result():
    """
    Just calculates the result!
    """
    say_score()
    print("Result:")
    for item in range(len(questions)):
        # print(item)
        print("Question " + str(item) + ". " + questions[item] + " Your answer: " + str(
            answers[item]) + " Correct Answer: " + str(correct_answers[item]))
