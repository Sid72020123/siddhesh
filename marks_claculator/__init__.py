"""
This package contains program to calculate marks.
Just contains a start() function to start the marks_calculator!
"""


def start():
    """
    Just starts the marks_calculator script!
    """
    # Name
    name = input("Enter your name: ")
    name = name.strip()
    while len(name) <= 1:
        print("Wrong Name!")
        name = input("Enter your name: ")
        name = name.strip()
    name = name[0].upper() + name[1:].lower()

    # Age
    age = input("Enter your age: ")
    age = age.strip()
    while len(age) <= 1:
        print("Wrong Age!")
        age = input("Enter your age: ")
        age = age.strip()
    try:
        age = int(age)
    except ValueError as error:
        print(f"Error: {error}")

    # Total_Subjects
    Total_Subjects = input("Number of total subjects: ")
    # print(not type(Total_Subjects) != None and  isinstance(Total_Subjects,str) and not isinstance(Total_Subjects,int))
    while len(Total_Subjects) <= 0:
        print("Wrong Value!")
        Total_Subjects = input("Number of total subjects: ")
        Total_Subjects = Total_Subjects.strip()
    try:
        Total_Subjects = int(Total_Subjects)
    except ValueError as error:
        print(f"Error: {error}")

    # M_Subjects
    M_Subjects = input("Total mark of 1 subject: ")
    while len(M_Subjects) <= 0:
        print("Wrong Value!")
        M_Subjects = input("Total mark of 1 subject: ")
        M_Subjects = M_Subjects.strip()
    try:
        M_Subjects = int(M_Subjects)
    except ValueError as error:
        print(f"Error: {error}")

    # Main Calculator
    num_of_subjects = 1
    total_list = []
    num_list = []
    text_list = []
    while num_of_subjects < Total_Subjects + 1:
        # print(text_list)
        Total_Str = "Enter the name of " + str(num_of_subjects) + " subject (minimum 3 letters and maximum 5 letters): "
        subject_name = input(Total_Str)
        while len(subject_name) < 3 or len(subject_name) > 5:
            print(
                "Wrong Input! Must be of minimum 3 letters and maximum 5 letters, also the names of the subject should be different!")
            subject_name = input(Total_Str)
            subject_name = subject_name.strip()
        subject_name = subject_name[0].upper() + subject_name[1:].lower()
        total_list.append(subject_name)
        text_list.append(subject_name)
        Total_Str = "Enter the marks you got of " + str(subject_name) + ": "
        subject_mark = input(Total_Str)
        while len(subject_mark) < 0 or int(subject_mark) > M_Subjects:
            print("Wrong Value! Must be less than maximum value of each subject(" + str(M_Subjects) + ")")
            subject_mark = input(Total_Str)
            subject_mark = subject_mark.strip()
        subject_mark = int(subject_mark)
        total_list.append(subject_mark)
        num_list.append(subject_mark)
        num_of_subjects = num_of_subjects + 1
        # print(num_list)
        # print(num_list[num_of_subjects])

    i = 0
    all_sum = 0
    while i < len(num_list):
        # print(i)
        all_sum = all_sum + num_list[i]
        i = i + 1
    i = 0
    # print(all_sum)
    result = ((all_sum / (M_Subjects * Total_Subjects)) * 100)
    # print(result)
    print("        ☆Subjects☆" + "            " + "                 ☆Marks☆")
    least_space = 3
    while i < len(text_list):
        if len(text_list[i]) < least_space:
            least_space = len(text_list[i])
        i = i + 1
    # print(least_space)
    i = 0
    while i < len(total_list):
        space = len(total_list[i])
        space = (" " * (space - 2))
        # print(i)
        print("         》" + str(total_list[i]) + space + "---------------------------》" + str(
            total_list[i + 1]) + "/" + str(M_Subjects))
        i = i + 2
    total = all_sum
    print("Total of all subjects: " + str(total) + "/" + str(M_Subjects * Total_Subjects))
    print("Average of all subjects is: " + str(all_sum / Total_Subjects))
    print(name + ",your result is " + str(round(result)) + "%")
