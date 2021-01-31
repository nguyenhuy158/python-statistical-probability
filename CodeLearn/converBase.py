def fromDecimal(b, n):
    ans = []
    while n != 0:
        ans.append(n % b)
        n //= b
    ans.reverse()
    return ''.join([str(x) for x in ans])


print(fromDecimal(2, 13))
