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
    def __init__(self, name: str, other_cities):
        super().__init__()
        self.name = name
        self.other_cities = other_cities

    def get_dist(self, other_city: city):
        if other_city.get_key() == self.name:
            return 999999  # infinity

        return self.other_cities[other_city.get_key()]

    def get_key(self):
        return self.name


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
        self.path_len = 0

    def out(self):
        return self.path_len

    def visit_city(self, c: city):
        super().visit_city(c)
        # change
        self.path_len = self.path_len + self.get_city(c)

# class city_without_name(city):
#     def __init__(self, numbins: int):
#         super().__init__(numbins)
#         self.sums = numbins * [0]
