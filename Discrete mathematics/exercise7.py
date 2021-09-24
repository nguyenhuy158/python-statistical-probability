def mSum(A, B):
	rowA = len(A)
	columnA = len(A[0])
	rowB = len(B)
	columnB = len(B[0])
	# print(rowA == rowB)
	# print(columnA == columnB)
	C = [[0 for i in range(columnA)] for j in range(rowA)]
	# print(C)
	if rowA == rowB and columnA == columnB:
		for row in range(rowA):
			for column in range(columnA):
				C[row][column] = A[row][column] + B[row][column]
	else:
		# print("Matrix dimension error")
		return "Matrix dimension error"

	return C


print(mSum([[1], [2]], [[1], [2]]))
print(mSum([[1], [2], [3]], [[1], [2]]))

a = [[1, 2, 3],
	 [4, 5, 6]]

b = [[1, 1, 1],
	 [1, 1, 1]]
print(mSum(a, b))
