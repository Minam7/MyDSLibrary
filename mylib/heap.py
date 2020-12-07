class MaxHeap:
    def __init__(self, data_in):
        self.data = data_in
        self.size = len(data_in)

    def get_max(self):
        return self.data[0]

    def max_heapify(self, index):
        if index > self.size // 2:
            return

        biggest = index

        left = 2 * index + 1
        right = 2 * (index + 1)
        if left < self.size and self.data[left] > self.data[biggest]:
            biggest = left

        if right < self.size and self.data[right] > self.data[biggest]:
            biggest = right

        if biggest != index:
            # swap
            self.data[index], self.data[biggest] = self.data[biggest], self.data[index]
            return self.max_heapify(biggest)

    def build_heap(self):
        for i in range(self.size // 2, -1, -1):
            self.max_heapify(i)

    def extract_max(self):
        # put max at the end of the array
        self.data[0], self.data[self.size - 1] = self.data[self.size - 1], self.data[0]
        self.size -= 1
        self.max_heapify(0)


class MinHeap:
    def __init__(self, data_in):
        self.data = data_in
        self.size = len(data_in)

    def get_min(self):
        return self.data[0]

    def min_heapify(self, index):
        if index > self.size // 2:
            return

        smallest = index

        left = 2 * index + 1
        right = 2 * (index + 1)
        if left < self.size and self.data[left] < self.data[smallest]:
            smallest = left

        if right < self.size and self.data[right] < self.data[smallest]:
            smallest = right

        if smallest != index:
            # swap
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            return self.min_heapify(smallest)

    def build_heap(self):
        for i in range(self.size // 2, -1, -1):
            self.min_heapify(i)

    def extract_min(self):
        # put max at the end of the array
        self.data[0], self.data[self.size - 1] = self.data[self.size - 1], self.data[0]
        self.size -= 1
        self.min_heapify(0)
