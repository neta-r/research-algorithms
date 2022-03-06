import unittest
from q2 import lastcall

import io
from contextlib import redirect_stdout


@lastcall
def f1(x: int):
    return x ** 3


@lastcall
def without_last_char(s: str):
    return s[:-1]


@lastcall
def sort_list(lst: list):
    return sorted(lst)


@lastcall
def round_float(x: float):
    return round(x)


class lastcall_test(unittest.TestCase):
    # argument's type is int
    def test_f(self):
        # new function, new value
        self.assertEqual(f1(3), 27)
        f = io.StringIO()
        # old function, old value
        with redirect_stdout(f):
            f1(3)
            # out now contains output printed in lastcall function
            out = f.getvalue()
            self.assertEqual(out, "I already told you that the answer is: 27\n")
        # old function, new value
        self.assertEqual(f1(2), 8)

    # argument's type is str
    def test_without_last_char(self):
        # new function, new value
        self.assertEqual(without_last_char('this is a test!!!'), 'this is a test!!')
        f = io.StringIO()
        # old function, old value
        with redirect_stdout(f):
            without_last_char('this is a test!!!')
            # out now contains output printed in lastcall function
            out = f.getvalue()
            self.assertEqual(out, "I already told you that the answer is: this is a test!!\n")
        # old function, new value
        self.assertEqual(without_last_char('another test :)!'), 'another test :)')

    # argument's type is list
    def test_without_last_char(self):
        # new function, new value
        self.assertEqual(sort_list([5, 4, 7]), [4, 5, 7])
        f = io.StringIO()
        # old function, old value
        with redirect_stdout(f):
            sort_list([5, 4, 7])
            # out now contains output printed in lastcall function
            out = f.getvalue()
            self.assertEqual(out, "I already told you that the answer is: [4, 5, 7]\n")
        # old function, new value (same result, different argument
        self.assertEqual(sort_list([7, 4, 5]), [4, 5, 7])

    # argument's type is float
    def test_without_last_char(self):
        # new function, new value
        self.assertEqual(round_float(2.3), 2)
        f = io.StringIO()
        # old function, old value
        with redirect_stdout(f):
            round_float(2.3)
            # out now contains output printed in lastcall function
            out = f.getvalue()
            self.assertEqual(out, "I already told you that the answer is: 2\n")
        # old function, new value (same result, different argument
        self.assertEqual(round_float(2.2), 2)