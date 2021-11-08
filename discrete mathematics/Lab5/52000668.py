# # ex1
# print("="*10, "1", "="*10)
# P = "You get good grade in the midterm exam"
# Q = "You understand how to solve all the exercises in the book"
# print("P ", P)
# print("Q ", Q)


# # 1a
# # (a) You get good grade in the midterm exam if you understand how to
# # solve all the exercises in the book, and if you will get good grade
# # in the midterm exam means you understand how to solve all the
# # exercises in the book, .
# print("="*10, "1a", "="*10)
# print("Q -> P ^ P -> Q")
# print("Q <-> P")

# # 1b
# # (b) You understand how to solve all the exercises in the book, but you
# # did not get good grade in the midterm exam
# print("="*10, "1b", "="*10)
# print("Q ^ ~P (by Negation Q -> P)")

# # (c) By understand how to solve all the exercises in the book, you will
# # get good grade in the midterm exam
# print("="*10, "1c", "="*10)
# print("Q -> P")


# # ex2
# print("="*10, "2", "="*10)
# P = "You get good grade in the midterm exam"
# Q = "You understand how to solve all the exercises in the book"
# print("P ", P)
# print("Q ", Q)

# # 2a
# # (a) You get good grade in the midterm exam if you understand how to
# # solve all the exercises in the book, and if you will get good grade
# # in the midterm exam means you understand how to solve all the
# # exercises in the book, .
# print("="*10, "2a", "="*10)
# print("Q <-> P")
# print(
#     "you get good grade in the midterm exam if, and only if you understand how to solve all the exercises in the book"
# )

# # (b) You understand how to solve all the exercises in the book, but you
# # did not get good grade in the midterm exam
# print("="*10, "2b", "="*10)
# print("Q ^ ~P")
# print("Q: you understand how to solve all the exercises in the book")
# print("~P: you did not get good grade in the midterm exam")
# print(
#     "if you understand how to solve all the exercises in the book then you get good grade in the midterm exam"
# )
# # OR
# #  print(
# #      "it is not the case that you understand how to solve all the exercises in the book then you get good grade in the midterm exam"
# #  )

# # (c) By understand how to solve all the exercises in the book, you will
# # get good grade in the midterm exam
# print("="*10, "2c", "="*10)
# print("Q -> P")
# print(
#     "if you understand how to solve all the exercises in the book then you will get good grade in the midterm exam"
# )

# # ex3
# print("="*10, "3", "="*10)
# P = "You get good grade in the midterm exam"
# Q = "You understand how to solve all the exercises in the book"
# print("P   ", P)
# print("Q   ", Q)
# print("P:  You get good grade in the midterm exam")
# print("~P: You did not get good grade in the midterm exam")
# print("Q:  You understand how to solve all the exercises in the book")
# print("~Q: You do not understand how to solve all the exercises in the book")

# print("="*10, "3a", "="*10)
# print(
#     "You get good grade in the midterm exam if, and only if you understand how to solve all the exercises in the book"
# )

# print("negative")
# print("~(Q <-> P)")
# print("~(Q -> P ^ P -> Q)")
# print("~(Q -> P ^ P -> Q)")
# print("~(Q -> P) V ~(P -> Q)")
# print("Q ^ ~P V P ^ ~Q")
# print("You understand how to solve all the exercises in the book and",
#       "you did not get good grade in the midterm exam or",
#       "you get good grade in the midterm exam and",
#       "you do not understand how to solve all the exercises in the book")

# print("converse: none")
# print("contrapositive: none")

# # (b)
# print("="*10, "3b", "="*10)
# print(
#     "it is not the case that you understand how to solve all the exercises in the book then you get good grade in the midterm exam"
# )
# print("Q ^ ~P")
# print("negative")
# print("~(Q ^ ~P)")
# print("Q -> P")
# print(
#     "if you understand how to solve all the exercises in the book then you will get good grade in the midterm exam"
# )
# print("converse: none")
# print("contrapositive: none")

# # (c)
# print("="*10, "3c", "="*10)
# print(
#     "if you understand how to solve all the exercises in the book then you will get good grade in the midterm exam"
# )
# print("Q -> P")
# print("negative")
# print("~(Q -> P)")
# print("Q ^ ~P")
# print(
#     "You get good grade in the midterm exam and You do not understand how to solve all the exercises in the book"
# )

# print("Q -> P")
# print("converse")
# print("P -> Q)")  # converse
# print(
#     "if You get good grade in the midterm exam then You understand how to solve all the exercises in the book"
# )

# print("Q -> P")
# print("contrapositive")
# print("~P -> ~Q)")  # contrapositive
# print(
#     "if You did not get good grade in the midterm exam then You do not understand how to solve all the exercises in the book"
# )


# print("Q -> P")
# print("inverse")
# print("~Q -> ~P)")  # INVERSE
# print(
#     "if You do not understand how to solve all the exercises in the book then You do not understand how to solve all the exercises in the book"
# )

# #  print("P -> Q")
# #  print("~Q -> ~P")  # contrapositive
# #  print("Q -> P")  # converse
# #  print("~P -> ~Q")  # inverse


# # ex4
# print("="*10, "4", "="*10)
# print("="*10, "4a", "="*10)
# print("p: Phong has Visa")
# print("q: Phong can fly")
# print("r: Phong can speak English")
# print("t: Phong goes to America")
# print('P ="Phong has Visa"')
# print('S1="If Phong can fly, Phong will go to America"')
# print('S2="If Phong has Visa, Phong will go to America"')
# print('S3="If Phong can speak English, Phong will go to America"')
# print('Conclusion : C ="Phong goes to America"')

# print('-'*20)
# print('P = p')
# print('S1= q -> t')
# print('S2= p -> t')
# print('S3= r -> t')
# print('Conclusion : C = t')

# print("="*10, "4b", "="*10)
# print("p: An wake up late")
# print("q: the traffic is flowing smooth")
# print("~q: the traffic is heavy")
# print("r: school day")
# print("s: An have go to school")
# print("v: An is late for school")

# print('Given:')
# print('P ="An wake up late"; Q ="The traffic is flowing smooth"')
# print('S1="The traffic is always heavy on school day"')
# print('S2="If An wake up late, he will be late for school on school day"')
# print('S3="An only have to go to school on school day"')
# print('S4="If An don’t have to go to school, An can’t be late for school"')
# print('Conclusion : C ="An is late for school"')

# print('-'*20)
# print('P = p')
# print('Q = q')
# print('S1= ')
# print('S2= p -> (v ^ r)')
# print('S3= ')
# print('S4= ~s -> ~v')
# print('Conclusion : C = ~v')


# # ex5


# function from lab2
import math


def lImplies(p, q):
    if p:
        return q
    return True


def lAnd(p, q):
    return p and q


def lOr(p, q):
    return p or q


def lXor(p, q):
    return p != q


def lNot(p):
    return not(p)


def lEquivalent(p, q):
    return p == q
# end


# ex6
A = [
    [2, 0, 5, 0, 3, 0],
    [3, 0, 0, 0, 0, 0],
    [0, 6, 2, 0, 5, 0],
    [3, 0, 9, 0, 25, 0],
    [0, 0, 2, 4, 5, 0],
    [0, 0, 0, 0, 0, 5]
]
row = len(A)
col = len(A[0])


def isOdd(a):
    return a % 2 == 1


def isPrime(a):
    if (a <= 1):
        return False
    for i in range(2, a):
        if (a % i == 0):
            return False
    return True


def isSquare(a):
    return math.pow(int(math.sqrt(a)), 2) == a


def isGreater(a, b):
    return a > b


def isEqual(a, b):
    return a == b


def isAbove(a, b):
    pass


def isLeftOf(a, b):
    pass


def ex6a(A):
    for i in range(row):
        for j in range(col):
            if (A[i][j])


for i in range(row):
    for j in range(col):
        print(A[i][j], end="\t")
    print("")
