from mylib.heap import MaxHeap, MinHeap


def test_max_heapify():
    # Test heapify
    data = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    answer = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    heap = MaxHeap(data)
    heap.max_heapify(1)
    assert heap.data == answer


def test_max_buildheap():
    # Test build heap
    data = [1, 2, 3, 4]
    answer = [4, 2, 3, 1]
    heap = MaxHeap(data)
    heap.build_heap()
    assert heap.data == answer


def test_extract_max():
    # Test extract max
    data = [1, 2, 3, 4]
    answer = [3, 2, 1, 4]
    heap = MaxHeap(data)
    heap.build_heap()
    heap.extract_max()
    assert heap.data == answer


def test_min_heapify():
    # Test heapify
    data = [16, 15, 10, 14, 7, 9, 3, 2, 8, 1]
    answer = [16, 7, 10, 14, 1, 9, 3, 2, 8, 15]
    heap = MinHeap(data)
    heap.min_heapify(1)
    assert heap.data == answer


def test_min_buildheap():
    # Test build heap
    data = [4, 3, 2, 1]
    answer = [1, 3, 2, 4]
    heap = MinHeap(data)
    heap.build_heap()
    assert heap.data == answer


def test_extract_min():
    # Test extract min
    data = [1, 2, 3, 4]
    answer = [3, 2, 1, 4]
    heap = MaxHeap(data)
    heap.build_heap()
    heap.extract_max()
    assert heap.data == answer
