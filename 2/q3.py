# class List(list):
#     lst = {}
#
#     def recursive_init(self, init_lst):
#         key = 0
#         for var in init_lst:
#             if isinstance(var, list):
#                 List.recursive_init(var)
#             else:
#                 self.lst = {key: var}
#
#     def __init__(self, init_lst):
#         List.recursive_init(list)
#         super().__init__()
#

# [1,2,3,4]
# [1,2,3,4]

# [[1,2,3,4],[5,6,7,8]]
# {0 : [1,2,3,4], 1: [5,6,7,8]}

# [[[1,2],[3,4]],[[5,6,7],[8,9]]]
# {0: {0: [1,2], 1: [3,4]}, 1: {0: [5, 6, 7], 1: [8, 9]}}
import copy

other_lst = {}


def recursive_init(lst):
    temp_dict = {}
    key = 0
    for var in lst:
        if isinstance(var, list):
            temp_dict[key] = recursive_init(var)
            key = key + 1
        else:
            return lst
    return temp_dict


def wrapper(lst):
    temp_dict = {}
    key = 0
    for var in lst:
        temp_dict[key] = recursive_init(var)
        key = key + 1
    return temp_dict


if __name__ == '__main__':
    # recursive_init([
    #     [[1, 2, 3, 33], [4, 5, 6, 66]],
    #     [[7, 8, 9, 99], [10, 11, 12, 122]],
    #     [[13, 14, 15, 155], [16, 17, 18, 188]],
    # ])
    # recursive_init([1, 2, 3])

    dct = {}
    # dct[0] = recursive_init([[1, 2, 3, 4], [5, 6, 7, 8]])
    # dct[0] = recursive_init([1, 2, 3])
    wrapper([[[1,2],[3,4]],[[5,6,7],[8,9]]])
    print("meow")