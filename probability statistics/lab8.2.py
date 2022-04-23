from cmath import sqrt
from unittest import result
import pandas as pd
import numpy as np


def sum(L):
    total = 0
    for i in L:
        total += i

    return total


def mean(L):
    return sum(L) / len(L)


def std(L):
    meanL = mean(L)
    varianceL = 0
    for i in L:
        varianceL += pow(meanL - i, 2)

    return pow(varianceL / (len(L) - 1), 0.5)


def min(L):
    result = L[0]
    for i in L:
        if i < result:
            result = i
    return result


def max(L):
    result = L[0]
    for i in L:
        if i > result:
            result = i
    return result


data = pd.read_csv("population.csv", delimiter=",")
print("Show the first 5 data points")
print(data.head(5))

columnsName = list(data.columns)[:2]
columnsName.extend(["Mean", "Std", "Min", "Max"])

table = [
    [
        list(data.groupby([columnsName[0], columnsName[1]]))[index][0][0],
        list(data.groupby([columnsName[0], columnsName[1]]))[index][0][1],
        mean(
            list(
                pd.DataFrame(
                    list(data.groupby([columnsName[0], columnsName[1]]))[index][1]
                )["Value"]
            )
        ),
        std(
            list(
                pd.DataFrame(
                    list(data.groupby([columnsName[0], columnsName[1]]))[index][1]
                )["Value"]
            )
        ),
        min(
            list(
                pd.DataFrame(
                    list(data.groupby([columnsName[0], columnsName[1]]))[index][1]
                )["Value"]
            )
        ),
        max(
            list(
                pd.DataFrame(
                    list(data.groupby([columnsName[0], columnsName[1]]))[index][1]
                )["Value"]
            )
        ),
    ]
    # for index in range(10)
    for index in range(len(list(data.groupby([columnsName[0], columnsName[1]]))))
]

print(len(list(data.groupby([columnsName[0], columnsName[1]]))))

result = pd.DataFrame(table, columns=columnsName)
print(result)
