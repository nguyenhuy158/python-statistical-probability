from cmath import sqrt
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


data = pd.read_csv("iris.csv", delimiter=",")
print("Show the first 5 data points")
print(data.head(5))

# CHECK
# print(data.std())
print("Compute...")

columnsName = list(data.columns)[:4]
rowsName = ["count", "mean", "std", "min", "max"]
result = pd.DataFrame(
    [
        [
            len(data[columnsName[0]]),
            len(data[columnsName[1]]),
            len(data[columnsName[2]]),
            len(data[columnsName[3]]),
        ],
        [
            mean(data[columnsName[0]]),
            mean(data[columnsName[1]]),
            mean(data[columnsName[2]]),
            mean(data[columnsName[3]]),
        ],
        [
            std(data[columnsName[0]]),
            std(data[columnsName[1]]),
            std(data[columnsName[2]]),
            std(data[columnsName[3]]),
        ],
        [
            min(data[columnsName[0]]),
            min(data[columnsName[1]]),
            min(data[columnsName[2]]),
            min(data[columnsName[3]]),
        ],
        [
            max(data[columnsName[0]]),
            max(data[columnsName[1]]),
            max(data[columnsName[2]]),
            max(data[columnsName[3]]),
        ],
    ],
    columns=columnsName,
    index=rowsName,
)

print(result)
