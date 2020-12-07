class Queue:
    def __init__(self, size_in):
        self.size = size_in
        self.first = 0
        self.item_count = 0
        self.Q = [None] * size_in

    def enqueue(self, item_in):
        if self.item_count == self.size:
            raise ValueError("Sorry Queue is full, try deleting item first.")

        self.Q[(self.item_count + self.first) % self.size] = item_in
        self.item_count += 1
        return

    def dequeue(self):
        if self.item_count == 0:
            raise ValueError("There is no item in the queue.")

        item_out = self.Q[self.first]
        self.Q[self.first] = None

        self.item_count -= 1
        self.first = (self.first + 1) % self.size

        return item_out

    def front(self):
        if self.item_count == 0:
            raise ValueError("There is no item in the queue.")

        return self.Q[self.first]

    def queue_size(self):
        return self.item_count

    def is_empty(self):
        return self.item_count == 0

    def is_full(self):
        return self.item_count >= self.size
