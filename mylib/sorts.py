from random import randint
from mylib.heap import MinHeap, MaxHeap


############### Bubble Sort
def bubble_sort(data_in):
    for i in range(len(data_in)):
        for j in range(len(data_in) - 1, i, -1):
            if data_in[j] < data_in[j - 1]:
                data_in[j - 1], data_in[j] = data_in[j], data_in[j - 1]
    return data_in


def speed_bubble_sort(data_in):
    for i in range(len(data_in)):
        bubble = False
        for j in range(len(data_in) - 1, i, -1):
            if data_in[j] < data_in[j - 1]:
                data_in[j - 1], data_in[j] = data_in[j], data_in[j - 1]
                bubble = True

        if bubble is False:
            break
    return data_in


############# Insertion Sort
def insertion_sort(data_in):
    for i in range(1, len(data_in)):
        key = data_in[i]

        j = i - 1
        while (j > -1) and (key < data_in[j]):
            data_in[j + 1] = data_in[j]
            j -= 1
        data_in[j + 1] = key
    return data_in


def binary_search(data_in, item_in):
    if len(data_in) == 0:
        return 0
    if len(data_in) == 1:
        if item_in < data_in[0]:
            return 0
        else:
            return 1

    length = len(data_in) // 2
    if item_in < data_in[length]:
        return binary_search(data_in[:length], item_in)
    elif item_in > data_in[length]:
        return length + binary_search(data_in[length:], item_in)
    else:
        return length


def binary_insertion_sort(data_in):
    for i in range(1, len(data_in)):
        key = data_in[i]

        j = binary_search(data_in[:i], key)
        for k in range(i - j):
            data_in[i - k] = data_in[i - k - 1]
        data_in[j] = key
    return data_in


############### Merge Sort
def merge(a_in, b_in):
    merged = []

    if len(a_in) == 0:
        return b_in
    if len(b_in) == 0:
        return a_in

    if a_in[len(a_in) - 1] < b_in[0]:
        merged = list(a_in)
        merged.extend(b_in)
        return merged
    if b_in[len(b_in) - 1] < a_in[0]:
        merged = list(b_in)
        merged.extend(a_in)
        return merged

    a_index = 0
    b_index = 0
    while (a_index < len(a_in)) and (b_index < len(b_in)):
        # <= is for making mergesort stable
        if a_in[a_index] <= b_in[b_index]:
            merged.append(a_in[a_index])
            a_index += 1

        elif a_in[a_index] > b_in[b_index]:
            merged.append(b_in[b_index])
            b_index += 1
        else:
            merged.append(a_in[a_index])
            merged.append(b_in[b_index])
            a_index += 1
            b_index += 1

    if a_index < len(a_in):
        # first array remains
        merged.extend(a_in[a_index:])
        return merged

    if b_index < len(b_in):
        # first array remains
        merged.extend(b_in[b_index:])
        return merged
    return merged


def merge_sort(data_in):
    if len(data_in) == 1:
        return data_in
    if len(data_in) == 0:
        return []
    else:
        length = len(data_in) // 2
        first_section = merge_sort(data_in[:length])
        second_section = merge_sort(data_in[length:])
        return merge(first_section, second_section)


############### Quick Sort
def partition_last(data_in, left_point, right_point):
    # choosing rightmost item in array as pivot
    pivot = data_in[right_point]

    smallest_index = left_point - 1

    for i in range(left_point, right_point + 1):
        if data_in[i] < pivot:
            smallest_index += 1
            data_in[smallest_index], data_in[i] = data_in[i], data_in[smallest_index]

    # swap pivot
    smallest_index += 1
    data_in[smallest_index], data_in[right_point] = pivot, data_in[smallest_index]

    return smallest_index


def partition_first(data_in, left_point, right_point):
    # choosing leftmost item in array as pivot
    pivot = data_in[left_point]

    biggest_index = right_point + 1

    for i in range(right_point, left_point, -1):
        if data_in[i] > pivot:
            biggest_index -= 1
            data_in[i], data_in[biggest_index] = data_in[biggest_index], data_in[i]

    # swap pivot
    biggest_index -= 1
    data_in[biggest_index], data_in[left_point] = pivot, data_in[biggest_index]

    return biggest_index


def partition_random(data_in, left_point, right_point):
    # random pivot choosing
    pivot_position = randint(left_point, right_point)

    # divide by pivot position then run two above!
    last_pos = partition_last(data_in, left_point, pivot_position)
    first_pos = partition_first(data_in, last_pos, right_point)

    return first_pos


def partition_median(data_in, left_point, right_point):
    # random pivot choosing
    pivot_position = (right_point + left_point) // 2

    # divide by pivot position then run two above!
    last_pos = partition_last(data_in, left_point, pivot_position)
    first_pos = partition_first(data_in, last_pos, right_point)

    return first_pos


def quick_sort(data_in, left_pointer, right_pointer, partition_func):
    if right_pointer > left_pointer:
        pivot_pos = partition_func(data_in, left_pointer, right_pointer)

        quick_sort(data_in, left_pointer, pivot_pos - 1, partition_func)
        quick_sort(data_in, pivot_pos + 1, right_pointer, partition_func)

    return data_in


############### Counting Sort
def unstable_counting_sort(k_in, data_in):
    holder = [[] for _ in range(k_in)]

    for item in data_in:
        holder[item].append(item)

    sorted_list = []
    for item in holder:
        sorted_list.extend(item)

    return sorted_list


def stable_counting_sort(data_in, k_in):
    key_in = [0 for _ in range(k_in)]
    for item in data_in:
        key_in[item - 1] += 1
    for x in range(1, k_in):
        key_in[x] += key_in[x - 1]

    sorted_out = [0 for _ in range(len(data_in))]
    for x in range(len(data_in) - 1, -1, -1):
        sorted_out[key_in[data_in[x] - 1] - 1] = data_in[x]
        key_in[data_in[x] - 1] -= 1

    return sorted_out


############### Radix Sort
def key_counting_sort(key_in, data_in):
    holder = [[] for _ in range(10)]

    for i in range(len(data_in)):
        holder[key_in[i]].append(data_in[i])

    sorted_list = []
    for item in holder:
        sorted_list.extend(item)

    return sorted_list


def convert(base_in, number):
    string = ''
    while number != 0:
        string += str(number % base_in)
        number = number // base_in
    return string[::-1]


def radix_sort(array_in):
    d = len(convert(10, max(array_in)))

    for k in range(d):
        keys = []

        for j in range(len(array_in)):
            keys.append((array_in[j] // (10 ** k)) % 10)

        array_in = key_counting_sort(keys, array_in)

    return array_in


############### Selection Sort
def find_min(data_in):
    minimum = float('inf')
    index = -1

    for i in range(len(data_in)):
        if data_in[i] < minimum:
            minimum = data_in[i]
            index = i
    return minimum, index


def selection_sort(data_in):
    for i in range(len(data_in)):
        mini, index_min = find_min(data_in[i:])
        data_in[i], data_in[index_min + i] = mini, data_in[i]

    return data_in


############### Max Heap Sort
def heap_sort_max(data_in):
    maxheap = MaxHeap(data_in)
    maxheap.build_heap()

    while maxheap.size > 1:
        maxheap.extract_max()

    return maxheap.data


############### Min Heap Sort
def heap_sort_min(data_in):
    minheap = MinHeap(data_in)
    minheap.build_heap()

    while minheap.size > 1:
        minheap.extract_min()

    return minheap.data
