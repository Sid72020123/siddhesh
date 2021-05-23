"""
Package to print the tables form 1 to a given number.
"""


def print_table(table=10):
    """
    Just enter the number to print the tables from 1 to given number!
    """
    if not int(table) <= 0:
        print("Tables from 1 to " + str(table))
        to_table = int(table)
        num1 = 1
        num2 = 1
        while num1 <= 10:
            num2 = 1
            while num2 <= to_table:
                print(f"\t" + str((num1 * num2)), end='')
                num2 = num2 + 1
            print()
            num1 = num1 + 1

    else:
        raise ValueError("The number should be more than 0")
