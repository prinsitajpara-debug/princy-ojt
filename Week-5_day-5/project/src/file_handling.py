"""
File Handling Module
"""

from pathlib import Path


def write_file(path: str, content: str):
    """Write content to file."""
    Path(path).write_text(content)


def read_file(path: str) -> str:
    """Read file content."""
    return Path(path).read_text()


def append_file(path: str, content: str):
    """Append content to file."""
    with open(path, "a") as f:
        f.write(content)