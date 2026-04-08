#!/usr/bin/env python3
"""
Module that provides a function to compute the sum of a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Compute the sum of a list of floats.

    Args:
        input_list (List[float]): The list of float numbers.

    Returns:
        float: The sum of all elements in input_list.
    """
    return sum(input_list)
