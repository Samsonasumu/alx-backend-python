#!/usr/bin/env python3
"""
 measures the total execution time
"""
import asyncio
import time
from typing import List


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int = 0, max_delay: int = 10) -> float:
    """
    the function measures the total time used for execution
    wait_n. return value is a float.
    """

    # Get the start time
    start_time = time.perf_counter()
    # Call the wait_n coroutine to get the delays
    asyncio.run(wait_n(n, max_delay))
    # Get the end time
    end_time = time.perf_counter()
    # Total execution time
    total_time = (end_time - start_time) / n

    # return value: average execution time per task
    return total_time
