class Stack_Array:
    def __init__(self, size_in):
        self.limit = size_in
        self.top = 0
        self.S = [None] * size_in

    def push(self, item_in):
        if self.top >= self.limit:
            raise ValueError("Stack overflow, try deleting an item first!")

        self.S[self.top] = item_in
        self.top += 1

        return

    def pop(self):
        item_out = self.S[self.top - 1]
        self.S[self.top - 1] = None
        self.top -= 1
        return item_out

    def peek(self):
        if self.top == 0:
            raise ValueError("Empty stack")
        return self.S[self.top - 1]

    def size(self):
        return self.top

    def is_full(self):
        return self.top >= self.limit

    def is_empty(self):
        return self.top == 0
