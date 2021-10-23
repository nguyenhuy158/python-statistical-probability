import itertools


# ex1
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


# ex2
def lLImplies(p, q):
    return [lImplies(p[i], q[i]) for i in range(len(p))]


def lLAnd(p, q):
    return [lAnd(p[i], q[i]) for i in range(len(p))]


def lLOr(p, q):
    return [lOr(p[i], q[i]) for i in range(len(p))]


def lLXor(p, q):
    return [lXor(p[i], q[i]) for i in range(len(p))]


def lLNot(p):
    return [lNot(p[i]) for i in range(len(p))]


def lLEquivalent(p, q):
    return [lEquivalent(p[i], q[i]) for i in range(len(p))]


def printTable(p, q, r):
    print("{} \t {} \t {}".format("p", "q", "r"))
    for i in range(len(r)):
        print("{} \t {} \t {}".format(p[i], q[i], r[i]))


# ex3.1
def pAndqImpliesr():
    print('p \t q \t r \t p^q \t p^q->r')
    for i in (list(itertools.product([False, True], repeat=3))):
        print(i[0], '\t', i[1], '\t', i[2], '\t', lAnd(
            i[0], i[1]), '\t', lImplies(lAnd(i[0], i[1]), i[2]))


# ex3.2
def rImpliespAndq():
    print('p \t q \t r \t p^q \t r -> p^q')
    for i in (list(itertools.product([False, True], repeat=3))):
        print(i[0], '\t', i[1], '\t', i[2], '\t', lAnd(
            i[0], i[1]), '\t', lImplies(i[2], lAnd(i[0], i[1])))


def isEquivalent(exp, equivalent):
    if equivalent:
        print(exp, 'equivalent')
    else:
        print(exp, 'inequivalent')


def exercises5():
    pass


def exercises6():
    pass


if __name__ == '__main__':
    # # ex1
    # p = True
    # q = False
    # print('Not ', lNot(p))
    # print('Or ', lOr(p, q))
    # print('And ', lAnd(p, q))
    # print('Xor ', lXor(p, q))
    # print('Equivalent ', lEquivalent(p, q))
    # print('Implies ', lImplies(p, q))

    # # ex2
    # P = [False, False, True, True]
    # Q = [False, True, False, True]
    # R = lLImplies(P, Q)
    # print('Truth table implies'.upper())
    # printTable(P, Q, R)
    # print('Truth table equivalent'.upper())
    # R = lLEquivalent(P, Q)
    # printTable(P, Q, R)
    # print('Truth table xor'.upper())
    # R = lLXor(P, Q)
    # printTable(P, Q, R)
    # print('Truth table not'.upper())
    # R = lLNot(P)
    # printTable(P, ['' for i in range(len(Q))], R)
    # print('Truth table and'.upper())
    # R = lLAnd(P, Q)
    # printTable(P, Q, R)
    # print('Truth table or'.upper())
    # R = lLOr(P, Q)
    # printTable(P, Q, R)

    # # ex3
    # pAndqImpliesr()
    # rImpliespAndq()

    # # ex4
    # # p∨q→p∧q→¬p∨¬q
    # print('1. p∨q→p∧q→¬p∨¬q')
    # print('p', '\t', 'q', '\t', 'p∨q', '\t', 'p∧q', '\t',
    #       '¬p∨¬q', '\t', 'p∨q→p∧q', '\t', 'p∨q→p∧q→¬p∨¬q')
    # for i in (list(itertools.product([False, True], repeat=2))):
    #     p = i[0]
    #     q = i[1]
    #     print(p, '\t', q, '\t', lOr(p, q), '\t', lAnd(p, q), '\t',
    #           lOr(lNot(p), lNot(q)), '\t', lImplies(lOr(p, q), lAnd(p, q)),
    #           '\t\t', lImplies(lImplies(lOr(p, q), lAnd(p, q)),
    #                            lOr(lNot(p), lNot(q))))
    # # ¬p∨(q∧r)→r
    # print('2. ¬p∨(q∧r)→r')
    # print('p', '\t', 'q', '\t', 'r', '\t', '¬p', '\t', 'q∧r', '\t',
    #       '¬p∨(q∧r)', '\t', '¬p∨(q∧r)→r')
    # for i in (list(itertools.product([False, True], repeat=3))):
    #     p = i[0]
    #     q = i[1]
    #     r = i[2]
    #     print(p, '\t', q, '\t', r, '\t', lNot(p), '\t', lAnd(q, r), '\t',
    #           lOr(lNot(p),  lAnd(q, r)), '\t', lImplies(lOr(lNot(p),  lAnd(q, r)), r))

    # # (p→q)∧(q→r)
    # print('3. (p→q)∧(q→r)')
    # print('p', '\t', 'q', '\t', 'r', '\t', 'p→q',
    #       '\t', 'q→r', '\t', '(p→q)∧(q→r)')
    # for i in (list(itertools.product([False, True], repeat=3))):
    #     p = i[0]
    #     q = i[1]
    #     r = i[2]
    #     print(p, '\t', q, '\t', r, '\t', lImplies(p, q), '\t', lImplies(q, r), '\t',
    #           lAnd(lImplies(p, q), lImplies(q, r)))

    # # (p∨(q∧r))↔((p∨q)∧(p∨r))
    # print('3. (p∨(q∧r))↔((p∨q)∧(p∨r))')
    # print('p', '\t', 'q', '\t', 'r', '\t', '(q∧r)',
    #       '\t', '(p∨(q∧r))', '\t', '(p∨q)', '\t', '(p∨r)', '\t', '((p∨q)∧(p∨r))',
    #       '\t', '(p∨(q∧r))↔((p∨q)∧(p∨r))')
    # for i in (list(itertools.product([False, True], repeat=3))):
    #     p = i[0]
    #     q = i[1]
    #     r = i[2]
    #     print(p, '\t', q, '\t', r, '\t', lAnd(q, r), '\t', lOr(p, lAnd(q, r)), '\t',
    #           lOr(p, q), '\t', lOr(p, r), '\t', lAnd(lOr(p, q), lOr(p, r)), '\t', lEquivalent(lOr(p, lAnd(q, r)),  lAnd(lOr(p, q), lOr(p, r))))

    # # p∨q→¬r∨t
    # print('4. p∨q→¬r∨t')
    # print('p', '\t', 'q', '\t', 'r', '\t', 'p∨q',
    #       '\t', '¬r∨t', '\t', 'p∨q→¬r∨t')
    # for i in (list(itertools.product([False, True], repeat=4))):
    #     p = i[0]
    #     q = i[1]
    #     r = i[2]
    #     t = i[3]
    #     print(p, '\t', q, '\t', r, '\t', t, '\t', lOr(p, q), '\t',
    #           lOr(lNot(r), t), '\t', lImplies(lOr(p, q), lOr(lNot(r), t)))

    # # p∨t→q→(r→t)
    # print('5. p∨t→q→(r→t)')
    # print('p', '\t', 'q', '\t', 'r', '\t', 't', '\t', 'p∨t→q→(r→t)')
    # for i in (list(itertools.product([False, True], repeat=4))):
    #     p = i[0]
    #     q = i[1]
    #     r = i[2]
    #     t = i[3]
    #     print(p, '\t', q, '\t', r, '\t', t, '\t', lImplies(lImplies(lOr(p, t), q), lImplies(
    #         r, t)))

    # # (p∨(q∧r))↔(((p∨q)∧(p∨r))∧(t∨¬t))
    # print('6. (p∨(q∧r))↔(((p∨q)∧(p∨r))∧(t∨¬t))')
    # print('p', '\t', 'q', '\t', 'r', '\t', 't', '\t', 'p∨t→q→(r→t)')
    # for i in (list(itertools.product([False, True], repeat=4))):
    #     p = i[0]
    #     q = i[1]
    #     r = i[2]
    #     t = i[3]
    #     left = lOr(p, lAnd(q, r))
    #     right = lAnd(lAnd(lOr(p, q), lOr(p, r)), lOr(t, lNot(t)))
    #     print(p, '\t', q, '\t', r, '\t', t, '\t', lEquivalent(left, right))

    # ex5

    equivalent = True
    for i in (list(itertools.product([False, True], repeat=2))):
        p = i[0]
        q = i[1]

        left = p
        right = lNot(lNot(p))

        if left != right:
            equivalent = False
            break

    isEquivalent('p≡¬(¬p) is', equivalent)

    # ¬(¬q∧p)∧(q∨p)≡q
    equivalent = True
    for i in (list(itertools.product([False, True], repeat=2))):
        p = i[0]
        q = i[1]

        left = lAnd(lNot(lAnd(lNot(q), p)), lOr(q, p))
        right = lNot(lNot(p))

        if left != right:
            equivalent = False
            break

    isEquivalent('¬(¬q∧p)∧(q∨p)≡q is', equivalent)

    # # ex6
    # # a
    # isInvalid = True
    # print("p\tq\tr\ts\tp → r\t¬p → q\tq → s\t¬r → s")
    # for i in (list(itertools.product([False, True], repeat=4))):
    #     p = i[0]
    #     q = i[1]
    #     r = i[2]
    #     s = i[3]

    #     p1 = lImplies(p, r)
    #     p2 = lImplies(lNot(p), q)
    #     p3 = lImplies(q, s)
    #     out = lImplies(lNot(r), s)
    #     if p1 and p2 and p3:
    #         print(p, '\t', q, '\t', r, '\t', s, '\t',
    #               p1, '\t', p2, '\t', p3, '\t', out)
    #         if out == False:
    #             isInvalid = False
    #             break

    # if isInvalid:
    #     print('VALID')
    # else:
    #     print('INVALID')

    # # b
    # isInvalid = True
    # print("p\tq\tr\ts\tt\tp → (q → r)\tp ∨ s\tt → q\t¬s\t¬r → ¬t")
    # for i in (list(itertools.product([False, True], repeat=5))):
    #     p = i[0]
    #     q = i[1]
    #     r = i[2]
    #     s = i[3]
    #     t = i[4]

    #     p1 = lImplies(p, lImplies(q, r))
    #     p2 = lOr(p, s)
    #     p3 = lImplies(t, q)
    #     p4 = not s
    #     out = lImplies(not r, not s)
    #     if p1 and p2 and p3:
    #         print(p, '\t', q, '\t', r, '\t', s, '\t', t, '\t',
    #               p1, '\t', p2, '\t', p3, '\t', out)
    #         if out == False:
    #             isInvalid = False
    #             break

    # if isInvalid:
    #     print('VALID')
    # else:
    #     print('INVALID')

    # # c
    # isInvalid = True
    # print("p\tq\tr\ts\tp → q\t¬r ∨ s\tp ∨ r\t¬q → s")
    # for i in (list(itertools.product([False, True], repeat=4))):
    #     p = i[0]
    #     q = i[1]
    #     r = i[2]
    #     s = i[3]

    #     p1 = lImplies(p, q)
    #     p2 = lOr(not r, s)
    #     p3 = lOr(p, r)
    #     out = lImplies(not q, s)
    #     if p1 and p2 and p3:
    #         print(p, '\t', q, "\t", r, "\t", s, '\t',
    #               p1, "\t", p2, "\t", p3, "\t", out)
    #         if out == False:
    #             isInvalid = False
    #             break

    # if isInvalid:
    #     print('VALID')
    # else:
    #     print('INVALID')

    # # d
    # isInvalid = True
    # print("p\tq\tr\ts\tp → r\tp → (q ∨ ¬r)\t¬q ∨ ¬s\ts")
    # for i in (list(itertools.product([False, True], repeat=4))):
    #     p = i[0]
    #     q = i[1]
    #     r = i[2]
    #     s = i[3]

    #     p1 = s
    #     p2 = lImplies(p, r)
    #     p3 = lImplies(p, lOr(q, not r))
    #     p4 = lOr(not q, not s)
    #     out = s
    #     if p1 and p2 and p3:
    #         print(p, '\t', q, "\t", r, "\t", s, '\t',
    #               p1, "\t", p2, "\t", p3, "\t", out)
    #         if out == False:
    #             isInvalid = False
    #             break

    # if isInvalid:
    #     print('VALID')
    # else:
    #     print('INVALID')
