from random import randint


class Node:
    def __init__(self, key_in, parent_in):
        self.key = key_in
        self.heap_key = randint(0, 10000)
        self.parent = parent_in
        self.left_child = None
        self.right_child = None

    def __str__(self):  # Returns the path from root to node
        if self.parent:
            return str(self.parent) + "->" + str(self.key) + ',' + str(self.heap_key)
        else:
            return str(self.key) + ',' + str(self.heap_key)

    def summary(self):
        print("----------------Node Summary----------------")
        print("Parent:", self.parent, "Key:", self.key, "Heapkey:", self.heap_key)
        print("Left Child:", self.left_child, "Right Child:", self.right_child)
        print()
        return


class Treap:
    def __init__(self, root_in=None):
        self.root = root_in

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
                    break
                walker = walker.left_child
            if walker.key <= node_in.key:
                if walker.right_child is None:
                    walker.right_child = node_in
                    node_in.parent = walker
                    break
                walker = walker.right_child
        return

    def heapify(self, node_in):
        if node_in is None or node_in.parent is None:
            return

        if node_in.parent.left_child is node_in:
            # node is left child
            self.right_rotation(node_in.parent)

        else:
            # node is right child
            self.left_rotation(node_in.parent)

    def min_heapify(self, node_in):
        walker = node_in
        while walker is not None and walker.parent is not None:
            if walker.heap_key < walker.parent.heap_key:
                self.heapify(walker)
            else:
                break

    def insert(self, node_in):
        self.bst_insert(node_in)
        self.min_heapify(node_in)

    def build_tree(self, array_in):
        for item in array_in:
            new_node = Node(item, None)
            print(new_node)
            self.insert(new_node)

    def find(self, value):
        if self.root is None:
            return None

        walker = self.root

        while walker is not None:
            if value == walker.key:
                return walker

            if value < walker.key:
                walker = walker.left_child
            elif value > walker.key:
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

    def delete_node(self, value_in):
        searched_node = self.find(value_in)
        self.delete(searched_node)

    def delete(self, found_node):

        if found_node is None:
            return

        if found_node.left_child is None and found_node.right_child is None:
            # this is leaf so delete it freely
            parent = found_node.parent
            if parent.left_child is found_node:
                parent.left_child = None
            else:
                parent.right_child = None
            return

        if found_node.left_child is None:
            # only have right child
            successor = found_node.right_child
            found_node.key = successor.key
            return

        if found_node.right_child is None:
            # only have left child
            successor = found_node.left_child
            found_node.key = successor.key
            return

        # having both children
        smallest_child = found_node.left_child

        if smallest_child.heap_key > found_node.right_child.heap_key:
            smallest_child = found_node.right_child

        if smallest_child is found_node.left_child:
            self.right_rotation(found_node)
        else:
            self.left_rotation(found_node)

        self.delete(found_node)

        return
