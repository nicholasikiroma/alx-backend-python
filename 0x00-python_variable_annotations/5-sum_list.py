#!/usr/bin/env python3
"""type-annotated function which
takes a list input_list of floats
as argument and returns
their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """returns sum of list"""
    value = 0
    for item in input_list:
        value += item
    return value
