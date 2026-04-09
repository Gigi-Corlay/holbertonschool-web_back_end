#!/usr/bin/env python3
"""
Function to spawn multiple task_wait_random coroutines and collect
their results as they complete in ascending order.
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn n tasks using task_wait_random with max_delay.
    Collect results as they complete to keep ascending order.

    Args:
        n: number of tasks
        max_delay: maximum delay for each task

    Returns:
        List of delays in ascending order
    """
    tasks: List[asyncio.Task] = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []

    for task in asyncio.as_completed(tasks):
        delays.append(await task)

    return delays
