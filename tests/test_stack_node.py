import pytest

from mylib.stackNode import StackNode


def test_push():
    # push
    s = StackNode()
    s.push(1)
    answer = 1
    assert s.peek() == answer

    s.push(2)
    s.push(3)
    answer = 3
    assert s.peek() == answer


def test_stack_functions():
    s = StackNode()

    # empty stack
    assert s.is_empty() is True

    s.push(1)
    s.push(2)
    s.push(-1)
    s.push(3)

    # non empty stack
    assert s.is_empty() is False
    assert s.size() == 4

    # test pop
    answer = 3
    assert s.pop() == answer
    assert s.size() == 3

    # now top should be -1
    answer = -1
    assert s.peek() == answer

    # pop all
    s.pop()
    s.pop()
    s.pop()
    assert s.is_empty() is True
    assert s.size() == 0


def test_empty_stack():
    s = StackNode()
    assert s.size() == 0

    with pytest.raises(ValueError, match='Empty stack'):
        s.peek()

    with pytest.raises(ValueError, match='Empty stack'):
        s.pop()
