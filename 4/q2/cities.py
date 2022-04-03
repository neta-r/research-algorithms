from abc import ABC, abstractmethod


class city(ABC):
    def __init__(self):
        self.is_visited = False

    @abstractmethod
    def get_dist(self, other_city):
        pass

    @abstractmethod
    def get_key(self):
        pass

    def visit(self):
        self.is_visited = True


class city_with_name(city, ABC):
    def __init__(self, name: str, other_cities: dict):
        super().__init__()
        self.name = name
        self.other_cities = other_cities

    def get_dist(self, other_city: city):
        if other_city.get_key() == self.name:
            return 999999  # infinity
        return self.other_cities[other_city.get_key()]

    def get_key(self):
        return self.name


class city_without_name(city, ABC):
    key = 0

    def __init__(self, other_dists: list):
        super().__init__()
        self.other_cities = {}
        self.key = str(city_without_name.key)
        city_without_name.key = city_without_name.key + 1
        i = 0
        for dist in other_dists:
            if i == int(self.key):
                i = i + 1
            self.other_cities[str(i)] = dist
            i = i + 1

    def get_dist(self, other_city: city):
        if other_city.get_key() == self.key:
            return 999999  # infinity
        return self.other_cities[other_city.get_key()]

    def get_key(self):  # for printing full path
        return self.key


class graph(ABC):
    def __init__(self, cities: list[city]):
        self.cities = cities

    def get(self, c):
        return self.cities[c]

    def num_of_cities(self):
        return len(self.cities)

    @abstractmethod
    def out(self):
        pass

    @abstractmethod
    def visit_city(self, c: city):
        c.visit()


class graph_path(graph, ABC):
    def __init__(self, cities: list[city]):
        super().__init__(cities)
        self.path = ""

    def out(self):
        return self.path[:-2]

    def visit_city(self, c: city):
        super().visit_city(c)
        self.path = self.path + c.get_key() + "->"


class graph_path_len(graph, ABC):
    def __init__(self, cities: list[city]):
        super().__init__(cities)
        self.current_city = None
        self.path_len = 0

    def out(self):
        return self.path_len

    def visit_city(self, c: city):
        super().visit_city(c)
        if self.current_city is None:
            self.current_city = c
        else:
            self.path_len = self.path_len + self.current_city.get_dist(c)
            self.current_city = c
