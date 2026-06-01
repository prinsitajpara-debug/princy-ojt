import os

from src.file_handling import (
    write_file,
    read_file,
    append_file,
)


def test_write_file():
    write_file("temp.txt", "hello")
    assert os.path.exists("temp.txt")
    os.remove("temp.txt")


def test_read_file():
    write_file("temp.txt", "python")
    assert read_file("temp.txt") == "python"
    os.remove("temp.txt")


def test_append_file():
    write_file("temp.txt", "hello")
    append_file("temp.txt", " world")
    assert read_file("temp.txt") == "hello world"
    os.remove("temp.txt")