#!/usr/bin/env python3
"""
Creating Async Generator using random module
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[
        float, None, None]:
    """
    Corotine which asynchronously yields integers randomly between (0,10).
    """
    try:
        for number in range(10):
            await asyncio.sleep(1)
            yield random.uniform(0, 10)
    except GeneratorExit:
        pass
