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
# print(len(U6))
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
colors = 3
print("cac truong hop co 3 mau rieng biet")
for i in U3:
    currentColor = set()
    for j in i:
        currentColor.add(j[0])
    if len(currentColor) == 3:
        print(*i)
# c
print("cac truong hop co ba thu 1 mau trang(W) va qua thu 2 mau do(R)")
for i in U3:
    if i[0][0] == 'W' and i[1][0] == 'R':
        print(*i)

# === bai3
# (M)athematics (P)hysics (C)hemistry (L)anguage
print("== bai 3 == \t" * 5)

shelf_3 = cross('M', '1234') | cross(
    'P', '123') | cross('C', '12') | cross('L', '1')

all_cases = list(itertools.permutations(shelf_3))
# print(len(all_cases))

correct = [''.join(a) for a in list(
    itertools.permutations(('MMMM', 'PPP', 'CC', 'L')))]
save = []
print(correct)
count = 0
for i in all_cases:
    s = ''.join([j[0] for j in i])

    if s in correct:
        save.append(i)
        count += 1

print("so truong hop thoa man de cau 3 la: ", count)
for s in save:
    print(s)

# === bai 4
print("== bai 4 == \t" * 5)
# (F)emale (M)ale
# people_4 = cross('F', '123456789') | cross('M', '123456')

choose_2_F = list(itertools.combinations(cross('F', '123456789'), 2))
choose_3_M = list(itertools.combinations(cross('M', '123456'), 3))

print("so luong truong hop thoa man la:", len(cross(choose_3_M, choose_2_F)))
print("cu the la: ")
for i in cross(choose_3_M, choose_2_F):
    print(i)

# === bai 5
# A234567890JQK
# 10 == 0 (con 10 quy ra la so 0)
print("== bai 5 == \t" * 5)
desk_order = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '0': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    }

desk_5 = cross('♠', 'A234567890JQK') | cross('♣', 'A234567890JQK') | cross('♦', 'A234567890JQK') | cross('♥', 'A234567890JQK')
# print(desk_5)
# print(len(desk_5))
def my_desk(e):
    return desk_order[e[-1]]
def three_of_a_kind(temp):
    if (desk_order[temp[0][-1]] + desk_order[temp[1][-1]] + desk_order[temp[2][-1]]) / 3 == desk_order[temp[0][-1]] and desk_order[temp[3][-1]] != desk_order[temp[4][-1]] and  desk_order[temp[3][-1]] != desk_order[temp[0][-1]]:
        return True
    if (desk_order[temp[1][-1]] + desk_order[temp[2][-1]] + desk_order[temp[3][-1]]) / 3 == desk_order[temp[1][-1]] and desk_order[temp[4][-1]] != desk_order[temp[0][-1]] and  desk_order[temp[4][-1]] != desk_order[temp[1][-1]]:
        return True
    if (desk_order[temp[2][-1]] + desk_order[temp[3][-1]] + desk_order[temp[4][-1]]) / 3 == desk_order[temp[2][-1]] and desk_order[temp[0][-1]] != desk_order[temp[1][-1]] and  desk_order[temp[1][-1]] != desk_order[temp[2][-1]]:
        return True
    
    return False
choose_5_card = list(itertools.combinations(desk_5, 5))
count = 0
print("liet ke bo three of a kind")
for i in choose_5_card:

    temp = list(i)
    temp.sort(key=my_desk)
    if three_of_a_kind(temp):
        print(temp)
    count += 1
    # if count == 100:
    #     break

print("so truong hop cua three of a kind la: ", count)
