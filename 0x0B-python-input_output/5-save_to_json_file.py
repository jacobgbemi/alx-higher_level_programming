#!/usr/bin/python3
"""
Contains function that writes Python obj to file using JSON represenation
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes Python obj to file using JSON represenation
    Args:
        my_obj: python object
        filename: file
    """

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
