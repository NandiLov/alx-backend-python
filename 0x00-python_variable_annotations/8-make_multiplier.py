#!/usr/bin/env python3
"""Contains a function that multiplies a float by multiplier"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create and return a multiplier function.

    Args:
        multiplier (float): The value to multiply by.

    Returns:
        Callable[[float], float]: A function that takes a float and returns the result of multiplying it by 'multiplier'.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
