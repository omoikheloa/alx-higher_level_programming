#!/usr/bin/python3
""" Module contains a function that returns the 
JSON representation of an object
"""
import json


def to_json_string(my_obj):
    """
    Function that returns the JSON representation of an object

    Args:
        my_obj: object

    Raises:
        exception: when the oject can't be encoded

    """
    return json.dumps(my_obj)
