from mylib.linkedList import Node


class QueueNode:
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, item_in):
        new_node = Node(item_in, None)
        if self.last is not None:
            self.last.next = new_node

        self.last = new_node

        if self.first is None:
            # Q was empty at first
            self.first = new_node

    def dequeue(self):
        if self.first is None:
            raise ValueError("Empty Queue")

        old_node = self.first
        self.first = self.first.next
        if self.first is None:
            # Q got emptied
            self.last = self.first

        return old_node.value

    def peek(self):
        if self.first is None:
            raise ValueError("Empty Queue")
        return self.first.value

    def size(self):
        if self.first is None:
            return 0

        counter = 1
        walker = self.first

        while walker != self.last:
            counter += 1
            walker = walker.next

        return counter

    def is_empty(self):
        return self.first is None
