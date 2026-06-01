"""
Data Structures Module
Stack, Queue implementations
"""


class Stack:
    """Simple Stack implementation."""

    def __init__(self):
        self.items = []

    def push(self, item):
        """Add item to stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return top item."""
        return self.items.pop() if self.items else None

    def is_empty(self):
        """Check if stack is empty."""
        return len(self.items) == 0


class Queue:
    """Simple Queue implementation."""

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add item to queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove first item."""
        return self.items.pop(0) if self.items else None