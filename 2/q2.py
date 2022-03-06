# f_results = { function_name : {argument: function(argument), other_argument: function(other_argument))
# for example - f(x) = x ** 2 , g(x) = x + 1
# {'f': { 1: 1, 2: 4}, 'g': { 1: 2, 2: 3}}
f_results = {}


def lastcall(func):
    def inner(*args, **kwargs):
        name = func.__name__
        # no key as func
        if name not in f_results.keys():
            return_val = func(*args, **kwargs)
            f_results[name] = {args: return_val}
            return return_val

        # func is a key in f_results
        else:
            # args is a key in the func dict
            if args in f_results[name]:
                print(f"I already told you that the answer is {f_results[name][args]}!")
            # args is not a key in the func dict
            else:
                return_val = func(*args, **kwargs)
                f_results[name] = {args: return_val}
                return return_val

    return inner


@lastcall
def f(x: int):
    return x ** 2


@lastcall
def g(x: int):
    return x + 1


if __name__ == '__main__':
    # new function
    val = f(2)
    if val is not None:
        print(val)  # returns 4

    # 'old' function with same key
    val = f(2)
    if val is not None:
        print(val)  # doesn't return anything - will print "I already told you that the answer is 4!"

    # 'old' function with 'old' key
    val = f(3)
    if val is not None:
        print(val)  # returns 9

    # other new function
    val = g(2)
    if val is not None:
        print(val)  # returns 3

    # 'old' function with same key
    val = g(2)
    if val is not None:
        print(val)  # doesn't return anything - will print "I already told you that the answer is 3!"

    # 'old' function with 'old' key
    val = g(5)
    if val is not None:
        print(val)  # returns 6
