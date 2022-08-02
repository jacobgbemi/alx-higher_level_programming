#!/usr/bin/python3
"""
Contains function that returns python data structure from JSON string
"""
import json


def from_json_string(my_str):
    """Returns python data structure from JSON string
    Args:
        my_str: json string representation
    Return:
        python object
    """

    return json.loads(my_str)
