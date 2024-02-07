#!/usr/bin/python3
"""Module contains a function that appends to a text file
"""


def append_write(filename="", text=""):
    """ Function that appends to a text file

    Args:
        filename: name of file
        text: text to append

    Raises
        Exception: when the file can't be opened

    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
