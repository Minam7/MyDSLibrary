import unittest
from collections import deque

from mylib.binarySearchTree import BinarySearchTree, Node
from mylib.treeOperations import bst_sequence, contains_tree, path_with_sum
from mylib.treeOperations import minimal_tree, list_of_depth, check_balanced, validate_bst, first_common_ancestor


class TestMinimalTree(unittest.TestCase):
    def test_odd_case(self):
        test_root = minimal_tree([1, 2, 3, 4, 5])

        self.assertEqual(test_root.key, 3)
        self.assertEqual(test_root.left_child.key, 2)
        self.assertEqual(test_root.left_child.left_child.key, 1)
        self.assertEqual(test_root.right_child.key, 5)
        self.assertEqual(test_root.right_child.left_child.key, 4)

    def test_even_case(self):
        test_root = minimal_tree([1, 2, 3, 4, 5, 6, 7, 8])

        self.assertEqual(test_root.key, 5)
        self.assertEqual(test_root.left_child.key, 3)
        self.assertEqual(test_root.left_child.left_child.key, 2)
        self.assertEqual(test_root.left_child.left_child.left_child.key, 1)
        self.assertEqual(test_root.left_child.right_child.key, 4)
        self.assertEqual(test_root.right_child.key, 7)
        self.assertEqual(test_root.right_child.left_child.key, 6)
        self.assertEqual(test_root.right_child.right_child.key, 8)

    def test_empty_case(self):
        test_root = minimal_tree([])
        self.assertEqual(test_root, None)

    def test_none_case(self):
        self.assertEqual(minimal_tree(None), None)


class TestListOfDepth(unittest.TestCase):
    def setUp(self) -> None:
        self.bst = BinarySearchTree()
        self.bst.build_tree([4, 2, 7, 12, 9, 0, -2, 5, 14, 1, -3])

    def test_correctness(self):
        lists = list_of_depth(self.bst)

        answer_array = [[4], [2, 7], [0, 5, 12], [-2, 1, 9, 14], [-3]]

        for i in range(len(lists)):
            for j in range(len(lists[i])):
                self.assertEqual(lists[i][j].key, answer_array[i][j])

    def test_none_case(self):
        self.assertEqual(None, list_of_depth(None))
        self.assertEqual(None, list_of_depth(BinarySearchTree()))


class TestCheckBalanced(unittest.TestCase):
    def test_balanced_tree_case(self):
        bst = BinarySearchTree()
        bst.build_tree([4, 3, 5])
        self.assertTrue(check_balanced(bst))

        bst = BinarySearchTree()
        bst.build_tree([6, 3, 9, 1, 5, 7, 11])
        self.assertTrue(check_balanced(bst))

        bst = BinarySearchTree()
        bst.build_tree([6, 3, 9, 1, 5, 7, 11, 13])
        self.assertTrue(check_balanced(bst))

    def test_unbalanced_tree_case(self):
        bst = BinarySearchTree()
        bst.build_tree([1, 2, 3, 4, 5, 6])
        self.assertFalse(check_balanced(bst))

        bst = BinarySearchTree()
        bst.build_tree([6, 3, 9, 1, 5, 7, 11, 13, 15])
        self.assertFalse(check_balanced(bst))

        bst = BinarySearchTree()
        bst.build_tree([6, 2, 9, 3, 4, 5, 7, 11, 13, 15])
        self.assertFalse(check_balanced(bst))

    def test_one_node_case(self):
        bst = BinarySearchTree()
        bst.build_tree([1])
        self.assertTrue(check_balanced(bst))

    def test_none_case_case(self):
        self.assertTrue(check_balanced(None))
        self.assertTrue(check_balanced(BinarySearchTree()))


class TestValidateBST(unittest.TestCase):
    def test_correct_case(self):
        bst = BinarySearchTree()
        bst.build_tree([4, 3, 5])
        self.assertTrue(validate_bst(bst))

        bst = BinarySearchTree()
        bst.build_tree([6, 3, 9, 1, 5, 7, 11, 13, 15])
        self.assertTrue(validate_bst(bst))

    def test_incorrect_case(self):
        bst = BinarySearchTree()
        bst.build_tree([4, 3, 5])
        # one error in root
        node = bst.find(4)
        node.key = -1
        self.assertFalse(validate_bst(bst))

        bst = BinarySearchTree()
        bst.build_tree([6, 3, 9, 1, 5, 7, 11, 13, 15])
        # one error
        bad_node = bst.find(5)
        bad_node.key = -1
        self.assertFalse(validate_bst(bst))
        # two error
        node = bst.find(11)
        node.key = -12
        self.assertFalse(validate_bst(bst))
        # three error
        node = bst.find(6)
        node.key = -20
        self.assertFalse(validate_bst(bst))

    def test_unbalanced_tree_case(self):
        bst = BinarySearchTree()
        bst.build_tree([1, 2, 3, 4, 5, 6])
        self.assertTrue(validate_bst(bst))

        # one error
        node = bst.find(3)
        node.key = -3
        self.assertFalse(validate_bst(bst))

        # two error
        node = bst.find(6)
        node.key = -6
        self.assertFalse(validate_bst(bst))

    def test_one_node(self):
        bst = BinarySearchTree()
        bst.build_tree([1])
        self.assertTrue(validate_bst(bst))

    def test_none_case(self):
        self.assertTrue(validate_bst(None))
        self.assertTrue(validate_bst(BinarySearchTree()))


class TestFirstCommonAncestor(unittest.TestCase):
    def test_different_size_case(self):
        # root is answer
        bst = BinarySearchTree()
        bst.build_tree([4, 3, 5])
        self.assertEqual(first_common_ancestor(bst, bst.find(3), bst.find(5)), bst.find(4))

        # subtree is answer
        bst = BinarySearchTree()
        bst.build_tree([6, 3, 9, 1, 5, 7, 11, 13, 15])
        self.assertEqual(first_common_ancestor(bst, bst.find(7), bst.find(11)), bst.find(9))

    def test_on_same_side_case(self):
        bst = BinarySearchTree()
        bst.build_tree([4, 3, 5, 6, 7])
        self.assertEqual(first_common_ancestor(bst, bst.find(7), bst.find(5)), bst.find(5))

    def test_same_node_case(self):
        bst = BinarySearchTree()
        bst.build_tree([4, 3, 5, 6, 7])
        self.assertEqual(first_common_ancestor(bst, bst.find(5), bst.find(5)), bst.find(5))

    def test_non_existant_node_case(self):
        bst = BinarySearchTree()
        bst.build_tree([4, 3, 5, 6, 7])
        self.assertEqual(first_common_ancestor(bst, bst.find(5), Node(12, None)), None)

    def test_one_node_case(self):
        bst = BinarySearchTree()
        bst.build_tree([6])
        self.assertEqual(first_common_ancestor(bst, bst.find(6), bst.find(6)), bst.find(6))

    def test_none_case(self):
        self.assertEqual(first_common_ancestor(None, '', ''), None)
        self.assertEqual(first_common_ancestor(BinarySearchTree(), '', ''), None)

        bst = BinarySearchTree()
        bst.build_tree([6])
        self.assertEqual(first_common_ancestor(bst, None, ''), None)
        self.assertEqual(first_common_ancestor(bst, None, None), None)
        self.assertEqual(first_common_ancestor(bst, '', None), None)


class TestBstSequence(unittest.TestCase):
    def test_simple_case(self):
        bst = BinarySearchTree()
        bst.build_tree([2, 1, 3])
        seq = bst_sequence(bst)
        answer = [deque([2, 1, 3]), deque([2, 3, 1])]
        for i in range(len(seq)):
            self.assertEqual(seq[i], answer[i])

    def test_one_node(self):
        bst = BinarySearchTree()
        bst.build_tree([2])
        seq = bst_sequence(bst)
        answer = [deque([2])]
        for i in range(len(seq)):
            self.assertEqual(seq[i], answer[i])

    def test_none_case(self):
        self.assertEqual([], bst_sequence(None))
        self.assertEqual([], bst_sequence(BinarySearchTree()))


class TestContainsTree(unittest.TestCase):
    def setUp(self) -> None:
        self.big_bst = BinarySearchTree()
        self.big_bst.build_tree([4, 2, 7, -3, 3, 6, 11, 5, 9, 10])

    def test_one_node(self):
        small_bst = BinarySearchTree()
        small_bst.build_tree([10])
        self.assertTrue(contains_tree(self.big_bst, small_bst))

        small_bst = BinarySearchTree()
        small_bst.build_tree([2])
        self.assertFalse(contains_tree(self.big_bst, small_bst))

    def test_true_case(self):
        small_bst = BinarySearchTree()
        small_bst.build_tree([2, -3, 3])
        self.assertTrue(contains_tree(self.big_bst, small_bst))

        self.assertTrue(contains_tree(self.big_bst, self.big_bst))

        small_bst = BinarySearchTree()
        small_bst.build_tree([9, 10])
        self.assertTrue(contains_tree(self.big_bst, small_bst))

    def test_false_case(self):
        small_bst = BinarySearchTree()
        small_bst.build_tree([2, -3, 4])
        self.assertFalse(contains_tree(self.big_bst, small_bst))

        small_bst = BinarySearchTree()
        small_bst.build_tree([9])
        self.assertFalse(contains_tree(self.big_bst, small_bst))

        small_bst = BinarySearchTree()
        small_bst.build_tree([33])
        self.assertFalse(contains_tree(self.big_bst, small_bst))


class TestPathWithSum(unittest.TestCase):
    def setUp(self) -> None:
        self.bst = BinarySearchTree()
        self.bst.build_tree([4, 1, 7, -3, 3, 2, 6, 11, 5, 9, 10])

        cn = self.bst.find(1)
        wn = self.bst.find(7)

        cn.key = 2
        cn.right_child.key = -2
        cn.right_child.left_child.key = 4

        wn.right_child.left_child.right_child.key = -10
        wn.left_child.left_child.key = -14

    def test_existent_normal_case(self):
        self.assertEqual(path_with_sum(self.bst, 4), 4)
        self.assertEqual(path_with_sum(self.bst, 13), 1)
        self.assertEqual(path_with_sum(self.bst, -1), 3)

    def test_non_existent_case(self):
        self.assertEqual(path_with_sum(self.bst, -18), 0)

    def test_none_case(self):
        self.assertEqual(path_with_sum(None, 1), 0)
        self.assertEqual(path_with_sum(BinarySearchTree(), 12), 0)
