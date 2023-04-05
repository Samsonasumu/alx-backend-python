#!/usr/bin/env python3
"""
Alteration of the code from wait_n into a new function task_wait_n
"""
import asyncio
from typing import List


async def task_wait_random(max_delay: int) -> int:
    """
    Coroutine awaits for a random delay given the range of maximun_delay second
    """
    await asyncio.sleep(max_delay)
    return max_delay


async def task_wait_n(n: int, max_delay: int) -> int:
    """
    This function is similar to wait_n but altered    
    """
    tasks = [asyncio.create_task(task_wait_random(max_delay)) for i in range(n)]
    results = await asyncio.gather(*tasks)
    return results

