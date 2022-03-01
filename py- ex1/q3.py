from sympy import *



def f(x):
    return x ** 2 - 4


x = symbols('x')
sqr = f(x)
eps = 0.001


def find_root(func, a, b):
    # calculate derivative with sympy library
    f_derivative = func.diff(x)
    # turns sympy expression into functions
    func = lambdify(x, func)
    f_derivative = lambdify(x, f_derivative)

    # x0 will be the middle of the range
    x0 = (a+b)/2

    # max_iter I chose is 1000000 to assure accuracy - represent maximum number of iteration
    max_iter = 100000000
    xn = x0
    for n in range(0, max_iter):
        fxn = func(xn)
        # epsilon I chose is 0.001 - represent precision
        if abs(fxn) < 0.001:
            return xn
        dfxn = f_derivative(xn)
        if dfxn == 0:
            raise ZeroDivisionError('Zero derivative')
        # calculating next x according to newton raphson
        xn = xn - fxn / dfxn
    # this solution will not accurate because we have reached max_iter
    return xn


if __name__ == '__main__':
    x = symbols('x')
    f = x ** 2 - 25
    try :
        print(find_root(f, 1, 3))
    except Exception as e:
        print(e.__traceback__)

    x = symbols('x')
    f = x ** 2 - 4
    try:
        print(find_root(f, 1, 3))
    except Exception as e:
        print(e.__traceback__)
