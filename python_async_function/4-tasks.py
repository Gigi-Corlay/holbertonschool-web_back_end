#!/usr/bin/env python3
"""
Concurrent coroutine that runs task_wait_random n times
and returns delays in ascending order of completion
"""
import asyncio
from typing import List

# Import task_wait_random depuis 3-tasks.py
task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Launch task_wait_random n times with max_delay and return list of results
    in ascending order of completion.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = []
    for completed_task in asyncio.as_completed(tasks):
        result = await completed_task
        results.append(result)
    return results
