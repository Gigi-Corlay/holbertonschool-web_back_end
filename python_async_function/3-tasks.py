#!/usr/bin/env python3
"""
Return an asyncio.Task wrapping wait_random
"""
import asyncio

"""
Import wait_random depuis 0-basic_async_syntax
"""
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task that wraps wait_random(max_delay)
    """
    return asyncio.create_task(wait_random(max_delay))
