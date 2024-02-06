#!/usr/bin/python3
"""
This module contains a function that reads from a file
"""


def read_file(filename=""):
    """
    function that reads from a file

    args:
        filename: name of file

    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
