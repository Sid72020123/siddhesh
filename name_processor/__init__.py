"""This package contains functions to process a name in the console. 1. process_name(name="Siddhesh"): Use the above
statement to process a name. The initial value of the name is "Siddhesh", the creator of this module! You can write
your own name too! """
from siddhesh import animation as sid


def process_name(name="Siddhesh"):
    """
    process_name(name="Siddhesh"): Use the above
statement to process a name. The initial value of the name is "Siddhesh", the creator of this module! You can write
your own name too!
    """
    try:
        name = name.strip()
    except AttributeError:
        raise AttributeError("The name should be in string format!")
    process_indicator = 0
    if len(name) <= 0 or len(name) <= 2:
        print(f"Processing name: {name} : ", end='')
        while process_indicator < 10:
            sid.animate_special_text("*", 0.1)
            process_indicator += 1
        print(f"\nName Error: '{name}' is not a correct name!")
    if name.isnumeric():
        print(f"Processing name: {name} : ", end='')
        while process_indicator < 10:
            sid.animate_special_text("*", 0.1)
            process_indicator += 1
        print(f"\nName Error: Name: '{name}' cannot be a number!")
    if not (len(name) <= 0 or len(name) <= 2 or name.isnumeric()):
        print(f"Processing name: {name} : ", end='')
        while process_indicator < 10:
            sid.animate_special_text("*", 0.1)
            process_indicator += 1
        print("\nCalculating results..........")
        sid.animate_triangle("equal", "#", 0.1, 20)
        sid.animate_square("filled", "*", 0.1, 20)
        sid.animate_rectangle("filled", ".", 0.1, 20)
        name_length = len(name)
        print("Here are the results: ")
        print(f"Your name is {name[0].upper() + name[1:].lower()}.")
        print(f"Then length(including the spaces in between) of your name is {name_length}!")
        print(f"The first letter of your name is {name[0].upper()}!")
        print(f"The last letter of your name is {name[-1].lower()}!")
        if name[0].upper() == name[0]:
            print("Good! You have wrote the name correctly with a capital letter in the beginning!")
        else:
            print("You should try to write the first letter of a name in capital letters!")
