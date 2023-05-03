#!/usr/env python3
"""measure_runtime should measure
the total runtime and return it."""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """return total runtime"""
    start = time.time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    total_time = time.time() - start
    return total_time
