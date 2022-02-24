import itertools

# ===== code mau
E = {'a', 'b', 'c', 'd'}
k = 3

# permutations
permutations_k = list(itertools.permutations(E, k))
print('permutations: ')
print(len(permutations_k))
for i in permutations_k:
    print(i)

# combinations
combinations_k = list(itertools.combinations(E, k))
print('combinations: ')
print(len(combinations_k))
for i in combinations_k:
    print(i)

# urn
def cross(A, B):
    return {a + b for a in A for b in B}
urn = cross('W', '12345678') | cross('B', '123456') | cross('R', '123456789')
print(urn)


U6 = list(itertools.combinations(urn, 6))

# a
print(len(U6))
# b
# for i in U6:
#     print(i)
# c
# for i in U6:
#     if i[0][0] == 'R' and i[-1][0] == 'R':
#         print(i)

# ===== code exercises
# === bai 1
def arr2int(items):
     return int(''.join(str(item) for item in items))
 
print("== bai 1 == \t" * 5)
A = {1, 2, 3, 4, 5}
k = 3
num_3_digit = list(itertools.permutations(A, k))
num_3_digit = [arr2int(i) for i in num_3_digit]
num_length = len(num_3_digit)
print("co %d co 3 chu so" % num_length)
print("cac so do la:", num_3_digit)

# # === bài 2
print("== bai 2 == \t" * 5)
urn_2 = cross('W', '12345678') | cross('B', '123456') | cross('R', '123456789')
k = 3

# a
U3 = list(itertools.combinations(urn_2, k))
len_U3 = len(U3)
# b
# method 1
# hoanvi_color =  ['WBR', 'WRB', 'BWR', 'BRW', 'RBW', 'RWB']
# for i in U3:
#   if i[0][0] + i[1][0] + i[2][0] in hoanvi_color:
#     print(i)
# method 2
colors = 3
for i in U3:
    currentColor = set()
    for j in i:
        currentColor.add(j[0])
    if len(currentColor) == 3:
        print(i)
# c
count = 0
for i in U3:
    if i[0][0] == 'W' and i[1][0] == 'R':
        # print(i)
        count += 1
print(count)

# # bai3
# # (M)athematics (P)hysics (C)hemistry (L)anguage
# shelf_3 = cross('M', '1234') | cross(
#     'P', '123') | cross('C', '12') | cross('L', '1')

# all_cases = list(itertools.permutations(shelf_3))
# print(len(all_cases))

# correct = [''.join(a) for a in list(
#     itertools.permutations(('MMMM', 'PPP', 'CC', 'L')))]
# print(correct)
# count = 0
# for i in all_cases:
#     s = ''.join([j[0] for j in i])

#     if s in correct:
#         print(s)
#         # print(i)
#         count += 1

# print("count: ", count)
