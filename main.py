from itertools import combinations
from itertools import permutations
import numpy


def coefficient(x, y):
    x_1 = x[0]
    x_2 = x[1]
    x_3 = x[2]
    y_1 = y[0]
    y_2 = y[1]
    y_3 = y[2]

    a = y_1 / ((x_1 - x_2) * (x_1 - x_3)) + y_2 / ((x_2 - x_1) * (x_2 - x_3)) + y_3 / ((x_3 - x_1) * (x_3 - x_2))
    b = (-y_1 * (x_2 + x_3) / ((x_1 - x_2) * (x_1 - x_3)) - y_2 * (x_1 + x_3) / ((x_2 - x_1) * (x_2 - x_3)) - y_3 * (x_1 + x_2) / ((x_3 - x_1) * (x_3 - x_2)))
    c = (y_1 * x_2 * x_3 / ((x_1 - x_2) * (x_1 - x_3)) + y_2 * x_1 * x_3 / ((x_2 - x_1) * (x_2 - x_3)) + y_3 * x_1 * x_2 / ((x_3 - x_1) * (x_3 - x_2)))
    return a, b, c


comb = permutations([2, 6, 4, 4, 6, 3, 2], 3)
combArray = []
for i in comb:
    # print(i)
    # print(numpy.asanyarray(i))
    combArray.append(numpy.asanyarray(i))

comb2 = permutations([0, 1, 2, 3, 4, 5, 6], 3)
combArray2 = []
for i in comb2:
    combArray2.append(numpy.asarray(i))

for i in range(len(combArray)):
    # print(combArray[i], combArray2[2])
    print(coefficient(combArray[i], combArray2[i]))
