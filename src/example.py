from typing import List, Set, Tuple, Dict

import numpy as np
import pandas as pd


def add_simple(a, b):
    return a + b


def add_with_type_hints(a: int, b: int) -> int:
    return a + b


def combine_with_docstring(a: int, b: int) -> List[int]:
    """Conbine two integers into a list.

    Args:
        a (int): integer to be combined.
        b (int): integer to be combined.

    Returns:
        List[int]: A list of conbined integer.
    """
    return [a, b]


def combine_with_example(a: int, b: int) -> List[int]:
    """Conbine two integers into a list.

    Args:
        a (int): integer to be combined.
        b (int): integer to be combined.

    Returns:
        List[int]: A list of conbined integer.

    Examples:
    >>> combine_with_example(1, 2)
    [1, 2]
    """
    return [a, b]