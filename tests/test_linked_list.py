from mylib.linkedList import SingleLink, DoubleLink
import pytest


def test_single_list_is_empty():
    # Test is_empty
    l_list = SingleLink()
    answer = True
    assert l_list.is_empty() == answer


def test_single_list_insert_exception():
    # Test insert
    l_list = SingleLink()

    l_list.insert_after(1, None)

    assert str(l_list.start) == '1->None'

    # should not be done
    with pytest.raises(ValueError, match='The next value you entered is not inserted in the list!'):
        l_list.insert_after(2, None)


def test_single_list_insert():
    # Test insert
    l_list = SingleLink()

    l_list.insert_after(1, None)
    assert str(l_list.start) == '1->None'

    l_list.insert_after(2, 1)
    assert str(l_list.start) == '1->2->None'

    l_list.insert_after(3, 2)
    assert str(l_list.start) == '1->2->3->None'

    l_list.insert_after(12, 1)


def test_single_list_find():
    # Test find
    l_list = SingleLink()

    l_list.insert_after(1, None)
    l_list.insert_after(2, 1)
    l_list.insert_after(3, 2)
    l_list.insert_after(12, 1)

    answer = None
    assert l_list.find(8) == answer

    assert str(l_list.find(2)) == '2->3->None'


def test_single_list_delete():
    # Test delete
    l_list = SingleLink()

    l_list.insert_after(1, None)
    assert str(l_list.start) == '1->None'

    l_list.insert_after(2, 1)
    assert str(l_list.start) == '1->2->None'

    l_list.insert_after(3, 2)
    assert str(l_list.start) == '1->2->3->None'

    l_list.insert_after(12, 1)
    assert str(l_list.start) == '1->12->2->3->None'

    l_list.delete(1)
    assert str(l_list.start) == '12->2->3->None'

    l_list.delete(2)
    assert str(l_list.start) == '12->3->None'


def test_single_list_get():
    # Test get
    l_list = SingleLink()

    l_list.insert_after(1, None)
    l_list.insert_after(2, 1)
    l_list.insert_after(3, 2)
    l_list.insert_after(12, 1)

    answer = -1  # not found is -1
    assert l_list.get(8) == answer

    answer = 2
    assert l_list.get(12) == answer


def test_single_size():
    # Test size
    l_list = SingleLink()
    answer = 0
    assert l_list.size() == answer

    l_list.insert_after(1, None)
    l_list.insert_after(2, 1)
    l_list.insert_after(3, 2)
    l_list.insert_after(12, 1)

    answer = 4
    assert l_list.size() == answer

    l_list.delete(1)
    l_list.delete(2)

    answer = 2
    assert l_list.size() == answer


def test_double_list_is_empty():
    # Test is_empty
    l_list = DoubleLink()
    answer = True
    assert l_list.is_empty() == answer


def test_double_list_find():
    # Test find
    l_list = DoubleLink()

    l_list.insert_after(1, None)
    l_list.insert_after(2, 1)
    l_list.insert_after(3, 2)
    l_list.insert_after(12, 1)

    answer = None
    assert l_list.find(8) == answer

    assert str(l_list.find(2)) == '2->3->None'


def test_double_list_delete():
    # Test delete
    l_list = DoubleLink()

    l_list.insert_after(1, None)
    l_list.insert_after(2, 1)
    l_list.insert_after(3, 2)
    l_list.insert_after(12, 1)
    assert str(l_list.start) == '1->12->2->3->None'

    l_list.delete(1)
    assert str(l_list.start) == '12->2->3->None'

    l_list.delete(2)
    assert str(l_list.start) == '12->3->None'


def test_double_list_get():
    # Test get
    l_list = DoubleLink()

    l_list.insert_after(1, None)
    l_list.insert_after(2, 1)
    l_list.insert_after(3, 2)
    l_list.insert_after(12, 1)

    answer = -1  # not found is -1
    assert l_list.get(8) == answer

    answer = 2
    assert l_list.get(12) == answer


def test_double_size():
    # Test size
    l_list = DoubleLink()
    answer = 0
    assert l_list.size() == answer

    l_list.insert_after(1, None)
    l_list.insert_after(2, 1)
    l_list.insert_after(3, 2)
    l_list.insert_after(12, 1)

    answer = 4
    assert l_list.size() == answer

    l_list.delete(1)
    l_list.delete(2)

    answer = 2
    assert l_list.size() == answer
