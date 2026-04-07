#!/usr/bin/env python3
"""
Allows you to specify a list with several possible types (Union[int, float]).
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Return the sum of a list containing ints and floats.
    """
    return sum(mxd_lst)
