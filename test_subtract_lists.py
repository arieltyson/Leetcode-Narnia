import unittest
from subtract_lists import subtract_lists

class TestSubtractLists(unittest.TestCase):
    
    def test_example_1(self):
        A = [1, 0, 2]
        B = [2, 2, 5]
        result = subtract_lists(A, B)
        expected = [-1, 2, 3]
        self.assertEqual(result, expected)

    def test_example_2(self):
        A = [9, 0, 0, 0]
        B = [1]
        result = subtract_lists(A, B)
        expected = [8, 9, 9, 9]
        self.assertEqual(result, expected)

    def test_example_3(self):
        A = [5]
        B = [7]
        result = subtract_lists(A, B)
        expected = [-2]
        self.assertEqual(result, expected)

    def test_same_numbers(self):
        A = [4, 5, 6]
        B = [4, 5, 6]
        result = subtract_lists(A, B)
        expected = [0]
        self.assertEqual(result, expected)

    def test_simple_borrow(self):
        A = [1, 0]
        B = [2]
        result = subtract_lists(A, B)
        expected = [8]
        self.assertEqual(result, expected)

    def test_borrow_across_zeros(self):
        A = [1, 0, 0, 0]
        B = [1]
        result = subtract_lists(A, B)
        expected = [9, 9, 9]
        self.assertEqual(result, expected)

    def test_large_difference(self):
        A = [9, 9, 9, 9]
        B = [1]
        result = subtract_lists(A, B)
        expected = [9, 9, 9, 8]
        self.assertEqual(result, expected)

    def test_different_lengths(self):
        A = [2, 5, 0]
        B = [2, 4, 9]
        result = subtract_lists(A, B)
        expected = [1]
        self.assertEqual(result, expected)

    def test_zero_minimum(self):
        A = [0, 0, 0]
        B = [0]
        result = subtract_lists(A, B)
        expected = [0]
        self.assertEqual(result, expected)

    def test_negative_large_b(self):
        A = [5, 0, 0, 1]
        B = [7, 1, 2, 3]
        result = subtract_lists(A, B)
        expected = [-2, 2, 1, 2]
        self.assertEqual(result, expected)

    def test_edge_case_single_digit(self):
        A = [1]
        B = [1]
        result = subtract_lists(A, B)
        expected = [0]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
