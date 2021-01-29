def digitsProduct(n):
    ans = 0
    for i in range(9, 1, -1):
        while not n % i:
            ans = ans * 10 + i
            n //= i
    
    fake = ans
    ans = 0
    while fake > 0:
        ans = ans * 10 + fake % 10
        fake //= 10

    if ans:
        return ans 
    return -1

n = int(input('enter: '))

print(digitsProduct(n))