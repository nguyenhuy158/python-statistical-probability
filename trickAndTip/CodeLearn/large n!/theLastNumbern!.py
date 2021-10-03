n = int(input('enter n!: '))

produc = 1 # produc = n!
for i in range(1, n+1):
	produc *= i # n! = 1.2.3..

	while not produc % 10: # n! = 120 -> 12	
		produc //= 10

	produc %= 100 # n! = 3628800 -> 88

print(f"the last number of {n}! is {produc % 10}")
