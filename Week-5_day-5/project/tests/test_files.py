# import os

# from src.file_handling import (
#     write_file,
#     read_file,
#     append_file,
# )


# def test_write_file():
#     write_file("temp.txt", "hello")
#     assert os.path.exists("temp.txt")
#     os.remove("temp.txt")


# def test_read_file():
#     write_file("temp.txt", "python")
#     assert read_file("temp.txt") == "python"
#     os.remove("temp.txt")


# def test_append_file():
#     write_file("temp.txt", "hello")
#     append_file("temp.txt", " world")
#     assert read_file("temp.txt") == "hello world"
#     os.remove("temp.txt")

import os

from src.file_handling import (
    write_file,
    read_file,
    append_file,
)


def test_write_file():
    write_file("temp.txt", "hello")
    print("File written: temp.txt with content 'hello'")

    assert os.path.exists("temp.txt")
    print("File exists check: PASSED")

    os.remove("temp.txt")
    print("File deleted: temp.txt")


def test_read_file():
    write_file("temp.txt", "python")
    print("File written: temp.txt with content 'python'")

    content = read_file("temp.txt")
    print("File read content:", content)

    assert content == "python"

    os.remove("temp.txt")
    print("File deleted: temp.txt")


def test_append_file():
    write_file("temp.txt", "hello")
    print("Initial file content: hello")

    append_file("temp.txt", " world")
    print("Appended ' world' to file")

    content = read_file("temp.txt")
    print("Final file content:", content)

    assert content == "hello world"

    os.remove("temp.txt")
    print("File deleted: temp.txt")