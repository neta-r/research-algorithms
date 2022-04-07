import unittest
from q1 import bounded_subset


class bounded_subset_test(unittest.TestCase):
    def test1(self):
        self.assertEqual(list(bounded_subset([1, 2, 3], 4)), [[3], [2], [1], [1, 3], [1, 2]])

    def test2(self):
        self.assertEqual(list(bounded_subset([32, 1, 99, 2, 5, 4, 7], 12)),
                         [[7], [4], [4, 7], [5], [5, 7], [5, 4], [2], [2, 7],
                          [2, 4], [2, 5], [2, 5, 4], [1], [1, 7], [1, 4], [1, 4, 7],
                          [1, 5], [1, 5, 4], [1, 2], [1, 2, 7], [1, 2, 4], [1, 2, 5], [1, 2, 5, 4]])

    def test3(self):
        self.assertEqual(list(bounded_subset([32, 5, 8, 7, 2], 1)), [])

    def test4(self):
        self.assertEqual(list(bounded_subset([], 2)), [])

    def test5(self):
        self.assertEqual(list(bounded_subset([1, 2, 3], -1)), [])

    def test6(self):
        self.assertEqual(list(bounded_subset([1, -2, 3], 1)), [[-2], [-2, 3], [1], [1, -2]])
