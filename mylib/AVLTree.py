def get_height(node_in):
    if node_in is None:
        return -1

    return node_in.height


class Node:
    def __init__(self, key_in, parent_in):
        self.key = key_in
        self.parent = parent_in
        self.left_child = None
        self.right_child = None
        self.height = 0

    def update_height(self):
        self.height = 1 + max(get_height(self.left_child), get_height(self.right_child))
        return

    def AVL_condition(self):

        # difference between left and right subtree
        left = get_height(self.left_child)
        right = get_height(self.right_child)

        return left - right

    def __str__(self):  # Returns the path from root to node
        if self.parent:
            return str(self.parent) + "->" + str(self.key)
        else:
            return str(self.key)

    def summary(self):
        print("----------------Node Summary----------------")
        print("Parent:", self.parent, "Key:", self.key)
        print("Left Child:", self.left_child, "Right Child:", self.right_child)
        print("Height:", self.height)
        print()
        return


class AVLTree:
    def __init__(self):
        self.root = None

    def left_rotation(self, node_in):
        parent = node_in.parent

        child = node_in.right_child
        child.parent = parent

        if child.parent is None:
            self.root = child
        else:
            if child.parent.left_child is node_in:
                child.parent.left_child = child
            elif child.parent.right_child is node_in:
                child.parent.right_child = child

        node_in.right_child = child.left_child
        if node_in.right_child is not None:
            node_in.right_child.parent = node_in

        child.left_child = node_in
        node_in.parent = child

        node_in.update_height()
        child.update_height()

        return

    def right_rotation(self, node_in):
        parent = node_in.parent

        child = node_in.left_child
        child.parent = parent

        if child.parent is None:
            self.root = child
        else:
            if child.parent.left_child is node_in:
                child.parent.left_child = child
            elif child.parent.right_child is node_in:
                child.parent.right_child = child

        node_in.left_child = child.right_child
        if node_in.left_child is not None:
            node_in.left_child.parent = node_in

        child.right_child = node_in
        node_in.parent = child

        node_in.update_height()
        child.update_height()

        return

    def build_tree(self, array_in):
        if len(array_in) == 0:
            return

        self.root = Node(array_in[0], None)
        for i in range(1, len(array_in)):
            new_node = Node(array_in[i], None)
            self.insert(new_node)

    def bst_insert(self, node_in):
        if self.root is None:
            self.root = node_in
            return

        walker = self.root

        while True:
            if walker.key > node_in.key:
                # go to left subtree
                if walker.left_child is None:
                    walker.left_child = node_in
                    node_in.parent = walker
                    return
                walker = walker.left_child
            if walker.key <= node_in.key:
                if walker.right_child is None:
                    walker.right_child = node_in
                    node_in.parent = walker
                    return
                walker = walker.right_child

    def rebalance(self, node_in):
        balance_walker = node_in

        while balance_walker is not None:
            balance_walker.update_height()
            condition = balance_walker.AVL_condition()
            if condition > 1:
                # left-heavy
                child_condition = balance_walker.left_child.AVL_condition()

                if child_condition > -1:
                    # child is also left-heavy or balanced
                    # do one right rotation
                    self.right_rotation(balance_walker)
                else:
                    # child is right-heavy
                    # do one left rotation, then right rotation
                    self.left_rotation(balance_walker.left_child)
                    self.right_rotation(balance_walker)

            elif condition < -1:

                # right-heavy
                child_condition = balance_walker.right_child.AVL_condition()

                if child_condition < 1:
                    # child is also right heavy or balanced
                    # do one left rotation
                    self.left_rotation(balance_walker)
                else:
                    # do one right rotation, then left rotation
                    self.right_rotation(balance_walker.right_child)
                    self.left_rotation(balance_walker)

            balance_walker = balance_walker.parent
        return

    def insert(self, node_in):
        self.bst_insert(node_in)
        self.rebalance(node_in)

    def find(self, value):
        if self.root is None:
            return None

        walker = self.root

        while walker is not None:
            if value == walker.key:
                return walker

            if value < walker.key:
                walker = walker.left_child

            if value > walker.key:
                walker = walker.right_child

        return None

    def find_min(self, walker='root'):
        if walker == 'root':
            walker = self.root

        if walker.left_child is None:
            return walker

        walker = walker.left_child
        while walker.left_child is not None:
            walker = walker.left_child
        return walker

    def find_max(self, walker='root'):
        if walker == 'root':
            walker = self.root

        if walker.right_child is None:
            return walker

        walker = walker.right_child
        while walker.right_child is not None:
            walker = walker.right_child
        return walker

    def next_larger(self, node_in):
        if node_in.right_child is not None:
            return self.find_min(node_in.right_child)

        walker = node_in.parent
        while walker is not None and walker.right_child == node_in:
            node_in = walker
            walker = node_in.parent

        return walker

    def in_order_traversal(self, node_in):
        sorted_list = list()
        # look at left child, then self, then right child
        if node_in is None:
            return sorted_list

        if node_in.left_child is not None:
            sorted_list.extend(self.in_order_traversal(node_in.left_child))

        sorted_list.append(node_in.key)

        if node_in.right_child is not None:
            sorted_list.extend(self.in_order_traversal(node_in.right_child))

        return sorted_list
