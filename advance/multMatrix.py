a = [
    [1, 1, 1],
    [1, 2, 2]
]


b = [
    [10, 2],
    [10, 2],
    [10, 2]
]


def mul(a, b):
    result = [[0 for i in range(len(b[0]))] for i in range(len(a))]
    # print(result)
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(a[0])):
                # print(f"{i,k}, {k,j}")
                result[i][j] += (a[i][k] * b[k][j])
                # print(a[i][k], b[k][j])
    
    return result


for row in mul(a, b):
    print(row)
