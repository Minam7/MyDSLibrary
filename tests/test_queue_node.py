from mylib.queueNode import QueueNode


def test_is_empty():
    # Test is_empty
    q = QueueNode()
    answer = True
    assert q.is_empty() == answer


def test_enqueue_front():
    # Test enqueue
    q = QueueNode()
    q.enqueue(1)

    # Test front
    answer = 1
    assert q.peek() == answer


def test_queue_fuctions():
    q = QueueNode()

    # empty Q
    assert q.is_empty() is True

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(-1)
    q.enqueue(3)

    # non empty Q
    assert q.is_empty() is False
    assert q.size() == 4

    # dequeue
    answer = 1
    assert q.dequeue() == answer
    assert q.size() == 3

    # now front should be 2
    answer = 2
    assert q.peek() == answer

    # dequeue all
    q.dequeue()
    q.dequeue()
    q.dequeue()
    assert q.is_empty() is True
    assert q.size() == 0

    # reinsert
    q.enqueue(12)
    assert q.peek() == 12
    assert q.size() == 1


if __name__ == '__main__':
    test_queue_fuctions()
