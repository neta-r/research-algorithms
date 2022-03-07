import unittest
from q3 import List


class test_doc_to_html(unittest.TestCase):
    def test_one_dimensional_list(self):
        l = List(['hi', 'my', 'name', 'is', 'neta'])
        # making sure function __getitem__ returning the right value
        self.assertEqual('name', l[2])
        # making sure function __getitem__ returning the right value before change
        self.assertEqual('neta', l[4])
        # making sure function __setitem__ working
        l[4] = 'amit'
        # making sure function __getitem__ returning the right value after change
        self.assertEqual('amit', l[4])
        # making sure function __getitem__ is raising IndexError
        try:
            l[5]
        except Exception:
            assert True

    def test_two_dimensional_list(self):
        l = List([[1.2, 2.2, 3.2], [1.0, 6.5, 8.9]])
        # making sure function __getitem__ returning the right value
        self.assertEqual(1.0, l[1, 0])
        # # making sure function __getitem__ returning the right value before change
        self.assertEqual(2.2, l[0, 1])
        # # making sure function __setitem__ working
        l[0, 1] = 5.2
        # # making sure function __getitem__ returning the right value after change
        self.assertEqual(5.2, l[0, 1])
        # # making sure function __getitem__ is raising IndexError
        try:
            l[5]
        except Exception:
            assert True

    def test_three_dimensional_list(self):
        l = List([[[1, "meow", 5.6], []], [[1, 5], [6]], [['hi', 8]]])
        # making sure function __getitem__ returning the right value
        self.assertEqual([[1, "meow", 5.6], []], l[0])
        # making sure function __getitem__ returning the right value before change
        self.assertEqual(6, l[1, 1, 0])
        # making sure function __setitem__ working
        l[0, 0, 2] = 'holla'
        # making sure function __getitem__ returning the right value after change
        self.assertEqual('holla', l[0, 0, 2])
        # making sure function __getitem__ is raising IndexError
        try:
            l[0, 1, 2]
        except Exception:
            assert True
