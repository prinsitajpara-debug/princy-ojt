from src.data_structures import Stack, Queue


def test_stack_push():
    s = Stack()
    s.push(10)
    assert s.items == [10]


def test_stack_pop():
    s = Stack()
    s.push(1)
    s.push(2)
    assert s.pop() == 2


def test_stack_empty():
    s = Stack()
    assert s.is_empty() is True


def test_queue_enqueue():
    q = Queue()
    q.enqueue(10)
    assert q.items == [10]


def test_queue_dequeue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1