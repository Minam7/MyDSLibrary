class Stack:
    def __init__(self, size_in):
        self.size = size_in
        self.top = 0
        self.S = [None] * size_in

    def push(self, item_in):
        if self.top >= self.size:
            raise ValueError("Stack overflow, try deleting an item first!")

        self.S[self.top] = item_in
        self.top += 1

        return

    def pop(self):
        item_out = self.S[self.top - 1]
        self.S[self.top - 1] = None
        self.top -= 1
        return item_out

    def stack_top(self):
        if self.top == 0:
            raise ValueError("Empty stack")
        return self.S[self.top - 1]

    def stack_size(self):
        return self.top

    def is_full(self):
        return self.top >= self.size
