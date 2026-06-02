# from src.types_module import (
#     add_numbers,
#     find_max,
#     safe_divide,
#     process_value,
# )


# def test_add_numbers_positive():
#     assert add_numbers([1, 2, 3]) == 6


# def test_add_numbers_empty():
#     assert add_numbers([]) == 0


# def test_find_max():
#     assert find_max([5, 9, 2]) == 9


# def test_safe_divide():
#     assert safe_divide(10, 2) == 5


# def test_process_value():
#     assert process_value(100) == "100"

from src.types_module import (
    add_numbers,
    find_max,
    safe_divide,
    process_value,
)


def test_add_numbers_positive():
    result = add_numbers([1, 2, 3])
    print("add_numbers([1,2,3]) =>", result)
    assert result == 6


def test_add_numbers_empty():
    result = add_numbers([])
    print("add_numbers([]) =>", result)
    assert result == 0


def test_find_max():
    result = find_max([5, 9, 2])
    print("find_max([5,9,2]) =>", result)
    assert result == 9


def test_safe_divide():
    result = safe_divide(10, 2)
    print("safe_divide(10,2) =>", result)
    assert result == 5


def test_process_value():
    result = process_value(100)
    print("process_value(100) =>", result)
    assert result == "100"