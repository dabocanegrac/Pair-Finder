import sys
import unittest
sys.path.insert(0, '../')  # Add the parent directory to the path
from find_pairs import find_pairs

class TestFindPairs(unittest.TestCase):

    # Test an empty list. Expect empty list.
    def test_empty_list(self):
        self.assertEqual(find_pairs([], 5), [])

    # Test a list with one item. Expect empty list.
    def test_single_item_list(self):
        self.assertEqual(find_pairs([1], 5), [])

    # Test a list with no pairs that sum to target. Expect empty list.
    def test_no_pairs(self):
        self.assertEqual(find_pairs([1, 2, 3, 4], 10), [])

    # Test target value outside of range of numbers. Expect empty list.
    def test_target_outside_range(self):
        self.assertEqual(find_pairs([-1, -2, -3, -4], 125), [])

    # Test a list with one pair that sum to target. Expect one pair.
    def test_one_pair(self):
        expected_output = {frozenset((1, 4))}  # use frozen set to ignore order
        # use list comprehension to convert to frozen set and ignore order
        actual_output = {frozenset(pair)
                         for pair in find_pairs([1, 3, 4], 5)}
        self.assertEqual(actual_output, expected_output)

    # Test a list with two pairs that sum to target. Expect two pairs.
    def test_two_pairs(self):
        expected_output = {frozenset((1, 4)), frozenset(
            (2, 3))}  # use frozen set to ignore order
        # use list comprehension to convert to frozen set and ignore order
        actual_output = {frozenset(pair)
                         for pair in find_pairs([1, 2, 3, 4], 5)}
        self.assertEqual(actual_output, expected_output)

    # Test a list with multiple pairs that sum to target. Expect multiple pairs.
    def test_multiple_pairs(self):
        expected_output = {frozenset((1, 6)), frozenset(
            (2, 5)), frozenset((3, 4))}  # use frozen set to ignore order
        # use list comprehension to convert to frozen set and ignore order
        actual_output = {frozenset(pair)
                         for pair in find_pairs([1, 2, 3, 4, 5, 6], 7)}
        self.assertEqual(actual_output, expected_output)

    # Test a list with negative numbers. Expect one or more pairs.
    def test_negative_numbers(self):
        expected_output = {
            frozenset((-3, 3)), frozenset((-2, 2)), frozenset((-1, 1))}
        actual_output = {frozenset(pair) for pair in find_pairs(
            [-3, -2, -1, 0, 1, 2, 3], 0)}
        self.assertEqual(actual_output, expected_output)

    # Test a large input list with an even number of elements. Expect multiple pairs.
    def test_large_input_even(self):
        n = 10000
        lst = list(range(n))
        target_sum = n - 1
        expected_output = {frozenset((i, target_sum - i))
                           for i in range(target_sum//2+1)}
        actual_output = {frozenset(pair)
                         for pair in find_pairs(lst, target_sum)}
        self.assertEqual(actual_output, expected_output)

    # Test a large input list with an odd number of elements. Expect multiple pairs.
    def test_large_input_odd(self):
        n = 10001
        lst = list(range(n))
        target_sum = n - 1
        expected_output = {frozenset((i, target_sum - i))
                           for i in range(target_sum//2)}
        actual_output = {frozenset(pair)
                         for pair in find_pairs(lst, target_sum)}
        self.assertEqual(actual_output, expected_output)

    # Test a list with no pairs that sum to target. Expect empty list.
    def test_no_pairs_large_input(self):
        n = 1000
        lst = list(range(n))
        target_sum = 2*n
        self.assertEqual(find_pairs(lst, target_sum), [])


if __name__ == '__main__':
    # Run the test suite.
    unittest.main()
