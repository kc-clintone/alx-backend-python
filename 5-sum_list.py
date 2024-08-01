#!/usr/bin/env python3
"""
Intro to complex types - list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    This calculates the sum of a list of floating-point numbers.
    """
    return float(sum(input_list))
