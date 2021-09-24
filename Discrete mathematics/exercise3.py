def sumN(n=0):
	result = ''
	sum = 0
	if n > 0:
		for i in range(n):
			sum += i
			result += '{}+'.format(i)
		result += '{}={}'.format(n, sum + n)
	else:
		for i in range(0, n, -1):
			sum += i
			result += '{}+'.format(i) if i == 0 else '({})+'.format(i)
		result += '(-{})={}'.format(-n, sum + n)

	return result


print(sumN(2))
print(sumN(5))
print(sumN(-5))
