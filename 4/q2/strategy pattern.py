from typing import Callable, Any
from Greedy_algo import greedy, next_unvisited_min
from Brute_force_algo import brute_force
from cities import *


def partition(algorithm: Callable, dists: list, cities_names=None, out_type: str = "length",
              city_type: str = "city_without_name"):
    cities_list = []
    if city_type == "city_with_name" and cities_names is not None:
        for i in range(len(dists)):
            c = city_with_name(cities_names[i], dists[i])
            cities_list.append(c)
    else:
        city_without_name.key = 0
        for i in range(len(dists)):
            c = city_without_name(dists[i])
            cities_list.append(c)

    if out_type == "path":
        g = graph_path(cities_list)
    else:
        g = graph_path_len(cities_list)
    return algorithm(g)


if __name__ == '__main__':

    # names + greedy + path
    # should print : Los Angeles->New York->Brooklyn->Chicago->California
    print(partition(greedy, [{"Brooklyn": 7, "New York": 5, "California": 5, "Chicago": 10},
                             {"Los Angeles": 7, "New York": 2, "California": 11, "Chicago": 5},
                             {"Los Angeles": 5, "Brooklyn": 2, "California": 2, "Chicago": 4},
                             {"Los Angeles": 5, "Brooklyn": 11, "New York": 2, "Chicago": 3},
                             {"Los Angeles": 10, "Brooklyn": 5, "New York": 4, "California": 3}],
                    ["Los Angeles", "Brooklyn", "New York", "California", "Chicago"], "path", "city_with_name"))

    # names + greedy + length
    # should print : 15
    print(partition(greedy, [{"Brooklyn": 7, "New York": 5, "California": 5, "Chicago": 10},
                       {"Los Angeles": 7, "New York": 2, "California": 11, "Chicago": 5},
                       {"Los Angeles": 5, "Brooklyn": 2, "California": 2, "Chicago": 4},
                       {"Los Angeles": 5, "Brooklyn": 11, "New York": 2, "Chicago": 3},
                       {"Los Angeles": 10, "Brooklyn": 5, "New York": 4, "California": 3}],
              ["Los Angeles", "Brooklyn", "New York", "California", "Chicago"], "length", "city_with_name"))

    # names + brute_force + path
    # should print : Los Angeles->Brooklyn->New York->California->Chicago
    print(partition(brute_force, [{"Brooklyn": 7, "New York": 5, "California": 5, "Chicago": 10},
                                  {"Los Angeles": 7, "New York": 2, "California": 11, "Chicago": 5},
                                  {"Los Angeles": 5, "Brooklyn": 2, "California": 2, "Chicago": 4},
                                  {"Los Angeles": 5, "Brooklyn": 11, "New York": 2, "Chicago": 3},
                                  {"Los Angeles": 10, "Brooklyn": 5, "New York": 4, "California": 3}],
                    ["Los Angeles", "Brooklyn", "New York", "California", "Chicago"], "path", "city_with_name"))

    # names + brute_force + length
    # should print 14
    print(partition(brute_force, [{"Brooklyn": 7, "New York": 5, "California": 5, "Chicago": 10},
                                  {"Los Angeles": 7, "New York": 2, "California": 11, "Chicago": 5},
                                  {"Los Angeles": 5, "Brooklyn": 2, "California": 2, "Chicago": 4},
                                  {"Los Angeles": 5, "Brooklyn": 11, "New York": 2, "Chicago": 3},
                                  {"Los Angeles": 10, "Brooklyn": 5, "New York": 4, "California": 3}],
                    ["Los Angeles", "Brooklyn", "New York", "California", "Chicago"], "length", "city_with_name"))

    # no names + greedy + path
    # should print: 0->2->1->4->3
    print(partition(greedy, [[7, 5, 5, 10], [7, 2, 11, 5], [5, 2, 2, 4], [5, 11, 2, 3], [10, 5, 4, 3]]
                    , out_type="path", city_type="city_without_name"))

    # no names + greedy + length
    # should print: 15
    print(partition(greedy, [[7, 5, 5, 10], [7, 2, 11, 5], [5, 2, 2, 4], [5, 11, 2, 3], [10, 5, 4, 3]]
                    , out_type="length", city_type="city_without_name"))

    # no names + brute_force + path
    # should print: 0->1->2->3->4
    print(partition(brute_force, [[7, 5, 5, 10], [7, 2, 11, 5], [5, 2, 2, 4], [5, 11, 2, 3], [10, 5, 4, 3]]
                    , out_type="path", city_type="city_without_name"))

    # no names + brute_force + length
    # should print: 14
    print(partition(brute_force, [[7, 5, 5, 10], [7, 2, 11, 5], [5, 2, 2, 4], [5, 11, 2, 3], [10, 5, 4, 3]]
                    , out_type="length", city_type="city_without_name"))