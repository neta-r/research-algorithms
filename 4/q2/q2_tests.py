import unittest
from strategy_pattern import *

import io
from contextlib import redirect_stdout


class strategy_pattern_test(unittest.TestCase):

    # names+greedy+path test
    def test1(self):
        # redirect stdout to this file
        f = io.StringIO()
        with redirect_stdout(f):
            print(partition(greedy, [{"London": 5, "Jerusalem": 14, "Paris": 2, "Berlin": 12},
                                     {"Madrid": 5, "Jerusalem": 6, "Paris": 9, "Berlin": 15},
                                     {"Madrid": 14, "London": 6, "Paris": 21, "Berlin": 10},
                                     {"Madrid": 2, "London": 9, "Jerusalem": 21, "Berlin": 3},
                                     {"Madrid": 12, "London": 15, "Jerusalem": 10, "Paris": 3}],
                            ["Madrid", "London", "Jerusalem", "Paris", "Berlin"], "path", "city_with_name"))
            print(partition(greedy, [{"Ariel": 99, "Eilat": 26, "Ashdod": 14, "Afula": 25, "Yahud": 13, "Nataniya": 80},
                                     {"Haifa": 99, "Eilat": 52, "Ashdod": 63, "Afula": 17, "Yahud": 19, "Nataniya": 23},
                                     {"Haifa": 26, "Ariel": 52, "Ashdod": 14, "Afula": 56, "Yahud": 53, "Nataniya": 54},
                                     {"Haifa": 14, "Ariel": 63, "Eilat": 14, "Afula": 23, "Yahud": 44, "Nataniya": 26},
                                     {"Haifa": 25, "Ariel": 17, "Eilat": 56, "Ashdod": 23, "Yahud": 24, "Nataniya": 47},
                                     {"Haifa": 13, "Ariel": 19, "Eilat": 53, "Ashdod": 44, "Afula": 24, "Nataniya": 2},
                                     {"Haifa": 80, "Ariel": 23, "Eilat": 54, "Ashdod": 26, "Afula": 47, "Yahud": 2}],
                            ["Haifa", "Ariel", "Eilat", "Ashdod", "Afula", "Yahud", "Nataniya"], "path",
                            "city_with_name"))
            out = f.getvalue()
            # comparing stdout to expected result
            self.assertEqual(out, "Madrid->Paris->Berlin->Jerusalem->London\n"
                                  "Haifa->Yahud->Nataniya->Ariel->Afula->Ashdod->Eilat\n")

    # names+greedy+length test
    def test2(self):
        # redirect stdout to this file
        f = io.StringIO()
        with redirect_stdout(f):
            print(partition(greedy, [{"London": 5, "Jerusalem": 14, "Paris": 2, "Berlin": 12},
                                     {"Madrid": 5, "Jerusalem": 6, "Paris": 9, "Berlin": 15},
                                     {"Madrid": 14, "London": 6, "Paris": 21, "Berlin": 10},
                                     {"Madrid": 2, "London": 9, "Jerusalem": 21, "Berlin": 3},
                                     {"Madrid": 12, "London": 15, "Jerusalem": 10, "Paris": 3}],
                            ["Madrid", "London", "Jerusalem", "Paris", "Berlin"], "length", "city_with_name"))
            print(partition(greedy, [{"Ariel": 99, "Eilat": 26, "Ashdod": 14, "Afula": 25, "Yahud": 13, "Nataniya": 80},
                                     {"Haifa": 99, "Eilat": 52, "Ashdod": 63, "Afula": 17, "Yahud": 19, "Nataniya": 23},
                                     {"Haifa": 26, "Ariel": 52, "Ashdod": 14, "Afula": 56, "Yahud": 53, "Nataniya": 54},
                                     {"Haifa": 14, "Ariel": 63, "Eilat": 14, "Afula": 23, "Yahud": 44, "Nataniya": 26},
                                     {"Haifa": 25, "Ariel": 17, "Eilat": 56, "Ashdod": 23, "Yahud": 24, "Nataniya": 47},
                                     {"Haifa": 13, "Ariel": 19, "Eilat": 53, "Ashdod": 44, "Afula": 24, "Nataniya": 2},
                                     {"Haifa": 80, "Ariel": 23, "Eilat": 54, "Ashdod": 26, "Afula": 47, "Yahud": 2}],
                            ["Haifa", "Ariel", "Eilat", "Ashdod", "Afula", "Yahud", "Nataniya"], "length",
                            "city_with_name"))
            out = f.getvalue()
            # comparing stdout to expected result
            self.assertEqual(out, "21\n92\n")

    # names+brute force+path test
    def test3(self):
        # redirect stdout to this file
        f = io.StringIO()
        with redirect_stdout(f):
            print(partition(brute_force, [{"London": 5, "Jerusalem": 14, "Paris": 2, "Berlin": 12},
                                          {"Madrid": 5, "Jerusalem": 6, "Paris": 9, "Berlin": 15},
                                          {"Madrid": 14, "London": 6, "Paris": 21, "Berlin": 10},
                                          {"Madrid": 2, "London": 9, "Jerusalem": 21, "Berlin": 3},
                                          {"Madrid": 12, "London": 15, "Jerusalem": 10, "Paris": 3}],
                            ["Madrid", "London", "Jerusalem", "Paris", "Berlin"], "path", "city_with_name"))
            print(partition(brute_force,
                            [{"Ariel": 99, "Eilat": 26, "Ashdod": 14, "Afula": 25, "Yahud": 13, "Nataniya": 80},
                             {"Haifa": 99, "Eilat": 52, "Ashdod": 63, "Afula": 17, "Yahud": 19, "Nataniya": 23},
                             {"Haifa": 26, "Ariel": 52, "Ashdod": 14, "Afula": 56, "Yahud": 53, "Nataniya": 54},
                             {"Haifa": 14, "Ariel": 63, "Eilat": 14, "Afula": 23, "Yahud": 44, "Nataniya": 26},
                             {"Haifa": 25, "Ariel": 17, "Eilat": 56, "Ashdod": 23, "Yahud": 24, "Nataniya": 47},
                             {"Haifa": 13, "Ariel": 19, "Eilat": 53, "Ashdod": 44, "Afula": 24, "Nataniya": 2},
                             {"Haifa": 80, "Ariel": 23, "Eilat": 54, "Ashdod": 26, "Afula": 47, "Yahud": 2}],
                            ["Haifa", "Ariel", "Eilat", "Ashdod", "Afula", "Yahud", "Nataniya"], "path",
                            "city_with_name"))
            out = f.getvalue()
            # comparing stdout to expected result
            self.assertEqual(out, "Jerusalem->London->Madrid->Paris->Berlin\n"
                                  "Eilat->Ashdod->Haifa->Yahud->Nataniya->Ariel->Afula\n")

    # names+brute force+length test
    def test4(self):
        # redirect stdout to this file
        f = io.StringIO()
        with redirect_stdout(f):
            print(partition(brute_force, [{"London": 5, "Jerusalem": 14, "Paris": 2, "Berlin": 12},
                                          {"Madrid": 5, "Jerusalem": 6, "Paris": 9, "Berlin": 15},
                                          {"Madrid": 14, "London": 6, "Paris": 21, "Berlin": 10},
                                          {"Madrid": 2, "London": 9, "Jerusalem": 21, "Berlin": 3},
                                          {"Madrid": 12, "London": 15, "Jerusalem": 10, "Paris": 3}],
                            ["Madrid", "London", "Jerusalem", "Paris", "Berlin"], "length", "city_with_name"))
            print(partition(brute_force,
                            [{"Ariel": 99, "Eilat": 26, "Ashdod": 14, "Afula": 25, "Yahud": 13, "Nataniya": 80},
                             {"Haifa": 99, "Eilat": 52, "Ashdod": 63, "Afula": 17, "Yahud": 19, "Nataniya": 23},
                             {"Haifa": 26, "Ariel": 52, "Ashdod": 14, "Afula": 56, "Yahud": 53, "Nataniya": 54},
                             {"Haifa": 14, "Ariel": 63, "Eilat": 14, "Afula": 23, "Yahud": 44, "Nataniya": 26},
                             {"Haifa": 25, "Ariel": 17, "Eilat": 56, "Ashdod": 23, "Yahud": 24, "Nataniya": 47},
                             {"Haifa": 13, "Ariel": 19, "Eilat": 53, "Ashdod": 44, "Afula": 24, "Nataniya": 2},
                             {"Haifa": 80, "Ariel": 23, "Eilat": 54, "Ashdod": 26, "Afula": 47, "Yahud": 2}],
                            ["Haifa", "Ariel", "Eilat", "Ashdod", "Afula", "Yahud", "Nataniya"], "length",
                            "city_with_name"))
            out = f.getvalue()
            # comparing stdout to expected result
            self.assertEqual(out, "16\n83\n")

    # no names+greedy+path test
    def test5(self):
        # redirect stdout to this file
        f = io.StringIO()
        with redirect_stdout(f):
            print(partition(greedy, [[5, 14, 2, 12], [5, 6, 9, 15], [14, 6, 21, 10], [2, 9, 21, 3], [12, 15, 10, 3]],
                            out_type="path", city_type="city_with_name"))
            print(partition(greedy, [[99, 26, 14, 25, 13, 80], [99, 52, 63, 17, 19, 23], [26, 52, 14, 56, 53, 54],
                                     [14, 63, 14, 23, 44, 26], [25, 17, 56, 23, 24, 47], [13, 19, 53, 44, 24, 2],
                                     [80, 23, 54, 26, 47, 2]], out_type="path", city_type="city_with_name"))
            out = f.getvalue()
            # comparing stdout to expected result
            self.assertEqual(out, "0->3->4->2->1\n"
                                  "0->5->6->1->4->3->2\n")

    # no names+greedy+length test
    def test6(self):
        # redirect stdout to this file
        f = io.StringIO()
        with redirect_stdout(f):
            print(partition(greedy, [[5, 14, 2, 12], [5, 6, 9, 15], [14, 6, 21, 10], [2, 9, 21, 3], [12, 15, 10, 3]],
                            out_type="length", city_type="city_with_name"))
            print(partition(greedy, [[99, 26, 14, 25, 13, 80], [99, 52, 63, 17, 19, 23], [26, 52, 14, 56, 53, 54],
                                     [14, 63, 14, 23, 44, 26], [25, 17, 56, 23, 24, 47], [13, 19, 53, 44, 24, 2],
                                     [80, 23, 54, 26, 47, 2]], out_type="length", city_type="city_with_name"))
            out = f.getvalue()
            # comparing stdout to expected result
            self.assertEqual(out, "21\n92\n")

    # no names+brute force+path test
    def test7(self):
        # redirect stdout to this file
        f = io.StringIO()
        with redirect_stdout(f):
            print(partition(brute_force, [[5, 14, 2, 12], [5, 6, 9, 15], [14, 6, 21, 10], [2, 9, 21, 3], [12, 15, 10, 3]],
                            out_type="path", city_type="city_with_name"))
            print(partition(brute_force, [[99, 26, 14, 25, 13, 80], [99, 52, 63, 17, 19, 23], [26, 52, 14, 56, 53, 54],
                                     [14, 63, 14, 23, 44, 26], [25, 17, 56, 23, 24, 47], [13, 19, 53, 44, 24, 2],
                                     [80, 23, 54, 26, 47, 2]], out_type="path", city_type="city_with_name"))
            out = f.getvalue()
            # comparing stdout to expected result
            self.assertEqual(out, "2->1->0->3->4\n"
                                  "2->3->0->5->6->1->4\n")

    # no names+brute force+length test
    def test8(self):
        # redirect stdout to this file
        f = io.StringIO()
        with redirect_stdout(f):
            print(partition(brute_force, [[5, 14, 2, 12], [5, 6, 9, 15], [14, 6, 21, 10], [2, 9, 21, 3], [12, 15, 10, 3]],
                            out_type="length", city_type="city_with_name"))
            print(partition(brute_force, [[99, 26, 14, 25, 13, 80], [99, 52, 63, 17, 19, 23], [26, 52, 14, 56, 53, 54],
                                     [14, 63, 14, 23, 44, 26], [25, 17, 56, 23, 24, 47], [13, 19, 53, 44, 24, 2],
                                     [80, 23, 54, 26, 47, 2]], out_type="length", city_type="city_with_name"))
            out = f.getvalue()
            # comparing stdout to expected result
            self.assertEqual(out, "16\n83\n")