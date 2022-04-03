from cities import city_with_name, graph_path, graph, city
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
    ind = random.randint(0, g.num_of_cities())
    v = g.get(ind)
    g.visit_city(v)
    visited = 1
    while visited != g.num_of_cities():
        u = next_unvisited_min(g, v)
        g.visit_city(u)
        visited = visited + 1
        v = u
    return g.out()


if __name__ == '__main__':
    pass
    LA = city_with_name("Los Angeles", {"Brooklyn": 7, "New York": 5, "California": 5, "Chicago": 10})
    BR = city_with_name("Brooklyn", {"Los Angeles": 7, "New York": 2, "California": 11, "Chicago": 5})
    NY = city_with_name("New York", {"Los Angeles": 5, "Brooklyn": 2, "California": 2, "Chicago": 4})
    CALI = city_with_name("California", {"Los Angeles": 5, "Brooklyn": 11, "New York": 2, "Chicago": 3})
    CHG = city_with_name("Chicago", {"Los Angeles": 10, "Brooklyn": 5, "New York": 4, "California": 3})
    gr = graph_path([LA, BR, NY, CALI, CHG])
    print(greedy(gr))
