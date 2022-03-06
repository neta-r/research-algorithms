import function

def func(x, y: float, z: int):
    return x + y + z


def fun(x: int, y: float, z):
    return x + y + z


def safe_call(f: function, *args):
    # f.__annotations__.items() returns a dict of types and names of f's arguments
    args_with_types = f.__annotations__.keys()
    the_types = f.__annotations__
    all_args = f.__code__.co_varnames
    args_counter = 0
    for a in all_args:
        # check if a has a type
        if a in args_with_types:

            if the_types[a] == 'str':
                assert (type(a) == str)

            # isinstance - checks if left argument has a type as written in the right argument
            elif not isinstance(args[args_counter], the_types[a]):
                raise TypeError('TypeError')
        args_counter = args_counter + 1

    # num_of_args = number of arguments expected
    # counter = actual number of arguments
    num_of_args = f.__code__.co_argcount
    if args_counter != num_of_args:
        raise Exception('DifferentNumberOfArgs')

    # if an exception hasn't been raised it's safe to send all the arguments to f :)
    return f(*args)


if __name__ == '__main__':

    # Don't raise exception - print 4.7
    try:
        print(safe_call(fun, 1, 0.7, 3))
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")

    # Raise TypeError exception
    try:
        print(safe_call(fun, 2, "h", 3))
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")

    # Raise TypeError exception
    try:
        print(safe_call(fun, 2.0, 0, 3))
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")

    # Raise IndexError exception (too few arguments)
    try:
        print(safe_call(fun, 2))
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")

    # Don't raise exception - print 15.0
    try:
        print(safe_call(func, 2, 4.0, 9))
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")

