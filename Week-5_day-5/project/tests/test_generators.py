# from src.generators import (
#     count_up_to,
#     fibonacci,
#     square_numbers,
# )


# def test_count_up_to():
#     assert list(count_up_to(3)) == [1, 2, 3]


# def test_fibonacci():
#     assert list(fibonacci(10)) == [0, 1, 1, 2, 3, 5, 8]


# def test_square_numbers():
#     assert list(square_numbers([1, 2, 3])) == [1, 4, 9]

from src.generators import (
    count_up_to,
    fibonacci,
    square_numbers,
)


def test_count_up_to():
    result = list(count_up_to(3))
    print("count_up_to(3) =>", result)
    assert result == [1, 2, 3]


def test_fibonacci():
    result = list(fibonacci(10))
    print("fibonacci(10) =>", result)
    assert result == [0, 1, 1, 2, 3, 5, 8]


def test_square_numbers():
    result = list(square_numbers([1, 2, 3]))
    print("square_numbers([1,2,3]) =>", result)
    assert result == [1, 4, 9]