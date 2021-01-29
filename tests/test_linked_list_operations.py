import unittest

from mylib.linkedList import SingleLink, Node
from mylib.linkedListOperations import delete_middle_node
from mylib.linkedListOperations import k_to_last
from mylib.linkedListOperations import linked_partition
from mylib.linkedListOperations import list_intersect
from mylib.linkedListOperations import list_loop_detection
from mylib.linkedListOperations import list_palindrome
from mylib.linkedListOperations import remove_dups
from mylib.linkedListOperations import sum_list
from mylib.linkedListOperations import sum_list_rev


class TestRemoveDuplicate(unittest.TestCase):
    def test_non_repetitive_case(self):
        # non repetitive
        l_list = SingleLink()
        l_list.insert_after(1, None)
        l_list.insert_after(2, 1)
        l_list.insert_after(3, 2)
        l_list.insert_after(12, 1)
        remove_dups(l_list)
        self.assertEqual(str(l_list.head), '1->12->2->3->None')

        # single case
        l_list = SingleLink()
        l_list.insert_after(1, None)
        remove_dups(l_list)
        self.assertEqual(str(l_list.head), '1->None')

    def test_repetitive_case(self):
        # repetitive case
        l_list = SingleLink()
        l_list.insert_after(1, None)
        l_list.insert_after(2, 1)
        l_list.insert_after(3, 2)
        l_list.insert_after(2, 1)
        self.assertEqual(str(l_list.head), '1->2->2->3->None')
        remove_dups(l_list)
        self.assertEqual(str(l_list.head), '1->2->3->None')

    def test_empty_case(self):
        l_list = SingleLink()
        remove_dups(l_list)
        self.assertEqual(l_list.head, None)

    def test_none_case(self):
        # none case
        l_list = None
        remove_dups(l_list)
        self.assertEqual(l_list, None)

    def test_special_case(self):
        # one element
        l_list = SingleLink()
        l_list.insert_after(1, None)
        self.assertEqual(str(l_list.head), '1->None')
        remove_dups(l_list)
        self.assertEqual(str(l_list.head), '1->None')

        # all same
        l_list = SingleLink()
        l_list.insert_after(1, None)
        l_list.insert_after(1, 1)
        l_list.insert_after(1, 1)
        self.assertEqual(str(l_list.head), '1->1->1->None')
        remove_dups(l_list)
        self.assertEqual(str(l_list.head), '1->None')


class TestKthFromLast(unittest.TestCase):
    def test_non_repetitive_case(self):
        # same as k length
        l_list = SingleLink()
        l_list.insert_after(1, None)
        l_list.insert_after(2, 1)
        l_list.insert_after(3, 2)
        l_list.insert_after(6, 3)
        l_list.insert_after(4, 6)
        self.assertEqual(str(k_to_last(l_list, k_in=4)), str(l_list.head))

        # more than k length
        l_list.insert_after(5, 4)
        self.assertEqual(str(k_to_last(l_list, k_in=4)), str(l_list.head.next))

        # less than k length
        self.assertEqual(k_to_last(l_list, k_in=10), None)

    def test_repetitive_case(self):
        # repetitive case
        l_list = SingleLink()
        l_list.insert_after(1, None)
        l_list.insert_after(2, 1)
        l_list.insert_after(3, 2)
        l_list.insert_after(2, 1)
        self.assertEqual(str(k_to_last(l_list, k_in=2)), '2->2->3->None')

    def test_empty_case(self):
        l_list = SingleLink()
        self.assertEqual(k_to_last(l_list, k_in=0), None)

    def test_none_case(self):
        # none case
        l_list = None
        self.assertEqual(k_to_last(l_list, k_in=0), None)

    def test_special_case(self):
        # one element
        l_list = SingleLink()
        l_list.insert_after(1, None)
        self.assertEqual(str(k_to_last(l_list, k_in=0)), '1->None')

        # more than one element zero length from last!
        l_list = SingleLink()
        l_list.insert_after(1, None)
        l_list.insert_after(2, 1)
        l_list.insert_after(3, 2)
        l_list.insert_after(6, 3)
        l_list.insert_after(4, 6)
        self.assertEqual(str(k_to_last(l_list, k_in=0)), '4->None')


class TestDeleteMiddleNode(unittest.TestCase):
    def test_middle_case(self):
        # delete middles in no order
        l_list = SingleLink()
        l_list.insert_after(1, None)
        l_list.insert_after(2, 1)
        l_list.insert_after(3, 2)
        l_list.insert_after(6, 3)
        l_list.insert_after(4, 6)
        delete_middle_node(l_list.find(6))
        self.assertEqual(str(l_list.head), '1->2->3->4->None')
        delete_middle_node(l_list.find(2))
        self.assertEqual(str(l_list.head), '1->3->4->None')
        delete_middle_node(l_list.find(3))
        self.assertEqual(str(l_list.head), '1->4->None')

    def test_none_case(self):
        # none case
        l_list = None
        delete_middle_node(l_list)
        self.assertEqual(l_list, None)

    def test_special_case(self):
        # last node
        l_list = SingleLink()
        l_list.insert_after(1, None)
        l_list.insert_after(2, 1)
        with self.assertRaises(Exception) as context:
            delete_middle_node(l_list.find(2))

        self.assertTrue('You can not delete the last node.' in str(context.exception))


class TestLinkedPartition(unittest.TestCase):
    def test_correct_case(self):
        # correct case
        l_list = SingleLink()
        l_list.insert_after(3, None)
        l_list.insert_after(5, 3)
        l_list.insert_after(8, 5)
        l_list.insert_after(6, 8)
        l_list.insert_after(10, 6)
        l_list.insert_after(2, 10)
        l_list.insert_after(1, 2)
        linked_partition(l_list, x_in=5)
        self.assertEqual(str(l_list.head), '3->2->1->6->10->5->8->None')

        # non present
        l_list = SingleLink()
        l_list.insert_after(3, None)
        l_list.insert_after(5, 3)
        l_list.insert_after(8, 5)
        l_list.insert_after(6, 8)
        l_list.insert_after(10, 6)
        l_list.insert_after(2, 10)
        l_list.insert_after(1, 2)
        linked_partition(l_list, x_in=9)
        self.assertEqual(str(l_list.head), '3->5->8->6->2->1->10->None')

        # other case
        l_list = SingleLink()
        l_list.insert_after(3, None)
        l_list.insert_after(5, 3)
        l_list.insert_after(8, 5)
        l_list.insert_after(6, 8)
        l_list.insert_after(10, 6)
        l_list.insert_after(2, 10)
        l_list.insert_after(1, 2)
        linked_partition(l_list, x_in=10)
        self.assertEqual(str(l_list.head), '3->5->8->6->2->1->10->None')

    def test_empty_case(self):
        l_list = SingleLink()
        linked_partition(l_list, x_in=10)
        self.assertEqual(l_list.head, None)

    def test_none_case(self):
        # none case
        l_list = None
        linked_partition(l_list, x_in=10)
        self.assertEqual(l_list, None)

    def test_special_case(self):
        # no change for big x
        l_list = SingleLink()
        l_list.insert_after(3, None)
        l_list.insert_after(5, 3)
        l_list.insert_after(8, 5)
        l_list.insert_after(6, 8)
        l_list.insert_after(10, 6)
        l_list.insert_after(2, 10)
        l_list.insert_after(1, 2)
        linked_partition(l_list, x_in=15)
        self.assertEqual(str(l_list.head), '3->5->8->6->10->2->1->None')

        # no change for small x
        linked_partition(l_list, x_in=0)
        self.assertEqual(str(l_list.head), '3->5->8->6->10->2->1->None')


class TestSumListRev(unittest.TestCase):
    def test_same_size(self):
        # same size
        l_list1 = SingleLink()
        l_list1.insert_after(7, None)
        l_list1.insert_after(1, 7)
        l_list1.insert_after(6, 1)
        l_list2 = SingleLink()
        l_list2.insert_after(5, None)
        l_list2.insert_after(9, 5)
        l_list2.insert_after(2, 9)
        self.assertEqual(str(sum_list_rev(l_list1, l_list2).head), '2->1->9->None')

    def test_last_carry(self):
        # test last carry
        l_list1 = SingleLink()
        l_list1.insert_after(9, None)
        l_list1.insert_after(7, 9)
        l_list1.insert_after(8, 7)
        l_list2 = SingleLink()
        l_list2.insert_after(6, None)
        l_list2.insert_after(8, 6)
        l_list2.insert_after(5, 8)
        self.assertEqual(str(sum_list_rev(l_list1, l_list2).head), '5->6->4->1->None')

    def test_different_size(self):
        # different size first larger
        l_list1 = SingleLink()
        l_list1.insert_after(7, None)
        l_list1.insert_after(1, 7)
        l_list1.insert_after(6, 1)
        l_list1.insert_after(3, 6)

        l_list2 = SingleLink()
        l_list2.insert_after(5, None)
        l_list2.insert_after(9, 5)
        l_list2.insert_after(2, 9)
        self.assertEqual(str(sum_list_rev(l_list1, l_list2).head), '2->1->9->3->None')

        # different size second larger
        l_list1 = SingleLink()
        l_list1.insert_after(7, None)
        l_list1.insert_after(1, 7)
        l_list1.insert_after(6, 1)

        l_list2 = SingleLink()
        l_list2.insert_after(5, None)
        l_list2.insert_after(9, 5)
        l_list2.insert_after(2, 9)
        l_list2.insert_after(3, 2)
        l_list2.insert_after(7, 3)
        self.assertEqual(str(sum_list_rev(l_list1, l_list2).head), '2->1->9->3->7->None')

    def test_none_case(self):
        # none
        self.assertEqual(sum_list_rev(None, None), None)
        l_list1 = SingleLink()
        self.assertEqual(sum_list_rev(l_list1, None), None)


class TestSumList(unittest.TestCase):
    def test_same_size(self):
        # same size
        l_list1 = SingleLink()
        l_list1.insert_after(6, None)
        l_list1.insert_after(1, 6)
        l_list1.insert_after(7, 1)
        l_list2 = SingleLink()
        l_list2.insert_after(2, None)
        l_list2.insert_after(9, 2)
        l_list2.insert_after(5, 9)
        self.assertEqual(str(sum_list(l_list1, l_list2).head), '9->1->2->None')

    def test_last_carry(self):
        # test last carry
        l_list1 = SingleLink()
        l_list1.insert_after(8, None)
        l_list1.insert_after(7, 8)
        l_list1.insert_after(9, 7)
        l_list2 = SingleLink()
        l_list2.insert_after(5, None)
        l_list2.insert_after(8, 5)
        l_list2.insert_after(6, 8)
        self.assertEqual(str(sum_list(l_list1, l_list2).head), '1->4->6->5->None')

    def test_different_size(self):
        # different size first larger
        l_list1 = SingleLink()
        l_list1.insert_after(7, None)
        l_list1.insert_after(1, 7)
        l_list1.insert_after(6, 1)
        l_list1.insert_after(3, 6)

        l_list2 = SingleLink()
        l_list2.insert_after(5, None)
        l_list2.insert_after(9, 5)
        l_list2.insert_after(2, 9)
        self.assertEqual(str(sum_list(l_list1, l_list2).head), '7->7->5->5->None')

        # different size second larger
        l_list1 = SingleLink()
        l_list1.insert_after(7, None)
        l_list1.insert_after(1, 7)
        l_list1.insert_after(6, 1)

        l_list2 = SingleLink()
        l_list2.insert_after(5, None)
        l_list2.insert_after(9, 5)
        l_list2.insert_after(2, 9)
        l_list2.insert_after(3, 2)
        l_list2.insert_after(7, 3)
        self.assertEqual(str(sum_list(l_list1, l_list2).head), '5->9->9->5->3->None')

    def test_none_case(self):
        # none
        self.assertEqual(sum_list(None, None), None)
        l_list1 = SingleLink()
        self.assertEqual(sum_list(l_list1, None), None)


class TestListPermutation(unittest.TestCase):
    def test_true_case(self):
        # true odd case
        l_list = SingleLink()
        l_list.insert_after(0, None)
        l_list.insert_after(1, 0)
        l_list.insert_after(2, 1)
        l_list.insert_after(3, 2)
        # adding rest
        last_node = l_list.find(3)
        new_node = Node(2, None)
        last_node.next = new_node
        last_node = new_node
        new_node = Node(1, None)
        last_node.next = new_node
        last_node = new_node
        new_node = Node(0, None)
        last_node.next = new_node
        self.assertTrue(list_palindrome(l_list))

        # true even case
        l_list = SingleLink()
        l_list.insert_after(0, None)
        l_list.insert_after(1, 0)
        l_list.insert_after(2, 1)
        # adding rest
        last_node = l_list.find(2)
        new_node = Node(2, None)
        last_node.next = new_node
        last_node = new_node
        new_node = Node(1, None)
        last_node.next = new_node
        last_node = new_node
        new_node = Node(0, None)
        last_node.next = new_node
        self.assertTrue(list_palindrome(l_list))

    def test_false_case(self):
        # true odd case
        l_list = SingleLink()
        l_list.insert_after(0, None)
        l_list.insert_after(1, 0)
        l_list.insert_after(22, 1)
        l_list.insert_after(3, 22)
        # adding rest
        last_node = l_list.find(3)
        new_node = Node(2, None)
        last_node.next = new_node
        last_node = new_node
        new_node = Node(1, None)
        last_node.next = new_node
        last_node = new_node
        new_node = Node(0, None)
        last_node.next = new_node
        self.assertFalse(list_palindrome(l_list))

        # true even case
        l_list = SingleLink()
        l_list.insert_after(0, None)
        l_list.insert_after(1, 0)
        l_list.insert_after(2, 1)
        # adding rest
        last_node = l_list.find(2)
        new_node = Node(2, None)
        last_node.next = new_node
        last_node = new_node
        new_node = Node(11, None)
        last_node.next = new_node
        last_node = new_node
        new_node = Node(0, None)
        last_node.next = new_node
        self.assertFalse(list_palindrome(l_list))

    def test_more_difference(self):
        # true odd case
        l_list = SingleLink()
        l_list.insert_after(0, None)
        l_list.insert_after(1, 0)
        l_list.insert_after(22, 1)
        l_list.insert_after(3, 22)
        # adding rest
        last_node = l_list.find(3)
        new_node = Node(12, None)
        last_node.next = new_node
        last_node = new_node
        new_node = Node(1, None)
        last_node.next = new_node
        last_node = new_node
        new_node = Node(0, None)
        last_node.next = new_node
        self.assertFalse(list_palindrome(l_list))

    def test_none_case(self):
        # none
        self.assertTrue(list_palindrome(None))
        l_list = SingleLink()
        self.assertTrue(list_palindrome(l_list))


class TestIntersectionList(unittest.TestCase):
    def test_same_size(self):
        # same size
        l_list1 = SingleLink()
        l_list1.insert_after(0, None)
        l_list1.insert_after(1, 0)
        l_list1.insert_after(2, 1)

        # adding rest
        last_node = l_list1.find(2)
        same_node = Node(5, None)
        last_node.next = same_node
        l_list1.insert_after(6, 5)
        l_list1.insert_after(7, 6)
        l_list1.insert_after(8, 7)

        l_list2 = SingleLink()
        l_list2.insert_after(12, None)
        l_list2.insert_after(9, 12)
        l_list2.insert_after(14, 9)
        # adding rest
        last_node = l_list2.find(14)
        last_node.next = same_node

        answer = list_intersect(l_list1, l_list2)
        # none
        self.assertEqual(same_node, answer[0])
        self.assertTrue(answer[1])

    def test_incorrect_same_size(self):
        # same size
        l_list1 = SingleLink()
        l_list1.insert_after(0, None)
        l_list1.insert_after(1, 0)
        l_list1.insert_after(2, 1)

        l_list2 = SingleLink()
        l_list2.insert_after(12, None)
        l_list2.insert_after(9, 12)
        l_list2.insert_after(14, 9)

        answer = list_intersect(l_list1, l_list2)
        # none
        self.assertEqual(None, answer[0])
        self.assertFalse(answer[1])

    def test_different_size(self):
        # same size
        l_list1 = SingleLink()
        l_list1.insert_after(0, None)
        l_list1.insert_after(1, 0)
        l_list1.insert_after(2, 1)
        l_list1.insert_after(3, 2)

        # adding rest
        last_node = l_list1.find(3)
        same_node = Node(5, None)
        last_node.next = same_node
        l_list1.insert_after(6, 5)
        l_list1.insert_after(7, 6)
        l_list1.insert_after(8, 7)

        l_list2 = SingleLink()
        l_list2.insert_after(12, None)
        l_list2.insert_after(9, 12)
        l_list2.insert_after(14, 9)
        # adding rest
        last_node = l_list2.find(14)
        last_node.next = same_node

        answer = list_intersect(l_list1, l_list2)
        # none
        self.assertEqual(same_node, answer[0])
        self.assertTrue(answer[1])

    def test_incorrect_different_size(self):
        # same size
        l_list1 = SingleLink()
        l_list1.insert_after(0, None)
        l_list1.insert_after(1, 0)
        l_list1.insert_after(2, 1)
        l_list1.insert_after(3, 2)

        l_list2 = SingleLink()
        l_list2.insert_after(0, None)
        l_list2.insert_after(1, 0)
        l_list2.insert_after(2, 1)

        answer = list_intersect(l_list1, l_list2)
        # none
        self.assertEqual(None, answer[0])
        self.assertFalse(answer[1])

    def test_same_list(self):
        # same size
        l_list1 = SingleLink()
        l_list1.insert_after(0, None)
        l_list1.insert_after(1, 0)
        l_list1.insert_after(2, 1)
        l_list1.insert_after(3, 2)

        answer = list_intersect(l_list1, l_list1)
        # none
        self.assertEqual(l_list1.head, answer[0])
        self.assertTrue(answer[1])

    def test_same_value(self):
        # same size
        l_list1 = SingleLink()
        l_list1.insert_after(0, None)
        l_list1.insert_after(1, 0)
        l_list1.insert_after(2, 1)
        l_list1.insert_after(3, 2)

        l_list2 = SingleLink()
        l_list2.insert_after(0, None)
        l_list2.insert_after(1, 0)
        l_list2.insert_after(2, 1)
        l_list2.insert_after(3, 2)

        answer = list_intersect(l_list1, l_list2)
        # none
        self.assertEqual(None, answer[0])
        self.assertFalse(answer[1])

    def test_none_case(self):
        answer = list_intersect(None, None)
        # none
        self.assertEqual(answer[0], None)
        self.assertFalse(answer[1])

        l_list1 = SingleLink()
        answer = list_intersect(l_list1, None)
        self.assertEqual(answer[0], None)
        self.assertFalse(answer[1])


class TestListLoopDetection(unittest.TestCase):
    def test_correct_case(self):
        # find case
        l_list1 = SingleLink()
        l_list1.insert_after('A', None)
        l_list1.insert_after('B', 'A')
        l_list1.insert_after('C', 'B')
        l_list1.insert_after('D', 'C')
        l_list1.insert_after('E', 'D')
        find_node1 = l_list1.find('E')
        find_node2 = l_list1.find('C')
        find_node1.next = find_node2
        self.assertEqual(list_loop_detection(l_list1).value, 'C')

    def test_incorrect_case(self):
        # find case
        l_list1 = SingleLink()
        l_list1.insert_after('A', None)
        l_list1.insert_after('B', 'A')
        l_list1.insert_after('C', 'B')
        l_list1.insert_after('D', 'C')
        l_list1.insert_after('E', 'D')

        self.assertEqual(list_loop_detection(l_list1), None)

    def test_none_case(self):
        # none
        self.assertEqual(list_loop_detection(None), None)

        l_list1 = SingleLink()
        self.assertEqual(list_loop_detection(l_list1), None)


if __name__ == '__main__':
    unittest.main()
