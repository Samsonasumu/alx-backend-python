#!/usr/bin/env python3
"""
spawn multiple coroutines & return the list of all delays in ascending order
"""
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
     return list of all delays which is a float values
    """
    # Define an empty list called delays to store the float values
    delays: List[float] = []
    # Define an empty list called tasks to store the tasks
    tasks: List = []

    for _ in range(n):
        # Create a new task using wait_random() and add it to tasks
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)
        tasks.append(task)

    # Loop over the tasks as they are completed
    for task in asyncio.as_completed(tasks):
        # Wait for the task to complete and store the result in delay
        delay = await task
        # Add the delay value to the delays list
        delays.append(delay)

    # Sorted the delays in ascending order
    return sorted(delays)
