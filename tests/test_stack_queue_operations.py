import unittest

from mylib.animalShelter import AnimalShelter
from mylib.stackNode import StackNode
from mylib.queueViaStack import QueueViaStacks
from mylib.setOfStacks import SetOfStacks, ShiftingSetOfStacks
from mylib.stackMin import StackMinHolder
from mylib.stackOperations import sort_stack


class TestStackMin(unittest.TestCase):
    def test_correct_case(self):
        s = StackMinHolder()
        s.push(1)
        self.assertEqual(s.min(), 1)

        s.push(2)
        self.assertEqual(s.min(), 1)

        s.push(0)
        self.assertEqual(s.min(), 0)

        s.pop()
        self.assertEqual(s.min(), 1)
        s.pop()
        s.pop()

        with self.assertRaises(Exception) as context:
            s.min()

        self.assertTrue('Empty stack' in str(context.exception))

    def test_empty_stack(self):
        s = StackMinHolder()
        with self.assertRaises(Exception) as context:
            s.min()

        self.assertTrue('Empty stack' in str(context.exception))

    def test_multiple_min(self):
        s = StackMinHolder()
        s.push(3)
        self.assertEqual(s.min(), 3)

        s.push(2)
        self.assertEqual(s.min(), 2)

        s.push(2)
        self.assertEqual(s.min(), 2)

        s.pop()
        self.assertEqual(s.min(), 2)
        s.pop()
        self.assertEqual(s.min(), 3)
        s.pop()


class TestSetOfStacks(unittest.TestCase):
    def test_correct_case(self):
        s = SetOfStacks(2)
        s.push(1)
        self.assertEqual(s.peek(), 1)

        s.push(2)
        self.assertEqual(s.peek(), 2)
        self.assertEqual(s.size(), 2)

        s.push(0)
        self.assertEqual(s.peek(), 0)
        self.assertEqual(s.size(), 3)

        self.assertEqual(s.pop(), 0)
        self.assertEqual(s.peek(), 2)
        self.assertEqual(s.size(), 2)
        s.pop()
        s.pop()
        self.assertEqual(s.size(), 0)

        with self.assertRaises(Exception) as context:
            s.pop()

        self.assertTrue('Empty stack' in str(context.exception))

    def test_empty_stack(self):
        s = StackMinHolder()
        with self.assertRaises(Exception) as context:
            s.peek()

        self.assertTrue('Empty stack' in str(context.exception))


class TestShiftingSetOfStacks(unittest.TestCase):
    def test_correct_case(self):
        s = ShiftingSetOfStacks(2)
        s.push(1)
        self.assertEqual(s.peek(), 1)

        s.push(2)
        self.assertEqual(s.peek(), 2)
        self.assertEqual(s.size(), 2)

        s.push(0)
        self.assertEqual(s.peek(), 0)
        self.assertEqual(s.size(), 3)
        s.push(3)
        s.push(14)
        s.push(1)

        s.push(13)
        s.push(9)
        self.assertEqual(len(s.stacks), 4)

        self.assertEqual(s.pop_at(2), 3)
        self.assertEqual(s.peek(), 9)
        s.pop()
        self.assertEqual(len(s.stacks), 3)
        self.assertEqual(s.pop_at(2), 14)
        self.assertEqual(s.size(), 5)
        self.assertEqual(s.pop_at(3), 13)
        self.assertEqual(len(s.stacks), 2)
        self.assertEqual(s.peek(), 1)

        s.push(11)
        self.assertEqual(s.peek(), 11)

        sized = s.size()
        for i in range(sized):
            s.pop()

        with self.assertRaises(Exception) as context:
            s.pop()

        self.assertTrue('Empty stack' in str(context.exception))

    def test_empty_stack(self):
        s = ShiftingSetOfStacks(2)
        with self.assertRaises(Exception) as context:
            s.peek()

        self.assertTrue('Empty stack' in str(context.exception))


class TestQueueViaStacks(unittest.TestCase):
    def test_correct_case(self):
        s = QueueViaStacks()
        s.push(1)
        self.assertEqual(s.peek(), 1)

        s.push(2)
        self.assertEqual(s.peek(), 1)
        self.assertEqual(s.size(), 2)
        s.push(3)

        self.assertEqual(s.pop(), 1)
        self.assertEqual(s.peek(), 2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.peek(), 3)
        self.assertEqual(s.pop(), 3)
        self.assertTrue(s.is_empty())
        with self.assertRaises(Exception) as context:
            s.pop()

        self.assertTrue('Empty stack' in str(context.exception))

        s.push(12)
        s.push(13)
        self.assertEqual(s.peek(), 12)
        self.assertEqual(s.pop(), 12)

    def test_empty_stack(self):
        s = QueueViaStacks()
        with self.assertRaises(Exception) as context:
            s.peek()

        self.assertTrue('Empty stack' in str(context.exception))


class TestSortStack(unittest.TestCase):
    def test_correct_case(self):
        s = StackNode()
        s.push(7)
        s.push(5)
        s.push(10)
        s.push(1)
        s.push(3)
        s.push(12)
        s.push(8)

        tested = sort_stack(s)
        answer = [12, 10, 8, 7, 5, 3, 1]
        for i in range(7):
            self.assertEqual(tested.pop(), answer[i])

    def test_empty_case(self):
        s = StackNode()
        self.assertEqual(sort_stack(s), s)

    def test_none_case(self):
        self.assertEqual(sort_stack(None), None)

    def test_special_case(self):
        # one item stack
        s = StackNode()
        s.push(1)
        self.assertEqual(sort_stack(s).pop(), 1)


class TestAnimalShelter(unittest.TestCase):
    def test_correct_case(self):
        a = AnimalShelter()
        a.enqueue('dog')
        self.assertEqual(a.peek().time, 1)

        a.enqueue('CAT')
        self.assertEqual(a.peek().animal, 'Dog')

        a.enqueue('cat')
        a.enqueue('cat')
        a.enqueue('Dog')

        self.assertEqual(a.dequeue_any().time, 1)
        self.assertEqual(a.dequeue_any().animal, 'Cat')
        self.assertEqual(a.dequeue_cat().time, 3)
        self.assertEqual(a.dequeue_dog().time, 5)
        self.assertEqual(a.dequeue_any().time, 4)
        self.assertTrue(a.is_empty())

        with self.assertRaises(Exception) as context:
            a.dequeue_any()

        self.assertTrue('Empty shelter' in str(context.exception))

    def test_empty_stack(self):
        a = AnimalShelter()
        with self.assertRaises(Exception) as context:
            a.peek()

        self.assertTrue('Empty shelter' in str(context.exception))
