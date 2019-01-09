import math as m


def euclid_distance(x1, x2):
    y = 0
    for i in range(len(x1)):
        y += (x1[i] - x2[i]) ** 2
    return m.sqrt(y)
