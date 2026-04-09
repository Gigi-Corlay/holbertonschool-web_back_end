#!/usr/bin/env python3
"""
Module that defines a coroutine using async comprehension to collect random numbers
from an asynchronous generator.
"""

async_generator = __import__('0-async_generator').async_generator
from typing import List


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers asynchronously using async comprehension.

    Returns:
        List[float]: A list containing 10 random numbers.
    """
    return [number async for number in async_generator()]
