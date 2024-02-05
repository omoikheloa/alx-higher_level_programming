#!/usr/bin/python3
"""
This module contains is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """True if the object is an instance of or inherited from a_class otherwise False."""
    return(isinstance(obj,a_class))
