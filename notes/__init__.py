"""
This package contains program to keep notes.
Call the new_file(location, name) function to create a new file. This also contains open_file(location, name) and write_in_file(location, name, something) functions!
"""

import os


def new_file(location, name):
    """
    Just creates a new .txt file with the given name in the given location!
    """
    file = open(str(location + name) + ".txt", "a")
    file.close()


def open_file(location, name):
    """
    Just opens a specified file with the name and the specified location!
    """
    file = location + name
    os.system(f'start {file}.txt')


def write_in_file(location, name, something):
    """
    Just opens a specified file with the name and the specified location and writes a text in that file!
    """
    file = open(str(location + name) + ".txt", "a")
    file.write("\n" + str(something))
    file.close()
