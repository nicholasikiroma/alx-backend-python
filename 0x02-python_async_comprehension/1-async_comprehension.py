#!/usr/bin/env python3
"""
Write a coroutine called
async_generator that takes no arguments.
The coroutine will loop 10 times,
each time asynchronously wait 1 second,
then yield a random number between 0 and 10.
Use the random module.
"""
import random
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """return list of 10 random numbers"""
    numbers = [i async for i in async_generator()]
    return numbers
