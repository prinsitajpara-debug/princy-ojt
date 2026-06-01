"""
Generators Module
"""


def count_up_to(n: int):
    """Yield numbers from 1 to n."""
    for i in range(1, n + 1):
        yield i


def fibonacci(limit: int):
    """Generate Fibonacci sequence."""
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


def square_numbers(nums):
    """Yield squares of numbers."""
    for n in nums:
        yield n * n