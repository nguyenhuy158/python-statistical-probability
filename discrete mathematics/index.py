def way(n, k):
    if k == 0 or k == n:
        return 1

    return way(n-1, k) + way(n-1, k-1)


print(way(10, 3))
