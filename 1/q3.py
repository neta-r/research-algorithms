from sympy import *


def find_root(func, a, b):
    espilon = 0.00001
    # x0 will be the middle of the range
    x0 = (a + b) / 2

    # max_iter I chose is 1000000 to assure accuracy - represent maximum number of iteration
    max_iter = 1000000
    xn = x0
    for n in range(0, max_iter):
        fxn = func(xn)
        # epsilon I chose is 0.001 - represent precision
        if abs(fxn) < espilon:
            return xn
        # calculating f'(xn) according to definition - f'(x) = [f(x+h)-f(x)]/h
        dfxn = (func(xn + espilon) - func(xn)) / espilon
        if dfxn == 0:
            raise ZeroDivisionError('Zero derivative')
        # calculating next x according to newton raphson
        xn = xn - fxn / dfxn
    # this solution will not accurate because we have reached max_iter
    return xn


if __name__ == '__main__':
    f = lambda x: x ** 2 - 25
    try:
        print(find_root(f, 1, 3))
    except Exception as e:
        print(e.__traceback__)

    f = lambda x: x ** 2 - 4
    try:
        print(find_root(f, 1, 3))
    except Exception as e:
        print(e.__traceback__)
