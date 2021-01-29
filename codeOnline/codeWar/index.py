n = int(input('enter: '))

i = 1
ans = 0
count = 0
while True:
    dk = True
    for i in range(9,1,-1):
        if not n % i:
            ans = ans * 10 + i
            n //= i
            dk = False
            count += 1
            break
    
    if dk:
        break

fake = ans
ans = 0
for i in range(count):
    ans = ans * 10 + fake % 10
    fake //= 10

print(ans, count)