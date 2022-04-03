from itertools import permutations

from cities import city_with_name, graph_path, graph, city, city_without_name, graph_path_len
from sys import maxsize


def brute_force(g: graph):
    min_path = maxsize
    perms = permutations(g.cities)
    winning_perm = None
    for perm in list(perms):
        curr_dist = 0
        (curr, *rest) = perm
        while len(rest) != 0:
            (nxt, *rest) = rest
            curr_dist += curr.get_dist(nxt)
            curr = nxt
        if curr_dist < min_path:
            min_path = curr_dist
            winning_perm = perm
    # after we discovered the solution let's visit all cities to get the right output
    (curr, *rest) = winning_perm
    g.visit_city(curr)
    while len(rest) != 0:
        (curr, *rest) = rest
        g.visit_city(curr)
    return g.out()


if __name__ == '__main__':
    LA = city_with_name("Los Angeles", {"Brooklyn": 7, "New York": 5, "California": 5})
    BR = city_with_name("Brooklyn", {"Los Angeles": 7, "New York": 2, "California": 11})
    NY = city_with_name("New York", {"Los Angeles": 5, "Brooklyn": 2, "California": 2})
    CALI = city_with_name("California", {"Los Angeles": 5, "Brooklyn": 11, "New York": 2})
    gr = graph_path([LA, BR, NY, CALI])
    # should print Los Angeles->California->New York->Brooklyn
    print(brute_force(gr))

    c0 = city_without_name([7, 5, 5])
    c1 = city_without_name([7, 2, 11])
    c2 = city_without_name([5, 2, 2])
    c3 = city_without_name([5, 11, 2])
    gr = graph_path([c0, c1, c2, c3])
    # should print 0->3->2->1
    print(brute_force(gr))