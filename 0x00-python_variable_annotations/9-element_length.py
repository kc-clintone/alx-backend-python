#!/usr/bin/env python3
"""
Iterable object
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This computes the length of a list of sequences.
    """
    return [(j, len(j)) for j in lst]
