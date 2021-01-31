from mylib.stackNode import StackNode


class StackMinHolder(StackNode):
    def __init__(self):
        super().__init__()
        self.minStack = StackNode()

    def push(self, item_in):
        super().push(item_in)
        if self.minStack.top is None:
            # the first item
            self.minStack.push(item_in)

        elif item_in <= self.minStack.peek():
            self.minStack.push(item_in)

    def pop(self):
        old_item = super().pop()
        if self.minStack.peek() == old_item:
            self.minStack.pop()

    def min(self):
        return self.minStack.peek()
