import pytest

from mylib.stackArray import Stack_Array


def test_is_full():
    # Test is_full
    s = Stack_Array(4)
    answer = False
    assert s.is_full() == answer


def test_push_top():
    # Test push
    s = Stack_Array(4)
    s.push(1)

    # Test top
    answer = 1
    assert s.peek() == answer


def test_stack_fuctions():
    s = Stack_Array(4)
    s.push(1)
    s.push(2)
    s.push(-1)
    s.push(3)

    with pytest.raises(ValueError, match='Stack overflow, try deleting an item first!'):
        s.push(-8)  # error for -8

    answer = True

    # full stack
    assert s.is_full() == answer

    # test pop
    answer = 3
    assert s.pop() == answer

    # now top should be -1
    answer = -1
    assert s.peek() == answer