import function


def fun(x: int, y: float, z):
    return x + y + z


def safe_call(f: function, *args):
    # f.__annotations__.items() returns a dict of types and names of f's arguments
    types = f.__annotations__.items()
    counter = 0
    for a in types:
        # isinstance - checks if left argument has a type as written in the right argument
        if not isinstance(args[counter], a[1]):
            raise TypeError('TypeError')
        counter = counter + 1
    # if an exception hasn't been raised it's safe to send all the arguments to f :)
    return f(*args)


if __name__ == '__main__':

    # Don't raise exception
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


