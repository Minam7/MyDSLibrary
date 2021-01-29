from mylib.linkedList import Node

class StackNode:
    def __init__(self):
        self.top = None

    def push(self, item_in):
        new_node = Node(item_in, self.top)
        self.top = new_node

    def pop(self):
        if self.top is None:
            raise ValueError("Empty stack")

        old_node = self.top
        self.top = self.top.next
        return old_node.value

    def peek(self):
        if self.top is None:
            raise ValueError("Empty stack")
        return self.top.value

    def size(self):
        # handling empty stack
        if self.top is None:
            return 0
        walker = self.top
        counter = 1
        while walker.next is not None:
            counter += 1
            walker = walker.next

        return counter

    def is_empty(self):
        return self.top is None
