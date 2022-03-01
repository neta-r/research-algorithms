import q1
import q2
import q3
import unittest
from sympy import *


def f1(name: str, age: int):
    return "my name is " + name + " and my age is " + str(age)


def f2(x: int, y: float, z):
    return x + y + z


class safe_call_test(unittest.TestCase):
    def test_f1(self):
        self.assertEqual("my name is Neta and my age is 23", q1.safe_call(f1, "Neta", 23))
        self.assertEqual("my name is Amit and my age is 25", q1.safe_call(f1, 'Amit', 25))
        # checking for correct return value
        self.assertNotEqual("my name is Amit and my age is 23", q1.safe_call(f1, 'Amit', 25))
        self.assertNotEqual("my name is Amit and my age is 25", q1.safe_call(f1, 'Neta', 23))
        # Incorrect types
        with self.assertRaises(TypeError):
            q1.safe_call(f1, 'Amit', 25.0)
        with self.assertRaises(TypeError):
            q1.safe_call(f1, 25, 'Amit')
        with self.assertRaises(TypeError):
            q1.safe_call(f1, 'Amit', 'Hey')
        with self.assertRaises(TypeError):
            q1.safe_call(f1, 25, 18)
        with self.assertRaises(TypeError):
            q1.safe_call(f1, 25, 18.0)
        # Too few arguments (will throw IndexError - args[counter] doesn't exists)
        with self.assertRaises(Exception):
            q1.safe_call(f1, 'Amit')
        with self.assertRaises(Exception):
            q1.safe_call(f1, 25)

    def test_f2(self):
        self.assertEqual(5.7, q1.safe_call(f2, 1, 4.0, 0.7))
        self.assertEqual(10.0, q1.safe_call(f2, 5, 1.0, 4))
        # checking for correct return value
        self.assertNotEqual(4.7, q1.safe_call(f2, 1, 5.0, 0.7))
        self.assertNotEqual(23, q1.safe_call(f2, 1, 5.0, 8))
        # Incorrect types
        with self.assertRaises(TypeError):
            q1.safe_call(f2, 1.0, 0, 0)
        with self.assertRaises(TypeError):
            q1.safe_call(f2, 1, 0, 0)
        with self.assertRaises(TypeError):
            q1.safe_call(f2, 1.0, 0.0, 0)
        with self.assertRaises(TypeError):
            q1.safe_call(f2, 25, 1.0, "0")
        # Too few arguments (will throw IndexError - args[counter] doesn't exists)
        with self.assertRaises(Exception):
            q1.safe_call(f2, 25)


class safe_print_sorted(unittest.TestCase):
    def test(self):
        self.assertEqual({'a': 5, 'b': {5: '0', 7: 'a'}, 'c': 6, 'd': (1, 2, 3, 4)},
                         q2.print_sorted({"a": 5, "c": 6, "d": (1, 3, 2, 4), "b": {7: "a", 5: "0"}}))
        self.assertEqual({1: 'a', 2: (1, 4, 5, 7), 8: 6, 13: {'1': '0', '2': 'a'}},
                         q2.print_sorted({1: "a", 8: 6, 2: (5, 7, 4, 1), 13: {"2": "a", "1": "0"}}))
        self.assertEqual({1: {4: 2, 5: 0}, 2: (1, 4, 5, 7), 8: {0: [-9, 0, 5], 1: (1, 3, 7)}, 13: {'1': '0', '2': 'a'}},
                         q2.print_sorted({1: {5: 0, 4: 2}, 8: {1: (1, 7, 3), 0: [5, 0, -9]}, 2: (5, 7, 4, 1),
                                          13: {"2": "a", "1": "0"}}))
        self.assertEqual((1, 3, [2, 3, 4]),
                         q2.print_sorted((3, [4, 3, 2], 1)))


class safe_find_root(unittest.TestCase):
    def test(self):
        # round function rounds the solution so it will be possible to be compared to
        x = symbols('x')
        f = x ** 2 - 4
        self.assertAlmostEqual(2.0, round(q3.find_root(f, 1, 3)))

        f = x ** 3 - 27
        self.assertAlmostEqual(3.0, round(q3.find_root(f, 2, 5)))

        f = x ** 5
        self.assertAlmostEqual(0, round(q3.find_root(f, -2, 5)))

        # this function has 2 int solution 2 , -2
        # I changed the range so the function will catch each solution
        f = x ** 8 - 256
        self.assertAlmostEqual(-2, round(q3.find_root(f, -10, 0)))
        self.assertAlmostEqual(2, round(q3.find_root(f, 0, 5)))

        x = symbols('x', real=True)
        f = ln(x)
        self.assertAlmostEqual(1, round(q3.find_root(f, -10, 10)))
