class StackInfo:
    def __init__(self, start_in, capacity_in):
        self.capacity = capacity_in
        self.start = start_in
        self.size = 0

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0


class FlexibleMultiStacks:
    def __init__(self, default_capacity_in, num_stack_in):
        self.S = [None] * default_capacity_in * num_stack_in
        self.stacks = []
        for i in range(num_stack_in):
            self.stacks.append(StackInfo(default_capacity_in * i, default_capacity_in))

    def is_all_full(self):
        all_full = True
        for item in self.stacks:
            all_full = all_full and item.is_full()
        return all_full

    def adjust_index(self, index_in):
        return index_in % len(self.stacks)

    def previous_index(self, index_in):
        return self.adjust_index(index_in - 1)

    def next_index(self, index_in):
        return self.adjust_index(index_in + 1)

    def last_element_index(self, stack_num_in):
        # this stack_num_in is base 0
        cur_stack = self.stacks[stack_num_in]
        return self.adjust_index(cur_stack.start + cur_stack.size - 1)

    def is_within_stack_capacity(self, stack_num_in, index_in):
        # this stack_num_in is base 0
        if index_in < 0 or index_in > len(self.S):
            return False
        cur_stack = self.stacks[stack_num_in]
        wraps_index = index_in
        if index_in < cur_stack.start:
            wraps_index = index_in + len(self.S)

        return (wraps_index >= cur_stack.start) and (wraps_index < (cur_stack.start + cur_stack.capacity))

    def last_capacity_index(self, stack_num_in):
        # this stack_num_in is base 0
        cur_stack = self.stacks[stack_num_in]
        return self.adjust_index(cur_stack.start + cur_stack.capacity - 1)

    def shift(self, stack_num_in):
        # this stack_num_in is base 0
        cur_stack = self.stacks[stack_num_in]
        if cur_stack.is_full():
            # this stack is full, we need to shift the next one
            self.shift((stack_num_in + 1) % len(self.stacks))
            cur_stack.capacity += 1

        # shift elements in stack
        start_index = self.last_capacity_index(stack_num_in)
        while self.is_within_stack_capacity(stack_num_in, start_index):
            self.S[start_index] = self.S[self.previous_index(start_index)]
            start_index = self.previous_index(start_index)

        self.S[cur_stack.start] = 0
        cur_stack.start = self.next_index(cur_stack.start)
        cur_stack.capacity -= 1

    def expand(self, stack_num_in):
        # this stack_num_in is base 0
        # shift next stack by 1
        self.shift((stack_num_in + 1) % len(self.stacks))
        self.stacks[stack_num_in].capacity += 1

    def push(self, stack_num_in, item_in):
        if self.is_all_full():
            raise ValueError("Stack overflow")

        cur_stack = self.stacks[stack_num_in - 1]
        if cur_stack.is_full():
            # time to expand
            self.expand(stack_num_in - 1)

        # normal push
        cur_stack.size += 1
        self.S[self.last_element_index(stack_num_in - 1)] = item_in

    def pop(self, stack_num_in):
        cur_stack = self.stacks[stack_num_in - 1]
        if cur_stack.is_empty():
            raise ValueError("Empty stack")
        else:
            old_item = self.S[self.last_element_index(stack_num_in - 1)]
            self.S[self.last_element_index(stack_num_in - 1)] = None
            cur_stack.size -= 1
            return old_item

    def peek(self, stack_num_in):
        cur_stack = self.stacks[stack_num_in - 1]
        if cur_stack.is_empty():
            raise ValueError("Empty stack")
        else:
            return self.S[self.last_element_index(stack_num_in - 1)]
