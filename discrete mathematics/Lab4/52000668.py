import math

print('=' * 10, '1', '=' * 10)

# P = "Phong has Visa"
# S1 = "If Phong can fly, Phong will go to America"
# S2 = "If Phong has Visa, Phong will go to America"
# S3 = "If Phong can speak English, Phong will go to America"
# Conclusion: C = "Phong goes to America"

print("P and S2 -> C")
print("If Phong has Visa, Phong will go to America (by S2)")
print("Phong has Visa (by P)")
print("C: Phong goes to America (by Modus Ponens)")

# P = "It’s hot yesterday"
# S1 = "If it’s hot, it will rain the next day"
# S2 = "If and only if it’s not rain, Nam goes outside" <=>
# if it's not rain, Nam goes outside ^ if Nam goes outside, it's not rain
# S3 = "If it’s not hot, Nam will go outside"
# Conclusion: C = "Nam goes outside"

print("S1 and P -> C1")
print("If it’s hot, it will rain the next day (by S1)")
print("It’s hot yesterday (by P)")
print("C1: It's rain today (by Modus Ponens)")

print("C1 and S2 -> C2")
print("If and only if it’s not rain, Nam goes outside (by S2)")
print(
    "if it's not rain, Nam goes outside ^ if Nam goes outside, it's not rain (by sepecialization)"
)
print("It's rain today (by C1)")
print("C2: Nam doesn't goes outside (by Modus Tollens)")

# Q = "An wake up late"
# R = "The traffic is flowing smooth"
# S1 = "The traffic is always heavy on school day"
# S2 = "If An wake up late, he will be late for school on school day"
# S3 = "An only have to go to school on school day"
# S4 = "If An don’t have to go to school, An can’t be late for school"
# Conclusion: C = "An is late for school"

print("S1 and R -> C1")
print("The traffic is always heavy on school day (by S1)")
print("if it's school day, the traffic will be heavy (by S1)")
print("The traffic is flowing smooth (by R)")
print("C1: It is not school day (by Modus Ponens)")

print("S2 and C1 -> C2")
print("If An don’t have to go to school, An can’t be late for school (by S4)")
print("It is not school day (by C1)")
print("C: An is not late for school (by Modus Ponens)")
print("disprove")

# 2
print('=' * 10, '2', '=' * 10)
PROVE = "the given statement is correct when x equal to "
DISPROVE = "the given statement is incorrect for all values x within the given domain."


def printProveorDisprove(x=''):
    print(PROVE, x) if (len(x) != 0) else print(DISPROVE)


# ∃x ∈ Z, 0 ≤ x ≤ 100, x^2 = 15^2 + 16^2
def ex2a():
    n = 100 + 1
    for x in range(n):
        if (x**2 == 15**2 + 16**2):
            printProveorDisprove(str(x))
            return

    printProveorDisprove()
    return


# ∃x ∈ Z, 0 ≤ x ≤ 100, x^2 = 12^2 + 16^2
def ex2b():
    n = 100 + 1
    for x in range(n):
        if (x**2 == 12**2 + 16**2):
            printProveorDisprove(str(x))
            return

    printProveorDisprove()
    return


# ∃x ∈ Z, −50 ≤ x ≤ 50, x^2 ≥ 99*x
def ex2c():
    n = 100 + 1
    for x in range(-50, 50 + 1):
        if (x**2 >= 99 * x):
            printProveorDisprove(str(x))
            return

    printProveorDisprove()
    return


# ∃x ∈ Z, 50 ≤ x ≤ 100, x(x + 1)(x + 2)%6 != 0
def ex2d():
    n = 100 + 1
    for x in range(-50, n):
        if ((x * (x + 1) * (x + 2)) % 6) != 0:
            printProveorDisprove(str(x))
            return

    printProveorDisprove()
    return


# ∃x, y ∈ Z, 0 ≤ x ≤ 100, √(x + y) = √x + √y
def ex2e():
    n = 100 + 1
    for x in range(n):
        for y in range(n):
            if pow(x + y, 1 / 2) == pow(x, 1 / 2) + pow(y, 1 / 2):
                printProveorDisprove('[{}, {}]'.format(str(x), str(y)))
                return

    printProveorDisprove()
    return


def ex2(start, end, vePhai):
    for x in range(start, end):
        if x**2 == vePhai:
            printProveorDisprove('[{}, {}]'.format(str(x), str(y)))
            return

    printProveorDisprove()
    return


#  ex2(min, max)
ex2b()
ex2c()
ex2d()
ex2e()

# ex3
print('=' * 10, '3', '=' * 10)
PROVE = 'Prove'
DISPROVE = 'Disprove'


def ex3a(min, max):
    for x in range(min, max + 1):
        if not (x**3 >= x):
            return DISPROVE
    return PROVE


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, math.floor(math.sqrt(n))):
        if n % i == 0:
            return False
    return True


def ex3b(min, max):
    for x in range(min, max + 1):
        if x % 2 == 0:
            if not (isPrime(x * 3 + 1)):
                return DISPROVE

    return PROVE


def ex3c(min, max):
    for x in range(min, max + 1):
        if x % 2 == 0:
            if not (isPrime(x * 5 + 3)):

                return DISPROVE

    return PROVE


def ex3d(min, max):
    for c in range(min, max + 1):
        if c % 4 == 0:
            for a in range(min, max + 1):
                for b in range(min, max + 1):
                    if c**2 == a**2 + b**2:
                        return PROVE

    return DISPROVE


def ex3e(min, max):
    for c in range(min, max + 1):
        if c % 5 == 0:
            for a in range(min, max + 1):
                for b in range(min, max + 1):
                    if c**2 == a**2 + b**2:
                        return PROVE

    return DISPROVE


def ex3f(min, max):
    for c in range(min, max + 1):
        if c**2 <= c:
            return PROVE

    return DISPROVE


print(ex3a(0, 100))
print(ex3b(0, 100))
print(ex3c(1, 100))
print(ex3d(0, 100))
print(ex3e(0, 100))
print(ex3f(0, 100))

# ex4
print('=' * 10, '4', '=' * 10)


# sum x! > 20!
def ex4b(min, max, rightExp):
    leftExp = 0
    for i in range(min, max + 1):
        leftExp += factorial(i)

    return PROVE if leftExp > rightExp else DISPROVE


def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


def ex4a(min, max):
    leftExp = 0
    rightExp = 0

    for x in range(min, max + 1):
        for y in range(min, max + 1):
            leftExp += (x + y)**2
            rightExp += (x + 2 * y)**2

    return PROVE if leftExp > rightExp else DISPROVE


def ex4c(min, max, rightExp):
    leftExp = 0
    for x in range(min, max + 1):
        leftExp += 3 * (x**2)

    return PROVE if leftExp >= rightExp else DISPROVE


def ex4d(min, max, rightExp):
    leftExp = 0
    for x in range(min, max + 1):
        leftExp += (4 * (x**3) + 6 * (x**2) + 2 * x)

    return PROVE if leftExp > rightExp else DISPROVE


print("a", ex4a(0, 10))
print("b", ex4b(0, 10, factorial(20)))
print("c", ex4c(0, 10, 10**3))
# print("d", ex4d(0, 10, 10 ** 4 + 2 * 10 ** 3 + 10 ** 2 - 5 ** 4 - 2 * 5 ** 3 - 5    ** 2))
print("d", ex4d(0, 10, 11200))

# ex5
print('=' * 10, '5', '=' * 10)
print("a.", '=' * 10)
print("p -> r (1)")
print("~p -> q (2)")
print("q -> s (3)")

print("step 1")
print("~p -> q (2)")
print("q -> s (3)")
print("(2) + (3) -> ~p -> s (by Transitivity) (4)")

print("step 2")
print("p -> r (1)")
print("(1) <-> ~r -> ~p (by contrapositive) (5)")

print("step 3")
print("~p -> s (4)")
print("~r -> ~p (5)")
print("(4) + (5) -> ~r -> s (by Transitivity) (4)")
print("Prove")

print("b.", '=' * 10)
print("p -> (q -> r) (1)")
print("p V s (2)")
print("t -> q (3)")
print("~s (4)")

print("step 1")
print("p V s (2)")
print("~s (4)")
print("(2) + (4) -> p (by Elimination) (5)")

print("step 2")
print("p (5)")
print("p -> (q -> r) (1)")
print("(5) + (1) -> q -> r (by Modus Ponens) (6)")

print("step 3")
print("t -> q (3)")
print("q -> r (6)")
print("(3) + (6) -> t -> r (by Transitivity) (7)")

print("step 4")
print("(7) <-> ~r -> ~t (by contrapositive) (8)")
print("Prove")

print("c.", '=' * 10)
print("p -> q (1)")
print("~r V s (2)")
print("p V r (3)")

print("step 1")
print("(3) <-> ~p -> r (by representation of if-then as or) (4)")

print("step 2")
print("(2) <-> r -> s (by representation of if-then as or) (5)")

print("step 3")
print("(1) <-> ~q -> ~p (by contrapositive) (6)")

print("step 4")
print("~q -> ~p (6)")
print("~p -> r (4)")
print("(6) + (4) -> ~q -> r (by Transitivity) (7)")
print("Prove")

print("d.", '=' * 10)
print("p (1)")
print("p -> r (2)")
print("p -> (q V ~r) (3)")
print("~q V ~s (4)")

print("step 1")
print("p (1)")
print("p -> r (2)")
print("(1) + (2) -> r (by Modus Ponens) (5)")

print("step 2")
print("p (1)")
print("p -> (q V ~r) (3)")
print("(1) + (3) -> q V ~r (by Modus Ponens) (6)")

print("step 3")
print("(6) <-> q V ~r (by contrapositive) (7)")

print("step 4")
print("(4) <-> q V ~s (by representation of if-then as or) (8)")

print("step 5")
print("(8) <-> s -> ~q (by contrapositive) (9)")

print("step 6")
print("(9) + (7) -> s -> ~r (by Transitivity) (10)")
print("Diprove")
