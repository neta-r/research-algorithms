# [1,2,3,4]
# [1,2,3,4]

# [[1,2,3,4],[5,6,7,8]]
# {0 : [1,2,3,4], 1: [5,6,7,8]}

# [[[1,2],[3,4]],[[5,6,7],[8,9]]]
# {0: {0: [1,2], 1: [3,4]}, 1: {0: [5, 6, 7], 1: [8, 9]}}

class List(list):
    lst = {}

    def recursive_init(self, init_lst):
        temp_dict = {}
        key = 0
        for var in init_lst:
            if isinstance(var, list):
                temp_dict[key] = self.recursive_init(var)
                key = key + 1
            else:
                super().__init__(init_lst)
                return init_lst
        return temp_dict

    def __init__(self, init_lst):
        key = 0
        for var in init_lst:
            self.lst[key] = self.recursive_init(var)
            key = key + 1
        super().__init__()


if __name__ == '__main__':
    lst = List([
        [[1, 2, 3, 33], [4, 5, 6, 66]],
        [[7, 8, 9, 99], [10, 11, 12, 122]],
        [[13, 14, 15, 155], [16, 17, 18, 188]],
    ])

