def thieves(x):
    if x <= 0:
        return 0
    if x == 1:
        return 1
    if x == 2:
        return 2

    # total = 0
    # for i in range(x - 1, 0, -1):
    #     total += thieves(i)
    # return x + total
    return x + thieves_sum(x - 1)


def thieves_sum(n):
    if n <= 0:
        return 0
    else:
        return thieves(n) + thieves_sum(n - 1)


def isSent(day, n=40):
    # print("n", n - thieves_sum(day))
    # if thieves(day) <= (n - thieves_sum(day)):
    if n - thieves_sum(day-1) - thieves(day) >= 0:
        return True
    return False


def maxDay(n=40):
    print(n)
    day = 0
    while isSent(day, n):
        day += 1

    return day - 1


def rishest(x):
    if x == 0:
        return 0
    else:
        preRishest = rishest(x-1)
        return x if rishestMan[x] > rishestMan[preRishest] else preRishest


def waytochoose(n, k):
    if k == 0 or k == n:
        return 1
    if k == 1:
        return n
    return waytochoose(n-1, k) + waytochoose(n-1, k-1)


def waytochooseP(n, k):
    if k == 0 or k == n:
        return 1
    if k == 1:
        return n
    return n * waytochooseP(n-1, k-1)


def countCharacterAppeared(store):
    if store <= 1:
        return 1
    return 2*countCharacterAppeared(store-1)


def F(n):
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return n
    # if n < 2:
    #     return 1

    return F(n-1)+F(n-2)


def towerOfHanoi(A, B, C):
    def move(step, s, t, mid):
        if step > 0:
            move(step - 1, s, mid, t)

            t[1].append(s[1].pop())

            print(A)
            print(B)
            print(C)
            print('='*50)

            move(step - 1, mid, t, s)

    move(len(A[1]), A, C, B)


# MAIN FUNCTION
if __name__ == "__main__":
    # ex1
    print('='*100)
    print("Exericises 1".upper())
    if True:
        thieve = 40
        print("default thieves man is", thieve)
        isChange = input("type c if you want to change: ")
        if isChange == 'c':
            thieve = int(input("enter new thieve: "))

        print("ngay cuoi co the gui linh di la", maxDay(thieve))

        for i in range(1,  maxDay(thieve) + 3):
            day = i
            print(
                "day",
                day,
                "con lai", thieve - thieves_sum(day - 1),
                "ten cuop phai sai di",
                thieves(day),
                "sai di",
                "duoc" if isSent(day, thieve) else "khong",
                "con lai", thieve - thieves_sum(day)
            )

    # ex2
    print('='*100)
    print("Exericises 2".upper())

    if True:
        rishestMan = [100, 101, 50, 20, 200]
        print("default rishest man is", rishestMan)
        isChange = input("type c if you want to change: ")
        if isChange == 'c':
            n = int(input("enter number of people: "))
            rishestMan = []
            for i in range(n):
                asset = float(input("enter person's money", i, ""))
                rishestMan.append(asset)

        rank = 0
        print("default rank is", rank)
        isChange = input("type c if you want to change: ")
        if isChange == 'c':
            while True:
                rank = int(input("enter new rank: "))
                if rank < len(rishestMan):
                    break
                else:
                    print("error please enter correctly")

        rishest = rishest(rank)
        print("people rishest in", rank,
              "first people is", rishest, "in", rishestMan)

    # ex3
    print('='*100)
    print("Exericises 3".upper())

    if True:
        n = 50
        way = 1000
        print("default n=", n)
        isChange = input("type c if you want to change: ")
        if isChange == 'c':
            n = int(input("enter new n: "))

        print("default way=", way)
        isChange = input("type c if you want to change: ")
        if isChange == 'c':
            way = int(input("enter new way: "))

        # minSub = way
        # k = n
        i = 0
        while waytochoose(n, i) < way:
            # print(waytochoose(n, i))

            # t_minSub = way - waytochoose(n, i)
            # if t_minSub < minSub:
            #     minSub = t_minSub
            #     k = i

            i += 1

        print(
            "the", i, "that give the number of ways to choose as close to", way, "as possible.")
        print("with n=", n, "way=", way)

    # ex4
    print('='*100)
    print("Exericises 4".upper())

    if True:
        n = 50
        way = 10000
        print("default n=", n)
        isChange = input("type c if you want to change: ")
        if isChange == 'c':
            n = int(input("enter new n: "))

        print("default way=", way)
        isChange = input("type c if you want to change: ")
        if isChange == 'c':
            way = int(input("enter new way: "))

        i = 0
        while waytochooseP(n, i) < way:
            print(waytochooseP(n, i))
            i += 1

        print(
            "the", i, "that give the number of ways to choose as close to", way, "as possible.")
        print("with n=", n, "way=", way)

    # ex5
    print('='*100)
    print("Exericises 5".upper())

    if True:
        stories = 547
        print("default stories=", stories)
        isChange = input("type c if you want to change: ")
        if isChange == 'c':
            stories = int(input("enter new stories: "))
        print("character appeared in", stories,
              "stories in", countCharacterAppeared(stories))

    # ex6
    print('='*100)
    print("Exericises 6".upper())

    if True:
        n = 10
        print("default n=", n)
        isChange = input("type c if you want to change: ")
        if isChange == 'c':
            n = int(input("enter new n: "))

        for i in range(n+2):
            print(F(i), end=" ")
        print("...")
        print("so fibo thu ", n, "la", F(n-1))

    # ex7
    print('='*100)
    print("Exericises 7".upper())

    if True:
        n = 64
        n = 3
        print("default n=", n)
        isChange = input("type c if you want to change: ")
        if isChange == 'c':
            n = int(input("enter new n: "))

        A = [['A'], [i for i in range(n, 0, -1)]]
        B = [['B'], []]
        C = [['C'], []]
        towerOfHanoi(A, B, C)
