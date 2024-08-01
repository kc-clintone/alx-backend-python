#!/usr/bin/env python3
"""
More involved type annotations
"""
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Dfn = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Dfn = None) -> Res:
    """
    This retrieves a value from a dict using a given key.
    """
    if key in dct:
        return dct[key]
    else:
        return default
