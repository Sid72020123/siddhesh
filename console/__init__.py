"""
This is the console package.
It contains many functions such as say() which prints something in the console! Use the ask() function to ask a question! Use ask_if() function to ask if a person has the specified thing! Use the display() function to display a shape!
"""


def say(something):
    """
    Just to print something in the console!
    """
    print(something)


def ask(anything, min_length, max_length, value, type_of_sentence):
    """
    Asks a question in the console and asks the question until the length of the users answer is more than min_length and less than max_length and also converts the value to a specified format and returns the value!
    """
    answer = input(anything)
    while max_length > len(answer) and min_length >= len(answer):
        print("Wrong " + value + "! It should be minimum " + str(min_length) + " and maximum " + str(
            max_length) + " characters!")
        answer = input(anything)
    if len(answer) <= 0:
        say("Wrong Input!")
    else:
        if type_of_sentence == "string":
            global string
            string = answer
            string = string.strip()
            string = string[0].upper() + string[1:].lower()
            return string
        if type_of_sentence == "integer":
            global integer
            integer = answer
            integer = integer.strip()
            try:
                integer = int(integer)
            except ValueError as error:
                raise ValueError(f"Error: {error}")
            return integer


def ask_if(statement):
    """
    Asks if a user can, have, and do a thing!
    """
    if str(ask("Do you have a " + statement + "?(y/n) ", 0, 3, statement, "string")) == "Y":
        say("Ok")
        say("Oh! So your " + statement + "'s name is " + str(
            ask("Enter your " + statement + "'s name: ", 1, 20, statement + "'s name", "string")))
    if string == "N":
        say("Ok")


def ask_is(anything, min_length, max_length, value, type_of_sentence):
    """
    Asks a question in the console and asks the question until the length of the users answer is more than min_length and less than max_length and also converts the value to a specified format and returns the value!
    """
    answer = input(anything)
    while max_length > len(answer) and min_length >= len(answer) and (answer.upper() == "Y" or answer.upper() == "N"):
        print("Wrong " + value + "! It should be minimum " + str(min_length) + " and maximum " + str(
            max_length) + " characters and (y or n)!")
        answer = input(anything)
    if len(answer) <= 0:
        say("Wrong Input!")
    else:
        if type_of_sentence == "string":
            global string
            string = answer
            string = string.strip()
            string = string[0].upper() + string[1:].lower()
            return string
        if type_of_sentence == "integer":
            global integer
            integer = answer
            integer = integer.strip()
            try:
                integer = int(integer)
            except ValueError as error:
                print(f"Error: {error}")
            return integer


def ask_if_is(statement):
    """
    Asks if a user can, have, and do a thing!
    """
    if str(ask_is("Do you have a " + statement + "?(y/n) ", 0, 3, statement, "string")) == "Y":
        say("Ok")
        say("Oh! So your " + statement + "'s name is " + str(
            ask("Enter your " + statement + "'s name: ", 1, 20, statement + "'s name", "string")))
    else:
        say("Wrong Input!")
    if string == "N":
        say("Ok")


def display(shape, style, size):
    """
    Draws the specified shape in the console!
    """
    if shape == "not_equal_triangle":
        for i in range(size + 1):
            print(style * i)
    if shape == "square":
        i = 0
        while i < size:
            print(style + " ", end='')
            i += 1
        for i in range(size + 1):
            print(style + "  " * (size + 1) + style)
        i = 0
        while i < size:
            print(style + " ", end='')
            i += 1
        print()
    if shape == "line":
        print(style * size)
    if shape == "rectangle":
        i = 0
        while i < size:
            print(style + "  ", end='')
            i += 1
        for i in range(size + 1):
            print(style + "   " * (size + 1) + style)
        i = 0
        while i < size:
            print(style + "  ", end='')
            i += 1
        print()
    if shape == "equal_triangle":
        for i in range(size + 1):
            print(" " * (size - i) + style * i + style * i)
    if shape == "filled_rectangle":
        for i in range(size):
            print(style * size)
    if shape == "filled_square":
        for i in range(size):
            print(style * size + style * 5)
