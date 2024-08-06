#!/usr/bin/env python3
"""
Async Generator
"""
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """
    Loops 10 times asynchronously
    wait for 1 second then yields a random number between 0 - 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
