import unittest
from q1 import bounded_subset

import io
from contextlib import redirect_stdout


class bounded_subset_test(unittest.TestCase):
    def test1(self):
        # redirect stdout to this file
        f = io.StringIO()
        with redirect_stdout(f):
            for s in bounded_subset([1, 2, 3], 4):
                print(s)
            out = f.getvalue()
            # comparing stdout to expected result
            self.assertEqual(out, "[3]\n[2]\n[1]\n[1, 3]\n[1, 2]\n")

    def test2(self):
        # redirect stdout to this file
        f = io.StringIO()
        with redirect_stdout(f):
            for s in bounded_subset([32, 1, 99, 2, 5, 4, 7], 12):
                print(s)
            out = f.getvalue()
            # comparing stdout to expected result
            self.assertEqual(out, "[7]\n[4]\n[4, 7]\n[5]\n[5, 7]\n[5, 4]\n[2]\n[2, 7]\n[2, 4]\n[2, "
                                  "5]\n[2, 5, 4]\n[1]\n[1, 7]\n[1, 4]\n[1, 4, 7]\n[1, 5]\n[1, 5, 4]\n[1, 2]\n[1, 2, "
                                  "7]\n[1, 2, 4]\n[1, 2, 5]\n[1, 2, 5, 4]\n")

    def test3(self):
        # redirect stdout to this file
        f = io.StringIO()
        with redirect_stdout(f):
            for s in bounded_subset([32, 5, 8, 7, 22], 2):
                print(s)
            out = f.getvalue()
            # comparing stdout to expected result
            self.assertEqual(out, "")  # none of the numbers match
