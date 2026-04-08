#!/usr/bin/env python3
"""
Module that provides a function to create a key-value pair with a squared value.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with a string and the square of a number.

    Args:
        k (str): The key of the tuple.
        v (Union[int, float]): The number to square.

    Returns:
        Tuple[str, float]: A tuple containing k and the square of v as a float.
    """
    return (k, float(v ** 2))