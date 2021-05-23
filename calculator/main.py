# Simple Calculator v1.0
# Made By Siddhesh Chavan. Visit: https://sid72020123.github.io/
# Version: 1.0
# -------------------------------------------------------- Import Modules -----------------------------------------
from tkinter import *

# Main Window
window = Tk()
window.title("Simple Calculator! v1.0")
window_height = 510
window_width = 400
window.geometry(f'{window_width}x{window_height}')

# Main_Variables
number1 = ""
number2 = ""
operator = None
answer = None
answered = "No"
label_text = ""

# Main Text
main_text = Label(window, text="Simple Calculator! v1.0", font=('Comic Sans MS', 20), fg="Red")
main_text.place(x=50, y=0)

# Enter text
enter_text = Label(window, text="Enter a number:", font=('Comic Sans MS', 15))
enter_text.place(x=100, y=50)

# Text Field
enter_field = Entry(window, width=50, borderwidth=5)
enter_field.place(x=40, y=100)


# Update Label
def update_label(text):
    global end_label
    global label_text
    global main_label_text
    label_text += str(text)
    end_label.config(text=label_text)


# Update Entry
def update_entry(num):
    global number1
    enter_field.insert(len(enter_field.get()), num)
    update_label(num)


# Clear Label
def clear_label():
    global label_text
    global end_label
    label_text = ""
    end_label.config(text="")


# Check
def check():
    global number1
    global number2
    global answer
    global label_text
    global end_label
    global answered
    number1 = enter_field.get()
    update_label(enter_field.get())
    number2 = 0
    answer = 0
    answered = "No"
    clear_label()
    update_label(number1)


# Clear
def clear():
    if answered == "No":
        enter_field.delete(0, END)
    else:
        check()


# Add
def add():
    global number1
    global operator
    number1 = enter_field.get()
    operator = "+"
    clear()
    update_label(" + ")
    # print(number1)


# Subtract
def subtract():
    global number1
    global operator
    number1 = enter_field.get()
    operator = "-"
    clear()
    update_label(" - ")
    # print(number1)


# Multiply
def multiply():
    global number1
    global operator
    number1 = enter_field.get()
    operator = "*"
    clear()
    update_label(" * ")
    # print(number1)


# Divide
def divide():
    global number1
    global operator
    number1 = enter_field.get()
    operator = "/"
    clear()
    update_label(" / ")
    # print(number1)


# Calculate
def calculate():
    global number1
    global number2
    global answer
    global answered
    number2 = enter_field.get()
    if operator == "+":
        answer = int(number1) + int(number2)
    if operator == "-":
        answer = int(number1) - int(number2)
    if operator == "*":
        answer = int(number1) * int(number2)
    if operator == "/":
        answer = int(number1) / int(number2)
    answered = "Yes"
    enter_field.delete(0, END)
    enter_field.insert(0, str(answer))
    update_label(f" = {answer}")
    clear()


# -------------------------------------------------------  Buttons: -----------------------------------------------
# 1
button_1 = Button(window, text="1", font=(20), borderwidth=5, padx=20, command=lambda: update_entry(1))
button_1.place(x=10, y=150)

# 2
button_2 = Button(window, text="2", font=(20), borderwidth=5, padx=20, command=lambda: update_entry(2))
button_2.place(x=100, y=150)

# 3
button_3 = Button(window, text="3", font=(20), borderwidth=5, padx=20, command=lambda: update_entry(3))
button_3.place(x=200, y=150)

# 4
button_4 = Button(window, text="4", font=(20), borderwidth=5, padx=20, command=lambda: update_entry(4))
button_4.place(x=10, y=200)

# 5
button_5 = Button(window, text="5", font=(20), borderwidth=5, padx=20, command=lambda: update_entry(5))
button_5.place(x=100, y=200)

# 6
button_6 = Button(window, text="6", font=(20), borderwidth=5, padx=20, command=lambda: update_entry(6))
button_6.place(x=200, y=200)

# 7
button_7 = Button(window, text="7", font=(20), borderwidth=5, padx=20, command=lambda: update_entry(7))
button_7.place(x=10, y=250)

# 8
button_8 = Button(window, text="8", font=(20), borderwidth=5, padx=20, command=lambda: update_entry(8))
button_8.place(x=100, y=250)

# 9
button_9 = Button(window, text="9", font=(20), borderwidth=5, padx=20, command=lambda: update_entry(9))
button_9.place(x=200, y=250)

# 0
button_9 = Button(window, text="0", font=(20), borderwidth=5, padx=20, command=lambda: update_entry(0))
button_9.place(x=10, y=300)

# Clear
button_clear = Button(window, text="Clear All", font=(20), borderwidth=5, padx=40, command=clear)
button_clear.place(x=100, y=300)

# Add_button
button_add = Button(window, text="+", font=(20), borderwidth=5, padx=20, command=add)
button_add.place(x=300, y=150)

# Subtract_button
button_subtract = Button(window, text="-", font=(20), borderwidth=5, padx=20, command=subtract)
button_subtract.place(x=300, y=200)

# Multiply_button
button_multiply = Button(window, text="*", font=(20), borderwidth=5, padx=20, command=multiply)
button_multiply.place(x=300, y=250)

# Divide_button
button_divide = Button(window, text="/", font=(20), borderwidth=5, padx=20, command=divide)
button_divide.place(x=300, y=300)

# Answer_button
button_answer = Button(window, text="=", font=(20), borderwidth=5, padx=160, command=calculate)
button_answer.place(x=10, y=350)

# Labels
end_label = Label(text="", font=(20), bg="black", fg="white")
end_label.place(x=10, y=400)

credit_label = Label(text="Created By: Siddhesh Chavan", font=(15))
credit_label.place(x=10, y=450)

credit_label1 = Label(text="Website: https://Sid72020123.github.io/", font=(15))
credit_label1.place(x=10, y=480)

# Mainloop
window.resizable(0, 0)
window.mainloop()
