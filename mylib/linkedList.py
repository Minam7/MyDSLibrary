class Node:
    def __init__(self, value_in, forward_in):
        self.value = value_in
        self.next = forward_in

    def __str__(self):  # Returns the path from root to node
        return str(self.value) + "->" + str(self.next)


class SingleLink:
    def __init__(self, start_in=None):
        self.start = start_in

    def find(self, value_in):
        # find the value_in node
        walker = self.start
        find_node = None
        while walker is not None:
            if walker.value == value_in:
                find_node = walker
                break
            walker = walker.next

        if find_node is None:
            return None

        return find_node

    def insert_after(self, item_in, after_in):
        if self.start is None:
            # this is the first item
            new_node = Node(item_in, None)
            self.start = new_node
            return

        # find the after_in node
        after_node = self.find(after_in)

        if after_node is None:
            raise ValueError('The next value you entered is not inserted in the list!')

        new_node = Node(item_in, after_node.next)
        after_node.next = new_node

        return

    def delete(self, item_in):
        if self.start is None:
            raise ValueError('List is already empty.')

        # find the item_in node
        walker = self.start
        find_node = None
        pre_node = None
        while walker is not None:
            if walker.value == item_in:
                find_node = walker
                break
            pre_node = walker
            walker = walker.next

        if find_node is None:
            raise ValueError('The next value you entered is not inserted in the list!')

        if pre_node is not None:
            pre_node.next = find_node.next
        else:
            # this is also the start of the list
            self.start = find_node.next

        find_node.next = None

        return find_node

    def get(self, value_in):
        count = 0
        # find the value_in node
        walker = self.start
        find_node = None
        while walker is not None:
            if walker.value == value_in:
                find_node = walker
                break
            count += 1
            walker = walker.next
        if find_node is None:
            return -1

        return count + 1

    def size(self):
        count = 0
        walker = self.start
        while walker is not None:
            count += 1
            walker = walker.next

        return count

    def is_empty(self):
        if self.start is None:
            return True
        return False


class DoubleNode(Node):
    def __init__(self, value_in, forward_in, backward_in):
        super().__init__(value_in, forward_in)
        self.prev = backward_in

    def summary(self):
        print("----------------Node Summary----------------")
        print("Value:", self.value)
        print("Backward Pointer:", self.prev, "Forward Pointer:", self.next)
        print()
        return


class DoubleLink:
    def __init__(self, start_in=None):
        self.start = start_in

    def find(self, value_in):
        # find the value_in node
        walker = self.start
        find_node = None
        while walker is not None:
            if walker.value == value_in:
                find_node = walker
                break
            walker = walker.next

        if find_node is None:
            return None

        return find_node

    def insert_after(self, item_in, after_in):
        if self.start is None:
            # this is the first item
            new_node = DoubleNode(item_in, None, None)
            self.start = new_node
            return

        # find the after_in node
        after_node = self.find(after_in)

        if after_node is None:
            raise ValueError('The next value you entered is not inserted in the list!')

        new_node = DoubleNode(item_in, after_node.next, after_node)

        if after_node.next is not None:
            after_node.next.prev = new_node

        after_node.next = new_node

        return

    def delete(self, item_in):
        if self.start is None:
            raise ValueError('List is already empty.')

        # find the item_in node
        find_node = self.find(item_in)

        if find_node is None:
            raise ValueError('The next value you entered is not inserted in the list!')

        if find_node.prev is not None:
            find_node.prev.next = find_node.next
        else:
            # this is also the start of the list
            self.start = find_node.next

        if find_node.next is not None:
            find_node.next.prev = find_node.prev

        find_node.next = None
        find_node.prev = None

        return find_node

    def get(self, value_in):
        count = 0
        # find the value_in node
        walker = self.start
        find_node = None
        while walker is not None:
            if walker.value == value_in:
                find_node = walker
                break
            count += 1
            walker = walker.next
        if find_node is None:
            return -1

        return count + 1

    def size(self):
        count = 0
        walker = self.start
        while walker is not None:
            count += 1
            walker = walker.next

        return count

    def is_empty(self):
        if self.start is None:
            return True
        return False
