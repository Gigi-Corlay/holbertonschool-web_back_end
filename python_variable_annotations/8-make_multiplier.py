#!/usr/bin/env python3
"""
Module that provides a function to create a multiplier function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that takes a float and
        returns it multiplied by multiplier.
    """

    def multiply(x: float) -> float:
        """
        Multiply a float by the captured multiplier.

        Args:
            x (float): The number to multiply.

        Returns:
            float: The result of x multiplied by multiplier.
        """
        return x * multiplier

    return multiply
