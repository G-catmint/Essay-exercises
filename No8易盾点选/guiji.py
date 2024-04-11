import random

import numpy as np


def erjie(x0, y0, x1, y1):
    list_co = []
    span = abs(x0 - x1) if abs(x0 - x1) > abs(y0 - y1) else abs(y0 - y1)
    P = np.array([span, span / 2])
    P0, P1 = np.array([x0, y0]), np.array([x1, y1])
    x, y = [], []
    step = round(10 / span, 2)
    for t in np.arange(0, 1.01, step/random.randint(4,15)):
        p11_t = (1 - t) * P0 + t * P
        p12_t = t * P1 + (1 - t) * P
        p2_t = (1 - t) * p11_t + t * p12_t
        x.append(round(p2_t[0]))
        y.append(round(p2_t[1]))
        list_co.append([round(p2_t[0]),round(p2_t[1])])
    return list_co
    # plt.scatter(x, y, c='r', marker=".")
    # plt.axis("equal")
    # plt.show()


if __name__ == '__main__':
    erjie(41, 121, 50, 38)

