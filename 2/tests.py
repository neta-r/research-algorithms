import sys

import unittest
from q2 import lastcall


@lastcall
def f(x: int):
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

    def test_f(self):
        self.assertEqual(f(3), 27)
        f(3)