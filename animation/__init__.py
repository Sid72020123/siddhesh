"""
This package contains functions to create animations in the console.
------------------------------------------------------------------------
1. animate_triangle(type, style, interval, size)
    First to show a animated triangle you have to first specify the type of the triangle. The type can be "equal" or "not_equal". Make sure that you type the spellings correctly! After that there is style. The style should be a string. After that is interval, you should give the correct interval in integer only and for size you should give it an integer value!
------------------------------------------------------------------------
2. animate_square(type="filled", style="*", interval=0.1, size=10)
    First to show a square  you have to first specify the type of the square. The type can be "filled" or "not_filled". Make sure that you type the spellings correctly! After that there is style. The style should be a string. After that is interval, you should give the correct interval in integer only and for size you should give it an integer value!
------------------------------------------------------------------------
3. animate_rectangle(type="filled", style="*", interval=0.1, size=10)
    First to show a animated rectangle you have to first specify the type of the rectangle. The type can be "filled" or "not_filled". Make sure that you type the spellings correctly! After that there is style. The style should be a string. After that is interval, you should give the correct interval in integer only and for size you should give it an integer value!
------------------------------------------------------------------------
4. animate_line(style="*", size=10, interval=0.1)
    First to show a animated line, there is style. The style should be a string. After that is interval, you should give the correct interval in integer only and for size you should give it an integer value!
------------------------------------------------------------------------
5. animate_text(something, interval=0.1)
    First to show a animated text you have to animate. The text should be in string format! After that you have to specify the interval, you should give the correct interval in integer only!
"""
import time


def animate_triangle(type="equal", style="*", interval=0.1, size=10):
    """
    animate_triangle(type, style, interval, size)
    First to show a animated triangle you have to first specify the type of the triangle. The type can be "equal" or "not_equal". Make sure that you type the spellings correctly! After that there is style. The style should be a string. After that is interval, you should give the correct interval in integer only and for size you should give it an integer value!
    """
    try:
        if type == "not_equal":
            for i in range(size + 1):
                try:
                    print(style * i)
                except TypeError:
                    raise TypeError("The 'style' should be in string format!")
                try:
                    time.sleep(interval)
                except TypeError:
                    raise TypeError("The 'interval' should be in integer format!")
    except TypeError:
        raise TypeError("The 'size' should be in integer format!")

    if type == "equal":
        try:
            for i in range(size + 1):
                try:
                    print(" " * (size - i) + style * i + style * i)
                except TypeError:
                    raise TypeError("The 'style'  should be in string format!")
                try:
                    time.sleep(interval)
                except TypeError:
                    raise TypeError("The 'interval' should be in integer format!")
        except TypeError:
            raise TypeError("The 'size' should be in integer format!")


def animate_square(type="filled", style="*", interval=0.1, size=10):
    """
    animate_square(type="filled", style="*", interval=0.1, size=10)
    First to show a square  you have to first specify the type of the square. The type can be "filled" or "not_filled". Make sure that you type the spellings correctly! After that there is style. The style should be a string. After that is interval, you should give the correct interval in integer only and for size you should give it an integer value!
    """
    if type == "filled":
        try:
            for i in range(size):
                try:
                    print(style * size + style * 5)
                except TypeError:
                    raise TypeError("The 'style' should be in string format!")
                try:
                    time.sleep(interval)
                except TypeError:
                    raise TypeError("The 'interval' should be in integer format!")
        except TypeError:
            raise TypeError("The 'size' should be in integer format!")
    if type == "not_filled":
        try:
            i = 0
            while i < size:
                try:
                    print(style + " ", end='')
                except TypeError:
                    raise TypeError("The 'style' should be in string format!")
                i += 1
                try:
                    time.sleep(interval)
                except TypeError:
                    raise TypeError("The 'interval' should be in integer format!")
            for i in range(size + 1):
                try:
                    print(style + "  " * (size + 1) + style)
                except TypeError:
                    raise TypeError("The 'style' should be in string format!")
                try:
                    time.sleep(interval)
                except TypeError:
                    raise TypeError("The 'interval' should be in integer format!")
            i = 0
            while i < size:
                try:
                    print(style + " ", end='')
                except TypeError:
                    raise TypeError("The 'style' should be in string format!")
                i += 1
                try:
                    time.sleep(interval)
                except TypeError:
                    raise TypeError("The 'interval' should be in integer format!")
            print()
        except TypeError:
            raise TypeError("The 'size' should be in integer format!")


def animate_rectangle(type="filled", style="*", interval=0.1, size=10):
    """
    animate_rectangle(type="filled", style="*", interval=0.1, size=10)
    First to show a animated rectangle you have to first specify the type of the rectangle. The type can be "filled" or "not_filled". Make sure that you type the spellings correctly! After that there is style. The style should be a string. After that is interval, you should give the correct interval in integer only and for size you should give it an integer value!
    """
    if type == "not_filled":
        i = 0
        try:
            while i < size:
                try:
                    print(style + "  ", end='')
                except TypeError:
                    raise TypeError("The 'style' should be in string format!")
                i += 1
                try:
                    time.sleep(interval)
                except TypeError:
                    raise TypeError("The 'interval' should be in integer format!")
            for i in range(size + 1):
                try:
                    print(style + "   " * (size + 1) + style)
                except TypeError:
                    raise TypeError("The 'style' should be in string format!")
                try:
                    time.sleep(interval)
                except TypeError:
                    raise TypeError("The 'interval' should be in integer format!")
            i = 0
            while i < size:
                try:
                    print(style + "  ", end='')
                except TypeError:
                    raise TypeError("The 'style' should be in string format!")
                i += 1
                try:
                    time.sleep(interval)
                except TypeError:
                    raise TypeError("The 'interval' should be in integer format!")
            print()
        except TypeError:
            raise TypeError("The 'size' should be in integer format!")
    if type == "filled":
        try:
            for i in range(size):
                try:
                    print(style * size)
                except TypeError:
                    raise TypeError("The 'style' should be in string format!")
                try:
                    time.sleep(interval)
                except TypeError:
                    raise TypeError("The 'interval' should be in integer format!")
        except TypeError:
            raise TypeError("The 'size' should be in integer format!")


def animate_line(style="*", size=10, interval=0.1):
    """
    animate_line(style="*", size=10, interval=0.1)
    First to show a animated line, there is style. The style should be a string. After that is interval, you should give the correct interval in integer only and for size you should give it an integer value!
    """
    i = 0
    try:
        while i < size:
            print(style, end='')
            try:
                time.sleep(interval)
            except TypeError:
                raise TypeError("The 'interval' should be in integer format!")
            i += 1
        print()
    except TypeError:
        raise TypeError("The 'size' should be in integer format!")


def animate_text(something, interval=0.1):
    """
    animate_text(something, interval=0.1)
    First to show a animated text you have to animate. The text should be in string format! After that you have to specify the interval, you should give the correct interval in integer only!
    """
    i = 0
    try:
        while i < len(something):
            try:
                print(something[i], end='')
            except TypeError:
                raise TypeError("The text 'something' should be in integer format!")
            try:
                time.sleep(interval)
            except TypeError:
                raise TypeError("The 'interval' should be in integer format!")
            i += 1
        print()
    except TypeError:
        raise TypeError("The text 'something' should be in integer format!")


def animate_special_text(something, interval):
    """
    Don't use this function in your code! This function is for the name_processor package!
    """
    i = 0
    try:
        while i < len(something):
            try:
                print(something[i], end='')
            except TypeError:
                raise TypeError("The text 'something' should be in integer format!")
            try:
                time.sleep(interval)
            except TypeError:
                raise TypeError("The 'interval' should be in integer format!")
            i += 1
        print("", end='')
    except TypeError:
        raise TypeError("The text 'something' should be in integer format!")
