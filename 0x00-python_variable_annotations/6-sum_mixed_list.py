#!/usr/bin/env python3
"""type-annotated function which
takes a list input_list of floats
as argument and returns
their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_list:
                   List[Union[int, float]) -> float:
    """returns sum of list"""
    value = 0
    for item in input_list:
        value += item
    return value
