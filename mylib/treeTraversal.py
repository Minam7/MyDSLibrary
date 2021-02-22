class Node:
    def __init__(self, value_in, parent_in=None):
        self.key = value_in
        self.parent = parent_in
        self.left = None
        self.right = None

    def __str__(self):
        if self.parent:
            return str(self.parent) + '->' + self.key
        else:
            return self.key


def in_order_traversal(root_in):
    orders = []
    if root_in is not None:
        if root_in.left is not None:
            orders.extend(in_order_traversal(root_in.left))

        orders.append(root_in.key)

        if root_in.right is not None:
            orders.extend(in_order_traversal(root_in.right))

    return orders


def pre_order_traversal(root_in):
    orders = []
    if root_in is not None:
        orders.append(root_in.key)

        if root_in.left is not None:
            orders.extend(pre_order_traversal(root_in.left))

        if root_in.right is not None:
            orders.extend(pre_order_traversal(root_in.right))
    return orders


def post_order_traversal(root_in):
    orders = []

    if root_in is not None:
        if root_in.left is not None:
            orders.extend(post_order_traversal(root_in.left))

        if root_in.right is not None:
            orders.extend(post_order_traversal(root_in.right))

        orders.append(root_in.key)
    return orders
