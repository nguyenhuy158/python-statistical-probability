def numberZeroDigits(n):		
	count = 0 # count zero
	produc = 1 # produc = n!

	for i in range(1, n+1):
		produc *= i # n! = 1.2.3..

		while not produc % 10: # n! = 120 -> 12	
			count += 1
			produc //= 10

		produc %= 100 # n! = 3628800 -> 88

	print(f"number zero of {n}! is {count}")
	# test
	countT = 0
	produc = 1
	for i in range(1, n+1):
		produc *= i

	while not produc % 10:
		countT += 1
		produc //= 10
		
	return countT


n = int(input('enter n!: '))
print(numberZeroDigits(n))

