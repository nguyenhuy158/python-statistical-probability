import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def draw(A1, vertexs):
    G1 = nx.from_numpy_matrix(A1)
    pos = nx.spring_layout(G1)
    nx.draw_networkx(
        G1, pos=pos, with_labels=True, labels={a: b for a, b in enumerate(vertexs)}
    )
    edge_labels = nx.draw_networkx_edge_labels(G1, font_size=6, pos=pos, label_pos=0.5)
    plt.axis("equal")
    plt.show()


def mPlus(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise Exception("len A not equal len B")

    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    # for i in range(len(A)):
    #     for j in range(len(A[0])):
    #         C[i][j] = A[i][j] + B[i][j]

    # return C


def mMinus(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise Exception("len A not equal len B")
    return [[A[j][i] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    # for i in range(len(A)):
    #     for j in range(len(A[0])):
    #         C[i][j] = A[i][j] + B[i][j]

    # return C


def mMultiply(A, B):
    if len(A[0]) != len(B):
        raise Exception("don't multiply matrix")

    C = [[0 for j in range(len(B[0]))] for i in range(len(A))]
    for i in range(len(C)):
        for j in range(len(C[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    return C


def mTranspose(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


def toLoE(A):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mapAlphabet = {i: alphabet[i] for i in range(len(alphabet))}
    edges = []
    for i in range(len(A)):
        for j in range(i + 1, len(A[0])):
            if A[i][j] != 0:
                edges.append((mapAlphabet[i], mapAlphabet[j], A[i][j]))

    return edges


if __name__ == "__main__":
    # A1 = np.array([[0, 3, 5, 2], [0, 0, 2, 0], [0, 0, 0, 3], [0, 0, 0, 0]])
    # A1 = np.array([[0, 1, 1], [1, 0, 0], [1, 0, 0]])
    # draw(A1)

    A = [[1, 2], [2, 3]]
    B = [[1, 2], [2, 3]]
    print(mPlus(A, B))
    # draw(np.array(mPlus(A, B)), "ab")

    A = [[2, 2], [2, 3]]
    B = [[1, 1], [3, 3]]
    # print(mMinus(A, B))
    # draw(np.array(mMinus(A, B)), "ab")

    A = [[2, 2], [2, 3]]
    B = [[1, 1, 1], [3, 3, 3]]
    # print(mMultiply(A, B))
    # draw(np.array(mMinus(A, B)), "ab")

    A = [[1, 2], [4, 3]]
    print(mTranspose(A))

    A = [[1, 2], [3, 4]]
    B = [[2, 0], [1, 2]]
    print(mMultiply(A, B))

    A = [[1, 4, 6, 10], [2, 7, 5, 3]]
    B = [[1, 4, 6], [2, 7, 5], [9, 0, 11], [3, 1, 0]]
    print(mMultiply(A, B))

    A = [
        [0, 0, 3, 0, 1],
        [0, 0, 5, 3, 0],
        [3, 5, 0, 1, 0],
        [0, 3, 1, 0, 2],
        [1, 0, 0, 2, 0],
    ]
    # draw(np.array(A), "abcde")

    A = [
        [0, 0, 0, 0, 1, 1],
        [0, 0, 5, 3, 0, 0],
        [0, 5, 0, 1, 0, 0],
        [0, 3, 1, 0, 2, 3],
        [1, 0, 0, 2, 0, 6],
        [1, 0, 0, 3, 6, 0],
    ]
    # draw(np.array(A), "abcdef")

    lines = [
        ("A", "C", 5),
        ("A", "D", 3),
        ("B", "C", 3),
        ("B", "D", 2),
        ("C", "D", 1),
        ("C", "E", 3),
        ("D", "E", 1),
        ("D", "F", 3),
        ("E", "F", 4),
    ]
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mapAlphabet = {alphabet[i]: i for i in range(len(alphabet))}
    n = len(alphabet)
    A = [[0 for j in range(n)] for i in range(n)]
    for line in lines:
        A[mapAlphabet[line[0]]][mapAlphabet[line[1]]] = 5
    # draw(np.array(A), "abcdef")

    lines = [
        ("A", "C", 2),
        ("A", "D", 3),
        ("A", "E", 3),
        ("B", "C", 3),
        ("B", "D", 2),
        ("C", "D", 2),
        ("C", "E", 8),
        ("C", "F", 6),
        ("D", "F", 5),
        ("E", "F", 3),
    ]
    for line in lines:
        A[mapAlphabet[line[0]]][mapAlphabet[line[1]]] = 5
    # draw(np.array(A), "abcdef")

    print(toLoE(A))
