"""
Types Module - basic type hinting utilities
"""

from typing import List, Optional, Union


def add_numbers(nums: List[int]) -> int:
    """Return sum of list of integers."""
    return sum(nums)


def find_max(nums: List[int]) -> int:
    """Return maximum number in list."""
    return max(nums)


def safe_divide(a: float, b: float) -> Optional[float]:
    """Return division result or None if division by zero."""
    if b == 0:
        return None
    return a / b


def process_value(value: Union[int, str]) -> str:
    """Convert int or str to string safely."""
    return str(value)