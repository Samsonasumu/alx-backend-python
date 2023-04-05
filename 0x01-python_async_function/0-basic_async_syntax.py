#!/usr/bin/env python3
"""
asynchronous coroutine that takes integer argument,return random float value
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """returns random float value"""
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
