import unittest

from mylib.treeTraversal import *


class TestInOrder(unittest.TestCase):
    def test_correctness(self):
        answer = [1, 2, 3]
        a = Node(2)
        b = Node(1, a)
        c = Node(3, a)
        a.left = b
        a.right = c

        self.assertEqual(answer, in_order_traversal(a))

    def test_big_tree(self):
        answer = [1, 2, 3, 4, 5, 6, 7]
        # h=1
        a = Node(4)
        b = Node(2, a)
        c = Node(6, a)
        a.left = b
        a.right = c

        # h=2
        d = Node(1, b)
        e = Node(3, b)
        b.left = d
        b.right = e

        f = Node(5, c)
        g = Node(7, c)
        c.left = f
        c.right = g

        self.assertEqual(answer, in_order_traversal(a))

    def test_empty(self):
        self.assertEqual([], in_order_traversal(None))

    def test_one_node(self):
        answer = [12]
        a = Node(12)
        self.assertEqual(answer, in_order_traversal(a))

    def test_one_child(self):
        # left
        answer = [1, 2]
        a = Node(2)
        b = Node(1, a)
        a.left = b
        self.assertEqual(answer, in_order_traversal(a))

        # right
        answer = [2, 3]
        a = Node(2)
        c = Node(3, a)
        a.right = c
        self.assertEqual(answer, in_order_traversal(a))


class TestPreOrder(unittest.TestCase):
    def test_correctness(self):
        answer = [1, 2, 3]
        a = Node(1)
        b = Node(2, a)
        c = Node(3, a)
        a.left = b
        a.right = c

        self.assertEqual(answer, pre_order_traversal(a))

    def test_big_tree(self):
        answer = [4, 2, 1, 3, 6, 5, 7]
        # h=1
        a = Node(4)
        b = Node(2, a)
        c = Node(6, a)
        a.left = b
        a.right = c

        # h=2
        d = Node(1, b)
        e = Node(3, b)
        b.left = d
        b.right = e

        f = Node(5, c)
        g = Node(7, c)
        c.left = f
        c.right = g

        self.assertEqual(answer, pre_order_traversal(a))

    def test_empty(self):
        self.assertEqual([], pre_order_traversal(None))

    def test_one_node(self):
        answer = [12]
        a = Node(12)
        self.assertEqual(answer, pre_order_traversal(a))

    def test_one_child(self):
        # left
        answer = [1, 2]
        a = Node(1)
        b = Node(2, a)
        a.left = b
        self.assertEqual(answer, pre_order_traversal(a))

        # right
        answer = [2, 3]
        a = Node(2)
        c = Node(3, a)
        a.right = c
        self.assertEqual(answer, pre_order_traversal(a))


class TestPostOrder(unittest.TestCase):
    def test_correctness(self):
        answer = [2, 3, 1]
        a = Node(1)
        b = Node(2, a)
        c = Node(3, a)
        a.left = b
        a.right = c

        self.assertEqual(answer, post_order_traversal(a))

    def test_big_tree(self):
        answer = [1, 3, 2, 5, 7, 6, 4]
        # h=1
        a = Node(4)
        b = Node(2, a)
        c = Node(6, a)
        a.left = b
        a.right = c

        # h=2
        d = Node(1, b)
        e = Node(3, b)
        b.left = d
        b.right = e

        f = Node(5, c)
        g = Node(7, c)
        c.left = f
        c.right = g

        self.assertEqual(answer, post_order_traversal(a))

    def test_empty(self):
        self.assertEqual([], post_order_traversal(None))

    def test_one_node(self):
        answer = [12]
        a = Node(12)
        self.assertEqual(answer, post_order_traversal(a))

    def test_one_child(self):
        # left
        answer = [2, 1]
        a = Node(1)
        b = Node(2, a)
        a.left = b
        self.assertEqual(answer, post_order_traversal(a))

        # right
        answer = [3, 2]
        a = Node(2)
        c = Node(3, a)
        a.right = c
        self.assertEqual(answer, post_order_traversal(a))
