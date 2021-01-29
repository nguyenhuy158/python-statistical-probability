def pagesNumbering(n):
    # 123 -> 3
    count = len(str(n))
    # compute
    # slcs: so luong chu so
    # 1 - 9 = 10^1 - 10^0 = 9 * 1(slcs)
    # 99 - 10 = 10^2 - 10^1 = 90 * 2(slcs)
    ans = 0
    for i in range(1, count):
        ans += (pow(10, i) - pow(10, i-1)) * i

    for i in range(pow(10, count-1), n+1):
        ans += count

    return ans

n = int(input())

print(pagesNumbering(n))
