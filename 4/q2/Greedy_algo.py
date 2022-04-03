from cities import city_with_name, graph_path, graph, city, city_without_name, graph_path_len
import random


def next_unvisited_min(g: graph, v: city):
    min_dist = 99999
    nei = v
    for u in g.cities:
        if not u.is_visited:
            if v.get_dist(u) < min_dist:
                min_dist = v.get_dist(u)
                nei = u
    return nei


def greedy(g: graph):
    v = g.get(0)
    g.visit_city(v)
    visited = 1
    while visited != g.num_of_cities():
        u = next_unvisited_min(g, v)
        g.visit_city(u)
        visited = visited + 1
        v = u
    return g.out()


if __name__ == '__main__':
    LA = city_with_name("Los Angeles", {"Brooklyn": 7, "New York": 5, "California": 5, "Chicago": 10})
    BR = city_with_name("Brooklyn", {"Los Angeles": 7, "New York": 2, "California": 11, "Chicago": 5})
    NY = city_with_name("New York", {"Los Angeles": 5, "Brooklyn": 2, "California": 2, "Chicago": 4})
    CALI = city_with_name("California", {"Los Angeles": 5, "Brooklyn": 11, "New York": 2, "Chicago": 3})
    CHG = city_with_name("Chicago", {"Los Angeles": 10, "Brooklyn": 5, "New York": 4, "California": 3})
    gr = graph_path([LA, BR, NY, CALI, CHG])
    # should print : Los Angeles->New York->Brooklyn->Chicago->California
    print(greedy(gr))

    LA.is_visited = BR.is_visited = NY.is_visited = CALI.is_visited = CHG.is_visited = False
    gr = graph_path_len([LA, BR, NY, CALI, CHG])
    # should print : 15
    print(greedy(gr))

    c0 = city_without_name([7, 5, 5, 10])
    c1 = city_without_name([7, 2, 11, 5])
    c2 = city_without_name([5, 2, 2, 4])
    c3 = city_without_name([5, 11, 2, 3])
    c4 = city_without_name([10, 5, 4, 3])
    gr = graph_path([c0, c1, c2, c3, c4])
    # should print : 0->2->1->4->3
    print(greedy(gr))
    gr = graph_path_len([c0, c1, c2, c3, c4])

    c0.is_visited = c1.is_visited = c2.is_visited = c3.is_visited = c4.is_visited = False
    # should print : 15
    print(greedy(gr))
