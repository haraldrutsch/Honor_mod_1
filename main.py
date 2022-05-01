from itertools import combinations
from collections import Counter
import numpy


def inverseInZ7(i):  # Calculates the multiplcative inverse in Z_7
    if (i % 7 == 0):
        return 0
    else:
        return pow(((i.item()) % 7), -1, 7)


def multInZ7(a, b):  # Calculates multiplcation in mod 7
    return (a * b) % 7


def divInZ7(a, b):  # Calculates the inverse
    return multInZ7(a, inverseInZ7(b))


def addInZ7(a, b):  # Not in use
    return (a + b) % 7


def minInZ7(a, b):  # Not in use
    return (a - b) % 7


def coefficient(x, y):  # Calculated the coefficient in Z_7
    x_1 = x[0]
    x_2 = x[1]
    x_3 = x[2]
    y_1 = y[0]
    y_2 = y[1]
    y_3 = y[2]

    a = ((divInZ7(y_1, multInZ7((x_1 - x_2) % 7, (x_1 - x_3) % 7)) +
          (divInZ7(y_2, multInZ7((x_2 - x_1) % 7, (x_2 - x_3) % 7))) % 7 +
          divInZ7(y_3, multInZ7((x_3 - x_1) % 7, (x_3 - x_2) % 7))) % 7)
    b = ((divInZ7(multInZ7(-y_1 % 7, (x_2 + x_3) % 7), multInZ7((x_1 - x_2) % 7, (x_1 - x_3) % 7)) -
          divInZ7(multInZ7(y_2, (x_1 + x_3) % 7), multInZ7((x_2 - x_1) % 7, (x_2 - x_3) % 7))) % 7 -
         divInZ7(multInZ7(y_3, (x_1 + x_2) % 7), multInZ7((x_3 - x_1) % 7, (x_3 - x_2) % 7))) % 7
    c = ((divInZ7(multInZ7(y_1, multInZ7(x_2, x_3)), multInZ7((x_1 - x_2) % 7, (x_1 - x_3) % 7)) +
          divInZ7(multInZ7(y_2, multInZ7(x_1, x_3)), multInZ7((x_2 - x_1) % 7, (x_2 - x_3) % 7))) % 7 +
         divInZ7(multInZ7(y_3, multInZ7(x_1, x_2)), multInZ7((x_3 - x_1) % 7, (x_3 - x_2) % 7))) % 7

    return a, b, c


def most_frequent(List):  # gives most frequent element in a list of lists
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]


comb = combinations([3, 6, 4, 5, 3, 3, 2], 3)  # creates an array of all possible combinations
combArray = []
for i in comb:
    combArray.append(numpy.asanyarray(i))

comb2 = combinations([0, 1, 2, 3, 4, 5, 6], 3)  # creates an array of the complimentary coordinates
combArray2 = []
for i in comb2:
    combArray2.append(numpy.asarray(i))

out = []
for i in range(len(combArray)):
    list2, list1 = zip(*sorted(zip(combArray2[i], combArray[i])))  # first sorts the points and then computes the polynomial
    out.append(coefficient(list1, list2))  # adds the result to the final list

print(Counter(out).most_common()) # prints the list of result sorted by occurrence
