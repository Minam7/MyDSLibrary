from mylib.queue import Queue
import pytest


def test_is_empty():
    # Test is_empty
    q = Queue(4)
    answer = True
    assert q.is_empty() == answer


def test_enqueue_front():
    # Test enqueue
    q = Queue(4)
    q.enqueue(1)

    # Test front
    answer = 1
    assert q.front() == answer


def test_queue_fuctions():
    q = Queue(4)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(-1)
    q.enqueue(3)

    with pytest.raises(ValueError, match='Sorry Queue is full, try deleting item first.'):
        q.enqueue(-8)  # error for -8

    answer = True
    # full queue
    assert q.is_full() == answer

    # dequeue
    answer = 1
    assert q.dequeue() == answer

    # now front should be 2
    answer = 2
    assert q.front() == answer
