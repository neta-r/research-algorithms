# f_results = { function_name : {argument: function(argument), other_argument: function(other_argument))
# for example - f(x) = x ** 2 , g(x) = x + 1
# {'f': { 1: 1, 2: 4}, 'g': { 1: 2, 2: 3}}
f_results = {}


def lastcall(func):
    def inner(*args, **kwargs):
        name = func.__name__

        if name not in f_results.keys():  # no key as func
            return_val = func(*args, **kwargs)
            key = args
            # only immutable object can be keys
            # in order to check if the return_val is immutable I'll check if the object has an iterable attribute
            if hasattr(args, '__iter__'):  # object is not immutable and can't be used as a key
                key = str(args)
            f_results[name] = {key: return_val} # inserting new function name as a key along with current result

            return return_val

        else:  # func is a key in f_results
            key = args
            if hasattr(args, '__iter__'):
                key = str(args)
            if key in f_results[name]:  # args is a key in the func dict (result exists)
                print(f"I already told you that the answer is: {f_results[name][key]}")

            else:  # args is not a key in the func dict (result doesn't exist)
                return_val = func(*args, **kwargs)
                f_results[name] = {key: return_val}  # inserting current tesult
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
