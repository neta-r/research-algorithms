class List(list):

    def __init__(self, init_lst):
        super().__init__(init_lst)

    def __getitem__(self, *args):
        try:  # if the list has 2 dimensions or more
            current = super().__getitem__(args[0][0])
            for index in args[0][1:]:
                current = current[index]
            return current
        except IndexError:
            raise IndexError
        except Exception:  # regular list
            current = super().__getitem__(args[0])
            for index in args[1:]:
                current = current[index]
            return current

    def __setitem__(self, *args):
        val = args[-1]
        try:  # if the list has 2 dimensions or more
            current = super().__getitem__(args[0][0])
            for index in args[0][1:-1]:
                current = current[index]
            current[args[0][-1]] = val # getting to one dimensional list and using regular [] operator :)
        except IndexError:
            raise IndexError
        except Exception:  # regular list
            current = self
            current[args[0]] = val


if __name__ == '__main__':
    # creating three dimensional list
    lst = List([
        [[1, 2, 3, 33], [4, 5, 6, 66]],
        [[7, 8, 9, 99], [10, 11, 12, 122]],
        [[13, 14, 15, 155], [16, 17, 18, 188]],
    ])
    # creating one dimensional list
    lst2 = List([1, 2, 3])
    # prints 122
    print(lst[1, 1, 3])
    # prints 2
    print(lst2[1])
    # prints three dimensional list before change
    print(lst)
    lst[1, 1, 3] = 5
    # prints three dimensional list after change
    print(lst)
