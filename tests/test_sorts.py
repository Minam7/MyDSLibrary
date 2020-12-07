from mylib import sorts


def test_bubble_sort():
    # test sort function
    c = [5, 3, 7, 0, -1, 2, 4, 7, 10, 23]
    answer = [-1, 0, 2, 3, 4, 5, 7, 7, 10, 23]
    assert sorts.bubble_sort(c) == answer


def test_speed_bubble_sort():
    # test sort function
    c = [5, 3, 7, 0, -1, 2, 4, 7, 10, 23]
    answer = [-1, 0, 2, 3, 4, 5, 7, 7, 10, 23]
    assert sorts.speed_bubble_sort(c) == answer


def test_insertion_sort():
    # test sort function
    c = [5, 3, 7, 0, -1, 2, 4, 7, 10, 23]
    answer = [-1, 0, 2, 3, 4, 5, 7, 7, 10, 23]
    assert sorts.insertion_sort(c) == answer


def test_binary_search():
    # test sort function
    answer = 3
    a = [1, 3, 3, 4, 8]
    b = 4
    assert sorts.binary_search(a, b) == answer


def test_binary_insertion_sort():
    # test sort function
    c = [5, 3, 7, 0, -1, 2, 4, 7, 10, 23]
    answer = [-1, 0, 2, 3, 4, 5, 7, 7, 10, 23]
    assert sorts.binary_insertion_sort(c) == answer


def test_merge_function():
    # Test merge function
    a = [5, 7, 9, 10]
    b = [3, 6, 7, 11, 12]
    answer = [3, 5, 6, 7, 7, 9, 10, 11, 12]
    assert sorts.merge(a, b) == answer


def test_merge_sort():
    # test sort function
    c = [5, 3, 7, 0, -1, 2, 4, 7, 10, 23]
    answer = [-1, 0, 2, 3, 4, 5, 7, 7, 10, 23]
    assert sorts.merge_sort(c) == answer


def test_last_quick_sort():
    # test sort function
    c = [5, 3, 7, 0, -1, 2, 4, 7, 10, 23]
    answer = [-1, 0, 2, 3, 4, 5, 7, 7, 10, 23]
    assert sorts.quick_sort(c, 0, len(c) - 1, sorts.partition_last) == answer


def test_first_quick_sort():
    # test sort function
    c = [5, 3, 7, 0, -1, 2, 4, 7, 10, 23]
    answer = [-1, 0, 2, 3, 4, 5, 7, 7, 10, 23]
    assert sorts.quick_sort(c, 0, len(c) - 1, sorts.partition_first) == answer


def test_random_quick_sort():
    # test sort function
    c = [5, 3, 7, 0, -1, 2, 4, 7, 10, 23]
    answer = [-1, 0, 2, 3, 4, 5, 7, 7, 10, 23]
    assert sorts.quick_sort(c, 0, len(c) - 1, sorts.partition_random) == answer


def test_median_quick_sort():
    # test sort function
    c = [5, 3, 7, 0, -1, 2, 4, 7, 10, 23]
    answer = [-1, 0, 2, 3, 4, 5, 7, 7, 10, 23]
    assert sorts.quick_sort(c, 0, len(c) - 1, sorts.partition_median) == answer


def test_counting_sort():
    # test sort function
    c = [5, 3, 7, 0, 2, 4, 7, 10, 23]
    answer = [0, 2, 3, 4, 5, 7, 7, 10, 23]
    assert sorts.counting_sort(24, c) == answer


def test_key_counting_sort():
    # test sort function
    c = [5, 3, 7, 0, 2, 4, 7, 9, 3]
    answer = [0, 2, 3, 3, 4, 5, 7, 7, 9]
    assert sorts.key_counting_sort(c, c) == answer


def test_radix_sort():
    # test sort function
    c = [5, 3, 7, 0, 2, 4, 7, 10, 23]
    answer = [0, 2, 3, 4, 5, 7, 7, 10, 23]
    assert sorts.radix_sort(c) == answer


def test_selection_sort():
    # test sort function
    c = [5, 3, 7, 0, -1, 2, 4, 7, 10, 23]
    answer = [-1, 0, 2, 3, 4, 5, 7, 7, 10, 23]
    assert sorts.selection_sort(c) == answer


def test_heap_sort_max():
    # test sort function
    c = [5, 3, 7, 0, -1, 2, 4, 7, 10, 23]
    answer = [-1, 0, 2, 3, 4, 5, 7, 7, 10, 23]
    assert sorts.heap_sort_max(c) == answer


def test_heap_sort_min():
    # test sort function
    c = [5, 3, 7, 0, -1, 2, 4, 7, 10, 23]
    answer = [23, 10, 7, 7, 5, 4, 3, 2, 0, -1]
    assert sorts.heap_sort_min(c) == answer
