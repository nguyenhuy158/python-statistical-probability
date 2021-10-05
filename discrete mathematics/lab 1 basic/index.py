def exercises1():
    print(15 * 2 + 7 * 8)
    print(20 - 15 + 15 * 2)
    print(20 + 30 - 3 * 15 + 5 * 5 ^ 2)
    print(((4 / 6) + (2 / 6)) / ((5 / 2) + (1 / 2)))
    print((14 / 2) + 7)
    print((5 * 2) / (5 - 20 * 3 ^ 2 + 30))


def exercises2():
    print("20 - 15 + 15 * 2) = {}".format(20 - 15 + 15 * 2))
    print("20 + 30 - 3 * 15 + 5 * 5^2 ) = {}".format(20 + 30 - 3 * 15 + 5 * 5 ^ 2))
    print("((4 / 6) + (2 / 6)) / ((5 / 2) + (1 / 2)) ) = {}".format(
        ((4 / 6) + (2 / 6)) / ((5 / 2) + (1 / 2))))
    print("(14 / 2) + 7 ) = {}".format((14 / 2) + 7))
    print("(5 * 2) / ( 5 - 20 * 3^2 + 30) = {}".format((5 * 2) / (5 - 20 * 3 ^ 2 + 30)))


def exercises3():
    def sumN(n=0):
        result = ''
        sum = 0
        if n > 0:
            for i in range(n):
                sum += i
                result += '{}+'.format(i)
            result += '{}={}'.format(n, sum + n)
        else:
            for i in range(0, n, -1):
                sum += i
                result += '{}+'.format(i) if i == 0 else '({})+'.format(i)
            result += '(-{})={}'.format(-n, sum + n)

        return result

    print(sumN(2))
    print(sumN(5))
    print(sumN(-5))


def exercises4():
    s = input("enter= ")

    a = s.split()
    print(''.join(a))

    a = s.split()
    print('_'.join(a))


def exercises5():
    s = input("enter= ")

    if s.find("-") != -1:
        first = s[: s.find("-")]
        second = s[s.find("-") + 1:]
        print(s, '=', int(first) - int(second))
        return

    if s.find("+") != -1:
        first = s[: s.find("+")]
        second = s[s.find("+") + 1:]
        print(s, '=', int(first) + int(second))
        return

    if s.find("*") != -1:
        first = s[: s.find("*")]
        second = s[s.find("*") + 1:]
        print(s, '=', int(first) * int(second))
        return

    if s.find("/") != -1:
        first = s[: s.find("/")]
        second = s[s.find("/") + 1:]
        print(s, '=', int(first) / int(second))
        return

    if s.find("^") != -1:
        first = s[: s.find("^")]
        second = s[s.find("^") + 1:]
        print(s, '=', pow(int(first), int(second)))
        return

    if s.find("%") != -1:
        first = s[: s.find("%")]
        second = s[s.find("%") + 1:]
        print(s, '=', int(first) % int(second))
        return

    print(s, '=', s)


def exercises6():
    def add(first, second):
        return first + second

    def minus(first, second):
        return first - second

    def time(first, second):
        return first * second

    def divide(first, second):
        return first / second

    def modulus(first, second):
        return first % second

    def getOperatorIndex(epx=""):
        for index, letter in enumerate(epx):
            if not letter.isnumeric():
                return index

        return -1

    operators = {
        '+': add,
        '-': minus,
        '*': time,
        '/': divide,
        '^': pow,
        '%': modulus
    }

    s = input("please enter epx Ex: 1+2. Enter: ")
    index = getOperatorIndex(s)
    if index != -1:
        # print(s[index]) # operator
        # print(s[:index]) # first number
        # print(s[index + 1:]) # second number
        print(s, '=', operators[s[index]](int(s[:index]), int(s[index + 1:])))
    else:
        print(s, '=', s)


def exercises7():
    def mSum(A, B):
        rowA = len(A)
        columnA = len(A[0])
        rowB = len(B)
        columnB = len(B[0])
        # print(rowA == rowB)
        # print(columnA == columnB)
        C = [[0 for i in range(columnA)] for j in range(rowA)]
        # print(C)
        if rowA == rowB and columnA == columnB:
            for row in range(rowA):
                for column in range(columnA):
                    C[row][column] = A[row][column] + B[row][column]
        else:
            # print("Matrix dimension error")
            return "Matrix dimension error"

        return C

    print(mSum([[1], [2]], [[1], [2]]))
    print(mSum([[1], [2], [3]], [[1], [2]]))

    a = [[1, 2, 3],
         [4, 5, 6]]

    b = [[1, 1, 1],
         [1, 1, 1]]
    print(mSum(a, b))


def exercises8():
    def mSum(A, B):
        rowA = len(A)
        columnA = len(A[0])
        rowB = len(B)
        columnB = len(B[0])

        C = [[0 for i in range(columnB)] for j in range(rowA)]
        # print(C)
        if columnA == rowB:
            for row in range(rowA):
                for column in range(columnB):
                    for k in range(columnA):
                        C[row][column] += A[row][k] * B[k][column]
        else:
            # print("Matrix dimension error")
            return "Matrix dimension error"

        return C

    print(mSum([[1], [2]], [[1], [2]]))
    print(mSum([[1], [2], [3]], [[1], [2]]))

    a = [[1, 2, 3],
         [4, 5, 6]]

    b = [[2, 2],
         [2, 1],
         [3, 3]]
    print(mSum(a, b))


def exercises9():
    def ithCombine(p, q):
        return 'if {}, then {}'.format(p, q)

    def panqCombine(p, q):
        return '{} and {} not {}'.format(p, q[: q.find(" ")], q[q.find(" ") + 1:])

    def npoqCombine(p, q):
        return '{} not {}, or {}'.format(p[: p.find(" ")], p[p.find(" ") + 1:], q)

    p = 'it sunny'
    q = 'I go camping'
    print(ithCombine(p, q))
    print(panqCombine(p, q))
    print(npoqCombine(p, q))


if __name__ == '__main__':
    exercises = {
        1: exercises1,
        2: exercises2,
        3: exercises3,
        4: exercises4,
        5: exercises5,
        6: exercises6,
        7: exercises7,
        8: exercises8,
        9: exercises9}

    # print(exercises[1]())
    while True:
        # Example you can enter 1 or 2 or .. or e
        user = input("select exercises(1), exercises(2), ..., exercises(9) or (e)xit. You choose: ")
        if user == 'e':
            print("see yah")
            break
        if user.isnumeric() and 0 < int(user) < 10:
            exercises[int(user)]()
        else:
            print("please enter correct form <3")
