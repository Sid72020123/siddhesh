"""
Package to start a simple GUI calculator in Python!
"""


def start_calculator():
    """
    Starts the GUI calculator!
    """
    print("Starting Calculator........")
    try:
        print("Calculator Started!")
        import siddhesh.calculator.main
    except ModuleNotFoundError:
        print("Oops! Calculator Not Found!")
