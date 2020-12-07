class Node:
    def __init__(self, key_in, parent_in):
        self.key = key_in
        self.parent = parent_in
        self.left_child = None
        self.right_child = None

    def __str__(self):  # Returns the path from root to node
        if self.parent:
            return str(self.parent) + "->" + str(self.key)
        else:
            return str(self.key)

    def summary(self):
        print("----------------Node Summary----------------")
        print("Parent:", self.parent, "Key:", self.key)
        print("Left Child:", self.left_child, "Right Child:", self.right_child)
        print()
        return


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, node_in):
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

    def build_tree(self, array_in):
        if len(array_in) == 0:
            return

        self.root = Node(array_in[0], None)

        for i in range(1, len(array_in)):
            new_node = Node(array_in[i], None)
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

    def delete(self, item_in):
        found_node = self.find(item_in)

        if found_node is None:
            return

        if found_node.left_child is None and found_node.right_child is None:
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
        next_larger_item = self.next_larger(found_node)
        item_key = next_larger_item.key
        self.delete(next_larger_item.key)
        found_node.key = item_key

        return

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


class AugmentedNode(Node):
    def __init__(self, key_in, parent_in):
        super().__init__(key_in, parent_in)
        self.size = 1

    def update_size(self):
        if self.left_child is None:
            if self.right_child is None:
                self.size = 1
                return
            # right child is not none but left child is none
            self.size = 1 + self.right_child.size
            return

        if self.right_child is None:
            # right child is none but left child is not none
            self.size = 1 + self.left_child.size
            return

            # both nodes are not none
        self.size = 1 + self.right_child.size + self.left_child.size
        return

    def summary(self):
        print("----------------Node Summary----------------")
        print("Parent:", self.parent, "Key:", self.key)
        print("Size:", self.size)
        print("Left Child:", self.left_child, "Right Child:", self.right_child)
        print()
        return


class AugmentedBinarySearchTree(BinarySearchTree):
    def insert(self, node_in):
        BinarySearchTree.insert(self, node_in)
        walker = node_in
        while walker is not None:
            walker.update_size()
            walker = walker.parent
        return

    def build_tree(self, array_in):
        if len(array_in) == 0:
            return

        self.root = AugmentedNode(array_in[0], None)

        for i in range(1, len(array_in)):
            new_node = AugmentedNode(array_in[i], None)
            self.insert(new_node)
