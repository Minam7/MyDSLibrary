from mylib.stackArray import Stack_Array
from mylib.stackNode import StackNode


class SetOfStacks:
    # define a stack limit for the whole structure.
    def __init__(self, limit_in):
        self.stack_holder = StackNode()
        self.limit = limit_in

    def push(self, item_in):
        try:
            self.stack_holder.peek()

            current_stack = self.stack_holder.peek()
            if current_stack.size() < self.limit:
                # current stack is still empty
                current_stack.push(item_in)
            else:
                # previous stack is full
                # create a new stack
                new_stack = Stack_Array(self.limit)
                new_stack.push(item_in)
                self.stack_holder.push(new_stack)

        except ValueError:
            # no stacks is created yet
            # create stack
            new_stack = Stack_Array(self.limit)
            new_stack.push(item_in)
            self.stack_holder.push(new_stack)

    def pop(self):
        last_stack = self.stack_holder.peek()
        old_item = last_stack.pop()
        if last_stack.is_empty():
            # delete this stack
            self.stack_holder.pop()
        return old_item

    def peek(self):
        return self.stack_holder.peek().peek()

    def size(self):
        if self.stack_holder.is_empty() is False:
            return ((self.stack_holder.size() - 1) * self.limit) + \
                   self.stack_holder.peek().size()
        else:
            return 0


class ShiftingSetOfStacks:
    def __init__(self, limit_in):
        self.limit = limit_in
        self.stacks = []

    def push(self, item_in):
        if len(self.stacks) == 0:
            # this is the first stack
            new_stack = Stack_Array(self.limit)
            new_stack.push(item_in)
            self.stacks.append(new_stack)
        else:
            try:
                # push in last stack
                self.stacks[len(self.stacks) - 1].push(item_in)

            except ValueError:
                # if stack is full add new one
                new_stack = Stack_Array(self.limit)
                new_stack.push(item_in)
                self.stacks.append(new_stack)

    def pop(self):
        if len(self.stacks) == 0:
            raise ValueError("Empty stack")
        else:
            last_stack = self.stacks[len(self.stacks) - 1]
            old_item = last_stack.pop()
            if last_stack.is_empty():
                # remove this stack
                self.stacks.pop()
            return old_item

    def remove_bottom(self, index_in):
        # return the bottom itme of the stack
        cur_stack = self.stacks[index_in]
        temp_stack = Stack_Array(self.limit)
        while cur_stack.size() > 1:
            temp_stack.push(cur_stack.pop())

        bottom_item = cur_stack.pop()
        while temp_stack.size() > 0:
            cur_stack.push(temp_stack.pop())

        return bottom_item

    def shift_left(self, index_in):
        for i in range(index_in, len(self.stacks)):
            bottom = self.remove_bottom(i)
            self.stacks[i - 1].push(bottom)

        if self.stacks[len(self.stacks) - 1].is_empty():
            # last stack got emptied
            # delete last stack
            self.stacks.pop()

    def pop_at(self, index_in):
        if index_in < 0 or index_in > len(self.stacks):
            raise ValueError("Stack index do not exist")

        reduced_stack = self.stacks[index_in - 1]
        old_item = reduced_stack.pop()

        if reduced_stack.is_empty():
            # there is no need to shift
            # just remove this stack
            self.stacks.pop(index_in - 1)
        else:
            # shift between stacks
            self.shift_left(index_in)

        return old_item

    def peek(self):
        if len(self.stacks) != 0:
            return self.stacks[len(self.stacks) - 1].peek()
        else:
            raise ValueError("Empty stack")

    def size(self):
        if len(self.stacks) != 0:
            return ((len(self.stacks) - 1) * self.limit) + \
                   self.stacks[len(self.stacks) - 1].size()
        else:
            return 0

    def is_empty(self):
        return len(self.stacks) == 0
