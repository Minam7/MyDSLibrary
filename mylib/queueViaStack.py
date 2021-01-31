from mylib.stackNode import StackNode


class QueueViaStacks:
    def __init__(self):
        self.frontS = StackNode()
        self.backS = StackNode()

    def push(self, item_in):
        if self.frontS.top is None and self.backS.top is None:
            # the first item in stack
            # push into front
            self.frontS.push(item_in)

        elif self.frontS.top is not None:
            self.backS.push(item_in)

    def fill_front(self):
        while self.backS.is_empty() is False:
            self.frontS.push(self.backS.pop())

    def pop(self):
        if self.frontS.is_empty() and self.backS.is_empty():
            raise ValueError("Empty stack")

        elif self.frontS.is_empty():
            # front got emptied
            # time to fill it with second one
            self.fill_front()

        old_item = self.frontS.pop()

        return old_item

    def peek(self):
        if self.frontS.is_empty() and self.backS.is_empty():
            raise ValueError("Empty stack")

        elif self.frontS.is_empty():
            # front got emptied
            # time to fill it with second one
            self.fill_front()

        return self.frontS.peek()

    def size(self):
        return self.frontS.size() + self.backS.size()

    def is_empty(self):
        return self.frontS.is_empty() and self.backS.is_empty()
