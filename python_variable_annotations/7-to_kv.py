#!/usr/bin/env python3
"""
Module that provides a function to create
a key-value pair with a squared value.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns:
        Tuple[str, float]: A tuple containing k and the square of v as a float.
    """
    return (k, v ** 2)
