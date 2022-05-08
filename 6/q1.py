import math

import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt


def plotIntersection(num_range, f, g):
    results = set()
    for i in range(math.ceil(num_range.min()), math.ceil(num_range.max())):
        temp = fsolve(lambda x: f(x) - g(x), i)
        if round(f(temp)[0], 3) == round(g(temp)[0], 3):
            results.add(round(temp[0], 3))
    for res in results:  # plotting the intersection in red, zorder=2 will output it on top of f and g
        plt.scatter(res, f(res), c='r', zorder=3)
    plt.plot(num_range, f(num_range), zorder=2)  # plotting f, zorder=1 will output it below the roots
    plt.plot(num_range, g(num_range), zorder=2)  # plotting g, zorder=1 will output it below the roots
    plt.grid(zorder=1)
    plt.show()


if __name__ == '__main__':
    f1 = lambda x: x ** 2
    f2 = lambda x: x + 10
    plotIntersection(np.linspace(-10, 10, 1000), f1, f2)
    g1 = lambda x: np.sin(x)
    g2 = lambda x: 0.2*x
    plotIntersection(np.linspace(-10, 10, 1000), g1, g2)
    h1 = lambda x: np.cos(x)
    h2 = lambda x: x+6
    plotIntersection(np.linspace(-8, 4, 1000), h1, h2)
    plotIntersection(np.linspace(0, 4, 1000), g1, h1)
    plotIntersection(np.linspace(-20, 0, 1000), f2, g2)

