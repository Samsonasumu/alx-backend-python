#!/usr/bin/env python3
"""
Async Comprehension and Parallel execution using asyncio.gather
"""
import asyncio
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure the total runtime and return it.
    """
    start_time = time.perf_counter()
    my_list = [asyncio.create_task(async_comprehension()) for i in range(4)]
    result = await asyncio.gather(*my_list)
    elapse = time.perf_counter()
    total_time = time.perf_counter() - start_time
    return total_time
