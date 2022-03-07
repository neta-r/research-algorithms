class List(list):

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
        self.lst = {}
        self.dim1 = True
        key = 0
        for var in init_lst:
            if isinstance(var, list):
                self.lst[key] = self.recursive_init(var)
                self.dim1 = False
            else:  # simple list
                self.lst = init_lst
                break
            key = key + 1
        super().__init__()

    def __getitem__(self, *args):
        if self.dim1:
            return self.lst[args[0]]
        else:
            var = self.lst[args[0][0]]
            for index in args[0][1:]:
                var = var[index]
        return var

    def __setitem__(self, *args):
        val = args[-1]
        if self.dim1:
            self.lst[args[0]] = val
            return
        else:
            var = self.lst[args[0][0]]
            for index in args[0][1:-1]:
                var = var[index]
        var[args[0][-1]] = val


if __name__ == '__main__':
    lst = List([
        [[1, 2, 3, 33], [4, 5, 6, 66]],
        [[7, 8, 9, 99], [10, 11, 12, 122]],
        [[13, 14, 15, 155], [16, 17, 18, 188]],
    ])
    lst2 = List([1, 2, 3])
    print(lst[1, 1, 3])
    print(lst2[1])
    print(lst[1, 1, 3])
    lst[1, 1, 3] = 5
    print(lst[1, 1, 3])
    # print(lst)
    # regular = [[[1, 2, 3, 33], [4, 5, 6, 66]], [[7, 8, 9, 99], [10, 11, 12, 122]], [[13, 14, 15, 155], [16, 17, 18, 188]]]
    # regular.__setitem__((1,1,1),0)
