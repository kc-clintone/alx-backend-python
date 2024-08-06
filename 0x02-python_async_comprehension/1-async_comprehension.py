#!/usr/bin/env python3
"""
Async Comprehensions -
    Import async_generator from the previous task and then write
    a coroutine called async_comprehension that takes no args.
"""

import typing

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """
    Creates a list of 10 numbers from a async_generator.
    """
    return [number async for number in async_generator()]
