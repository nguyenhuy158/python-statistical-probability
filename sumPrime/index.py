def primeSum(n):
    N = n + 1
    mark = [1] * N
    mark[0] = mark[1] = 0
    i = 2
    while i < N:
        if mark[i]:
            j = i
            while j + i < N:
                j += i
                mark[j] = 0
        i += 1
    print(mark)
    ans = 0
    for i in range(2, n + 1):
        if mark[i]:
            ans += i

    return ans % 22082018

    print(mark)


n = int(input())
print(primeSum(n))
