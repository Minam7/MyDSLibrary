import unittest
from mylib.stringOperations import is_unique
from mylib.stringOperations import is_permutation
from mylib.stringOperations import urlify
from mylib.stringOperations import palindrome_permutation
from mylib.stringOperations import one_away
from mylib.stringOperations import string_compression
from mylib.stringOperations import rotate_matrix
from mylib.stringOperations import zero_matrix
from mylib.stringOperations import string_rotation


class TestIsUnique(unittest.TestCase):
    def test_correct_case(self):
        # correct case
        input_in = 'abDc'
        self.assertTrue(is_unique(input_in))

    def test_incorrect_case(self):
        # incorrect case
        input_in = 'aAca'
        self.assertFalse(is_unique(input_in))

    def test_empty_case(self):
        # empty case
        input_in = ''
        self.assertTrue(is_unique(input_in))

    def test_none_case(self):
        # none case
        input_in = None
        self.assertTrue(is_unique(input_in))

    def test_all_same(self):
        # all same case
        input_in = 'wwwww'
        self.assertFalse(is_unique(input_in))


class TestIsPermutation(unittest.TestCase):
    def test_correct_case(self):
        # correct case
        input_in = 'abbcda'
        self.assertTrue(is_permutation('bcadba', input_in))
        self.assertTrue(is_permutation(input_in, 'bbaadc'))
        self.assertFalse(is_permutation(input_in, 'BBCAAD'))

    def test_incorrect_case(self):
        # incorrect case
        input_in = 'bytgs'
        self.assertFalse(is_permutation(input_in, 'gsadf'))
        self.assertFalse(is_permutation('g', input_in))

    def test_empty_case(self):
        # empty case
        input_in = ''
        self.assertTrue(is_permutation(input_in, ''))
        self.assertFalse(is_permutation('a', input_in))

    def test_none_case(self):
        # none case
        input_in = None
        self.assertFalse(is_permutation(input_in, None))
        self.assertFalse(is_permutation('ss', input_in))
        self.assertFalse(is_permutation(input_in, '42'))

    def test_all_same(self):
        # all same case
        input_in = 'aAaa'
        self.assertFalse(is_permutation(input_in, 'a'))
        self.assertTrue(is_permutation('aaAa', input_in))
        self.assertFalse(is_permutation(input_in, 'aaaa'))


class TestUrlify(unittest.TestCase):
    def test_correct_case(self):
        # correct case
        self.assertEqual(urlify('Mr John Smith ', 13), 'Mr%20John%20Smith')
        self.assertEqual(urlify('Mr  v gd   ', 8), 'Mr%20%20v%20gd')
        self.assertEqual(urlify(' M w', 4), '%20M%20w')
        self.assertEqual(urlify('adf', 3), 'adf')

    def test_incorrect_case(self):
        # incorrect case
        self.assertNotEqual('frg4', urlify('frg4', 3))

    def test_empty_case(self):
        # empty case
        self.assertEqual(urlify('', 12), '')
        self.assertEqual(urlify('', 0), '')

    def test_none_case(self):
        # none case
        self.assertEqual(urlify(None, 28), None)

    def test_special(self):
        # special cases
        # all non character
        self.assertEqual(urlify('  ', 2), '%20%20')
        # different length
        self.assertEqual(urlify('h  jg s', 4), 'h%20%20j')


class TestPalindromePermutation(unittest.TestCase):
    def test_correct_case(self):
        # correct case
        self.assertTrue(palindrome_permutation('Tact Coa'))
        self.assertTrue(palindrome_permutation(' Rf n j Frj'))

    def test_incorrect_case(self):
        # incorrect case
        self.assertFalse(palindrome_permutation('abc'))
        self.assertFalse(palindrome_permutation('gW x s sG'))

    def test_empty_case(self):
        # empty case
        self.assertTrue(palindrome_permutation(''))

    def test_none_case(self):
        # none case
        self.assertTrue(palindrome_permutation(None))

    def test_special_case(self):
        # one char case
        self.assertTrue(palindrome_permutation('g'))
        # one space case
        self.assertTrue(palindrome_permutation(' '))


class TestOneAway(unittest.TestCase):
    def test_correct_case(self):
        # correct case
        self.assertTrue(one_away('pale', 'ple'))
        self.assertTrue(one_away('pales', 'pale'))
        self.assertTrue(one_away('pale', 'bale'))

    def test_incorrect_case(self):
        # incorrect case
        self.assertFalse(one_away('pale', 'bales'))
        self.assertFalse(one_away('b ', 'as'))

    def test_empty_case(self):
        # empty case
        self.assertTrue(one_away('', 'z'))
        self.assertTrue(one_away('a', ''))
        self.assertFalse(one_away('', 'grg'))
        self.assertTrue(one_away('', ''))

    def test_none_case(self):
        # none case
        self.assertTrue(one_away(None, None))
        self.assertTrue(one_away(None, ' '))
        self.assertTrue(one_away('z', None))
        self.assertTrue(one_away(None, ''))
        self.assertFalse(one_away(None, '  '))

    def test_special_case(self):
        # one space case
        self.assertTrue(one_away(' ', 'a'))


class TestStringCompression(unittest.TestCase):
    def test_correct_case(self):
        # correct case
        self.assertEqual(string_compression('aabcccccaaa'), 'a2b1c5a3')
        self.assertEqual(string_compression('avc'), 'avc')
        self.assertEqual(string_compression('aaaaaabbbaa'), 'a6b3a2')

    def test_base_case(self):
        # test returning original
        self.assertEqual(string_compression('aabCcCcaAAAff'), 'aabCcCcaAAAff')
        self.assertEqual(string_compression('abaaAA'), 'abaaAA')

    def test_empty_case(self):
        # empty case
        self.assertEqual(string_compression(''), '')

    def test_none_case(self):
        # none case
        self.assertEqual(string_compression(None), None)

    def test_special_case(self):
        # All same
        self.assertEqual(string_compression('aaaa'), 'a4')
        # single char
        self.assertEqual(string_compression('A'), 'A')


class TestRotateMatrix(unittest.TestCase):
    def test_even_case(self):
        # even case
        input_in = [[1, 2], [3, 4]]
        answer = [[3, 1], [4, 2]]
        self.assertEqual(rotate_matrix(input_in), answer)

        input_in = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        answer = [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
        self.assertEqual(rotate_matrix(input_in), answer)

    def test_odd_case(self):
        # odd case
        input_in = [[1]]
        answer = [[1]]
        self.assertEqual(rotate_matrix(input_in), answer)

        input_in = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        answer = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        self.assertEqual(rotate_matrix(input_in), answer)

        input_in = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
        answer = [[21, 16, 11, 6, 1], [22, 17, 12, 7, 2], [23, 18, 13, 8, 3], [24, 19, 14, 9, 4], [25, 20, 15, 10, 5]]
        self.assertEqual(rotate_matrix(input_in), answer)

    def test_incorrect_case(self):
        # non square case
        input_in = [[1], [2]]
        answer = None
        self.assertEqual(rotate_matrix(input_in), answer)

    def test_empty_case(self):
        # empty case
        input_in = []
        self.assertEqual(rotate_matrix(input_in), [])

    def test_none_case(self):
        # none case
        self.assertEqual(rotate_matrix(None), None)


class TestZeroMatrix(unittest.TestCase):
    def test_non_first_case(self):
        # test normal cases
        input_in = [[1]]
        answer = [[1]]
        self.assertEqual(zero_matrix(input_in), answer)

        input_in = [[0, 1], [1, 0]]
        answer = [[0, 0], [0, 0]]
        self.assertEqual(zero_matrix(input_in), answer)

        input_in = [[1, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 1]]
        answer = [[1, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 1]]
        self.assertEqual(zero_matrix(input_in), answer)

    def test_first_both(self):
        # test first row or column zero
        input_in = [[0, 1, 1], [1, 1, 1], [1, 1, 1]]
        answer = [[0, 0, 0], [0, 1, 1], [0, 1, 1]]
        self.assertEqual(zero_matrix(input_in), answer)

        input_in = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 1]]
        answer = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]
        self.assertEqual(zero_matrix(input_in), answer)

        input_in = [[0, 0, 0, 0], [0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 1]]
        answer = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.assertEqual(zero_matrix(input_in), answer)

    def test_empty_case(self):
        # empty case
        input_in = []
        self.assertEqual(zero_matrix(input_in), None)

    def test_none_case(self):
        # none case
        self.assertEqual(zero_matrix(None), None)


class TestStringRotation(unittest.TestCase):
    def test_correct_case(self):
        # correct case
        self.assertTrue(string_rotation('waterbottle', 'erbottlewat'))
        self.assertTrue(string_rotation('WiskonterHan', 'HanWiskonter'))

    def test_incorrect_case(self):
        # incorrect case
        self.assertFalse(string_rotation('waterbottle', 'erbottlew'))
        self.assertFalse(string_rotation('waterbottle', 'ERBOTTLEWAT'))

    def test_empty_case(self):
        # empty case
        self.assertTrue(string_rotation('', ''))
        self.assertFalse(string_rotation('a', ''))
        self.assertFalse(string_rotation('', 'x'))

    def test_none_case(self):
        # none case
        self.assertTrue(string_rotation(None, None))
        self.assertFalse(string_rotation(None, 'add'))
        self.assertFalse(string_rotation('', None))

    def test_special_case(self):
        # one character case
        self.assertTrue(string_rotation('a', 'a'))
        self.assertFalse(string_rotation('b', 'a'))

        # repetitive character case
        self.assertTrue(string_rotation('aaaa', 'aaaa'))
        self.assertFalse(string_rotation('aaaa', 'abaa'))


if __name__ == '__main__':
    unittest.main()
