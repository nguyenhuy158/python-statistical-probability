from collections import Counter


x = int(input().strip())
shoe = dict(Counter(input().split()))
sum = 0

print(type(shoe))
n = int(input().strip())
for i in range(n):
    key = input().split()
    size = int(key[0])
    price = int(key[1])

    try:
        if shoe[str(size)]:
            shoe[str(size)] -= 1
            sum += price
    except:
        pass

print(sum)

