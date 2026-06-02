# # from src.data_structures import Stack, Queue


# # def test_stack_push():
# #     s = Stack()
# #     s.push(10)
# #     assert s.items == [10]


# # def test_stack_pop():
# #     s = Stack()
# #     s.push(1)
# #     s.push(2)
# #     assert s.pop() == 2


# # def test_stack_empty():
# #     s = Stack()
# #     assert s.is_empty() is True


# # def test_queue_enqueue():
# #     q = Queue()
# #     q.enqueue(10)
# #     assert q.items == [10]


# # def test_queue_dequeue():
# #     q = Queue()
# #     q.enqueue(1)
# #     q.enqueue(2)
# #     assert q.dequeue() == 1

from src.data_structures import Stack, Queue


def test_stack_push():
    s = Stack()
    s.push(10)
    print("Stack after push:", s.items)

    assert s.items == [10]


def test_stack_pop():
    s = Stack()
    s.push(1)
    s.push(2)

    popped = s.pop()
    print("Popped value:", popped)
    print("Stack after pop:", s.items)

    assert popped == 2


def test_stack_empty():
    s = Stack()
    print("Stack is empty:", s.is_empty())

    assert s.is_empty() is True


def test_queue_enqueue():
    q = Queue()
    q.enqueue(10)
    print("Queue after enqueue:", q.items)

    assert q.items == [10]


def test_queue_dequeue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)

    removed = q.dequeue()
    print("Dequeued value:", removed)
    print("Queue after dequeue:", q.items)

    assert removed == 1
