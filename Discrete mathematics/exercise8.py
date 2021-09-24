def mSum(A, B):
	rowA = len(A)
	columnA = len(A[0])
	rowB = len(B)
	columnB = len(B[0])

	C = [[0 for i in range(columnB)] for j in range(rowA)]
	# print(C)
	if columnA == rowB:
		for row in range(rowA):
			for column in range(columnB):
				for k in range(columnA):
					C[row][column] += A[row][k] * B[k][column]
	else:
		# print("Matrix dimension error")
		return "Matrix dimension error"

	return C


print(mSum([[1], [2]], [[1], [2]]))
print(mSum([[1], [2], [3]], [[1], [2]]))

a = [[1, 2, 3],
	 [4, 5, 6]]

b = [[2, 2],
	 [2, 1],
	 [3, 3]]
print(mSum(a, b))
