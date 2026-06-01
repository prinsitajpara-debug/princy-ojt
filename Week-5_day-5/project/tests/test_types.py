from src.types_module import (
    add_numbers,
    find_max,
    safe_divide,
    process_value,
)


def test_add_numbers_positive():
    assert add_numbers([1, 2, 3]) == 6


def test_add_numbers_empty():
    assert add_numbers([]) == 0


def test_find_max():
    assert find_max([5, 9, 2]) == 9


def test_safe_divide():
    assert safe_divide(10, 2) == 5


def test_process_value():
    assert process_value(100) == "100"