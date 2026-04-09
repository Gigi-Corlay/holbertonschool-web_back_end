#!/usr/bin/env python3
"""
Concurrent coroutine that runs wait_random n times
and returns delays in ascending order of completion
"""
import asyncio
from typing import List

# Import depuis 0-basic_async_syntax.py avec __import__
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Launch wait_random n times with max_delay and return list of results
    in ascending order of completion (without using sort()).
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    results = []
    for completed_task in asyncio.as_completed(tasks):
        result = await completed_task
        results.append(result)
    return results
