from src.generators import (
    count_up_to,
    fibonacci,
    square_numbers,
)


def test_count_up_to():
    assert list(count_up_to(3)) == [1, 2, 3]


def test_fibonacci():
    assert list(fibonacci(10)) == [0, 1, 1, 2, 3, 5, 8]


def test_square_numbers():
    assert list(square_numbers([1, 2, 3])) == [1, 4, 9]