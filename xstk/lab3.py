from fractions import Fraction
def P(event, space):
  return Fraction(len(event & space), len(space))

# S = {'BB', 'BG', 'GB', 'GG'}

# B = {s for s in S if 'B' in s}
# A_B = {s for s in B if s.count('B') == 2}

# # A is the event that Mr. Smith’s two children to be boys.
# # B is the event that at least one of Mr. Smith’s children is a boy.

# P_B = P(B, S)
# P_A_B = P(A_B, S)

# P_A_with_B = P_A_B / P_B

# print(P_A_with_B)

# exercises 1. Know that a house has 3 cats.

import itertools

# a
print("=1A="*10)
S = {''.join(s) for s in list(itertools.product(['M', 'F'], repeat=3))}
print("len S =", len(S), S)

# b
print("=1B="*10)
num_S = len(S)
print("num_S =", num_S)

# (c) Let B is the event that there is at least one female cat. List the elements of B and save to variable B.
print("=1C="*10)
B = {s for s in S if 'F' in s}
print("len B =", len(B), B)

# (d) Let A is the event that all three cats are female. List elements of event A and save to variable A.
print("=1D="*10)
A = {s for s in S if s.count('F') == 3}
A_B = {s for s in B if s.count('F') == 3}
print("len A =", len(A), A)
print("len A_B =", len(A_B), A_B)

# (e) Calculate the probability that all three cats are female under the condition that at least one cat is a female.
print("=1E="*10)
P_A = P(A, S)
P_B = P(B, S)
P_A_B = P(A_B, S)
print("P_A =", P_A)
print("P_B =", P_B)
print("P_A_B =", P_A_B)

P_A_with_B = P_A_B / P_B
print("P_A_with_B =", P_A_with_B)


print("\n"*10)


S = [('Thanh', 'Nu'), ('Hồng', 'Nữ'), ('Thương', 'Nữ'), ('Đào', 'Nữ'), 
     ('My', 'Nữ'), ('Yến', 'Nữ'), ('Hạnh', 'Nữ'), ('My', 'Nữ'), ('Vy', 'Nữ'), 
     ('Tiên', 'Nữ'), ('Thanh', 'Nam'), ('Thanh', 'Nam'), ('Bình', 'Nam'), 
     ('Nhật', 'Nam'), ('Hào', 'Nam'), ('Đạt', 'Nam'), ('Minh', 'Nam')]

# (a) List elements of event A and store in variable A.
# “student’s name is Thanh”,
print("=2A="*10)
A = [s for s in S if s[0] == 'Thanh']
print("len A =", len(A), A)

# (b) List the elements of event B and save to variable B.
# “is a female”.
print("=2B="*10)
B = [s for s in S if s[1] == 'Nữ']
print("len B =", len(B), B)


# (c) List the elements of the event A ∩ B and store it in the variable A_B.
print("=2C="*10)
A_B = [s for s in B if s[0] == 'Thanh']
print("len A_B =", len(A_B), A_B)


# (d) Calculate the probability of the three above events and stored in three variables P_A, P_B, P_A_B respectively.
print("=2D="*10)
P_A =   Fraction(len(A) , len(S))
P_B =   Fraction(len(B) , len(S))
P_A_B = Fraction(len(A_B) , len(S))
print("P_A =", P_A)
print("P_B =", P_B)
print("P_A_B =", P_A_B)


# (e) Calculate the probability that the called student’s name is “Thanh” under the condition that “this is a female”.
print("=2E="*10)
P_A_with_B = P_A_B / P_B
print("P_A_with_B =", P_A_with_B)


print("\n"*10)


ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
suits = {'♡', '♢', '♣', '♠'}

# a
print("=3A="*10)
cards = list(itertools.product(ranks , suits))
print("len cards =", len(cards), cards)
# b
print("=3B="*10)
B = list(itertools.combinations(cards, 3))
print("len B =", len(B))
# (c) A1 is the event that 3 cards include 1 or 2 K. Save the elements of event A1 to variable A1.
print("=3C="*10)
A1 = [s for s in B if ''.join(str(i) for i in s).count('K') == 1 or  ''.join(str(i) for i in s).count('K') == 2]
print("len A1 =", len(A1))

# (d) A2 is the event that 3 cards include at least 1 K. Save the elements of event A2 into variable A2.
print("=3D="*10)
A2 = [s for s in B if ''.join(str(i) for i in s).count('K') >= 1]
print("len A2 =", len(A2))

# (e) Calculate the probability of two events A1 and A2. (Hint: P(A1) = 0.2172; P(A2) = 0.2174)
print("=3E="*10)
P_A1 = P(set(A1), set(B))
P_A2 = P(set(A2), set(B))
print("P_A1 =", P_A1)
print("P_A2 =", P_A2)
