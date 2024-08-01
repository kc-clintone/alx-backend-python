#!/usr/bin/env python3
"""
Intro to complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This creates a multiplier function.
    """
    return lambda x: x * multiplier
