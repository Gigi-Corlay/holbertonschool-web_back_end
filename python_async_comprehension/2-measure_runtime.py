#!/usr/bin/env python3
"""
Measures the runtime of running async_comprehension 4 times in parallel.
"""

import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Runs async_comprehension 4 times in parallel and returns execution time.
    """
    start = time.time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    return time.time() - start
