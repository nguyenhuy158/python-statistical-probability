import math


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def isEven(n):
    return n % 2 == 0


def nextPrime(n):
    if n < 2:
        return 2

    if isEven(n):
        n += 1
    else:
        n += 2

    while not (isPrime(n)):
        n += 2
    return n


# # ex1
# print("ex 1")
# print(nextPrime(1))
# print(nextPrime(3))
# print(nextPrime(11))
# print(nextPrime(19))
# # for i in range(1000):
# #     print(i) if isPrime(i) else print(end='')


def primeFact(p):
    result = []
    prime = 2
    while p != 1:
        if p % prime == 0:
            result.append(prime)
            p /= prime
        else:
            prime = nextPrime(prime)

    return result


def countSameNumber(list):
    dict = {}
    for i in list:
        oldValue = dict.get(i)
        oldValue = oldValue if oldValue != None else 0
        dict.update({i: int(oldValue) + 1})

    return dict


print(primeFact(60))
print(countSameNumber(primeFact(60)))
