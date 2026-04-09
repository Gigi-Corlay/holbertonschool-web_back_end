#!/usr/bin/env python3
"""
Module that defines an asynchronous generator that yields random numbers.
"""

import asyncio
import random


async def async_generator():
    """
    Asynchronously generates random numbers.

    This coroutine loops 10 times, waits 1 second asynchronously
    on each iteration, and yields a random float between 0 and 10.

    Yields:
        float: A random number between 0 et 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
