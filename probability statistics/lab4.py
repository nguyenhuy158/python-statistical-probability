
# ex1
# Rolling two fair dice. Write a function to calculate the practical probability of the following evens with n times of experiments.
import itertools
import random

print("=1A="*10)
# a/ Both dice are the same
# a/ Hai viên giống nhau
def solve1A(times):
  count = 0
  for i in range(times):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    if dice1 == dice2:
      count += 1
  return count / times

# b/ Both dice are different
# b/ Hai viên khác nhau
def solve1B(times):
  # count = 0
  # for i in range(times):
  #   dice1 = random.randint(1, 6)
  #   dice2 = random.randint(1, 6)
  #   if dice1 != dice2:
  #     count += 1
  # return count / times
  return 1 - solve1A(times)

# c/ Both dice are even
# c/ Hai viên cùng chẵn
def solve1C(times):
  count = 0
  for i in range(times):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    if dice1 % 2 + dice2 % 2 == 0:
      count += 1
  return count / times

# d/ Both dice are odd
# d/ Hai viên cùng lẻ
def solve1D(times):
  count = 0
  for i in range(times):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    if dice1 % 2 + dice2 % 2 == 2:
      count += 1
  return count / times

# e/ One die is even and the other is odd
# e/ Một viên chẵn và một viên lẻ
def solve1E(times):
  count = 0
  for i in range(times):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    if (dice1 % 2 + dice2 % 2) == 1:
      count += 1
  return count / times

# f/ Both dice are 6
# f/ Hai viên cùng ra 6
def solve1F(times):
  count = 0
  for i in range(times):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    if dice1 == dice2 and dice1 == 6:
      count += 1
  return count / times

# g/ Summation of both dice are greater than 10.
# g/ Hai viên có tổng số nút lớn hơn 10
def solve1G(times):
  count = 0
  for i in range(times):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    if dice1 + dice2 > 10:
      count += 1
  return count / times


times = 100000
print("1a:", solve1A(times))
print("1b:", solve1B(times))
print("1c:", solve1C(times))
print("1d:", solve1D(times))
print("1e:", solve1E(times))
print("1f:", solve1F(times))
print("1g:", solve1G(times))



print("=2A="*10)

# ex2
# Given a close urn with 2 blue balls, 3 red balls and 5 white balls. 
# Choose 3 balls from the urn. 
# Write an function to calculate the practical probability of the following  evens with n times of experiments.
# Cho một bình kín có 2 bi xanh, 3 bi đỏ và 5 bi trắng. 
# Giả sử bốc 3 viên bi từ trong bình. 
# Hãy viết hàm tính xác suất thực nghiệm với n lần thí nghiệm của các sự kiện sau:


# a/ All 3 balls are same color.
# a/ Cả ba viên cùng màu
# (3C3 + 5C3) / 10C3
def solve2A(times):
  count = 0
  for i in range(times):
    sample = ''.join(random.sample(U2, k=3))
    if sample.count('W') == 3 or sample.count('R') == 3:
      # print(sample)
      count += 1
  return count / times

# b/ All 3 balls are different colors.
# b/ Cả ba viên đều khác màu nhau
# (2C1 * 3C1 * 5C1) / 10C3
def solve2B(times):
  count = 0
  for i in range(times):
    sample = ''.join(random.sample(U2, k=3))
    if sample.count('W') == 1 and sample.count('R') == 1 and sample.count('B') == 1:
      # print(sample)
      count += 1
  return count / times

# c/ Only 2 balls are same color.
# c/ Chỉ có hai viên cùng màu
# (2C1 * 8C1 + 3C2*7C1 + 5C2*5C1) / 10C3
def solve2C(times):
  count = 0
  for i in range(times):
    sample = ''.join(random.sample(U2, k=3))
    if sample.count('W') == 2 or sample.count('R') == 2 or sample.count('B') == 2:
      # print(sample)
      count += 1
  return count / times
  
# d/ There are 2 red balls and 1 white ball.
# d/ Được 2 bi đỏ và 1 bi trắng
#  (3C2*5C1) / 10C3
def solve2D(times):
  count = 0
  for i in range(times):
    sample = ''.join(random.sample(U2, k=3))
    if sample.count('R') == 2 and sample.count('W') == 1:
      # print(sample)
      count += 1
  return count / times

# e/ List all the cases that all 3 balls are white.
# e/ Liệt kê các trường hợp 3 bi đều màu trắng.
# (5C3) / 10C3
def solve2E(times):
  count = 0
  for i in range(times):
    sample = ''.join(random.sample(U2, k=3))
    if sample.count('W') == 3:
      # print(sample)
      count += 1
  return count / times

U2 = list(''.join(s) for s in itertools.product('B', '12')) + list(''.join(s) for s in itertools.product('R', '123')) + list(''.join(s) for s in itertools.product('W', '12345')) 
print(U2)

times = 1000
print("2a:", solve2A(times))
print("2b:", solve2B(times))
# print(list(itertools.combinations(U2, 3)))
# print([s for s in list(itertools.combinations(U2, 3)) if ''.join(s).count('W') == 1 and ''.join(s).count('R') == 1 and ''.join(s).count('B') == 1])
# print(len([s for s in list(itertools.combinations(U2, 3)) if ''.join(s).count('W') == 1 and ''.join(s).count('R') == 1 and ''.join(s).count('B') == 1]                            ))
print("2c:", solve2C(times))
print("2d:", solve2D(times))
print("2e:", solve2E(times))

# ex3
# Drawing 4 cards from a deck of 52 cards. Write a function to compute the practical
# probabitity of the following evens with n times of experiments.
print("=3A="*10)

# Giả sử làm thí nghiệm rút 4 là bài từ bộ bài 52 lá, 
# hãy viết hàm tính xác suất thực nghiệm với n lần thí của các sự kiện sau:

# a/ All 4 cards are from the same suit.
# a/ Bốn lá cùng chất
# (13C4*4) / 52C4 =
def solve3A(times):
  count = 0
  for i in range(times):
    sample = ''.join(random.sample(desk3, k=4))
    if sample.count('♡') == 4 or  sample.count('♢') == 4 or sample.count('♣') == 4 or sample.count('♠') == 4:
      # print(sample)
      count += 1
  return count / times

# b/ All 4 cards are differents suits. 
# b/ Bốn lá đôi một khác chất
# (13C1*13C1*13C1*13C1) / 52C4
def solve3B(times):
  count = 0
  for i in range(times):
    sample = ''.join(random.sample(desk3, k=4))
    if sample.count('♡') == 1 and sample.count('♢') == 1 and sample.count('♣') == 1 and sample.count('♠') == 1:
      # print(sample)
      count += 1
  return count / times

# c/ All 4 cards are same color.
# c/ Bốn lá cùng màu
# (26C4+26C4) / 52C4
def solve3C(times):
  count = 0
  for i in range(times):
    sample = ''.join(random.sample(desk3, k=4))
    if (sample.count('♡') + sample.count('♢')) == 4 or (sample.count('♣') + sample.count('♠')) == 4:
      # print(sample)
      count += 1
  return count / times

# d/ All 4 cards are same value.
# d/ Bốn lá cùng chỉ số (tứ quý) 
# (4C4 * 13) / 52
def solve3D(times):
  count = 0
  for i in range(times):
    sample = ''.join(random.sample(desk3, k=4))
    if sample[0] == sample[2] and sample[2] == sample[4] and sample[4] == sample[6]:
      # print(sample)
      count += 1
  return count / times

# e/ All 4 cards are numbers.
# e/ Bốn lá cùng là loại số
# 40C4 / 52C4 = 0.338278
def solve3E(times):
  count = 0
  for i in range(times):
    sample = ''.join(random.sample(desk3, k=4))
    if sample[0] not in ('J', 'Q', 'K') and sample[2] not in ('J', 'Q', 'K') and sample[4] not in ('J', 'Q', 'K') and sample[6] not in ('J', 'Q', 'K'):
      # print(sample)
      count += 1
  return count / times

# f/ All 4 cards are faces.
# f/ Bốn lá cùng là loại hình
# 12C4 / 52C4 = 0.0018284237
def solve3F(times):
  count = 0
  for i in range(times):
    sample = ''.join(random.sample(desk3, k=4))
    # print(sample[0], sample[2], sample[4], sample[6])
    if sample[0] in ('J', 'Q', 'K') and sample[2] in ('J', 'Q', 'K') and sample[4] in ('J', 'Q', 'K') and sample[6] in ('J', 'Q', 'K'):
      # print(sample)
      count += 1
  return count / times


desk3 = list(itertools.product({'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'J', 'Q', 'K'}, {'♡', '♢', '♣', '♠'}))
desk3 = [''.join(s) for s in desk3]
print(desk3)
print(len(desk3))


times = 1000000
print("3a:", solve3A(times))
print("3b:", solve3B(times))
print("3c:", solve3C(times))
print("3d:", solve3D(times))
print("3e:", solve3E(times))
print("3f:", solve3F(times))

# ex4
# Given a close urn that contains 9 balls: 2 white balls, 3 blue balls, and 4 red balls.
# Knowing that the probabilities of choosing each ball are equals.
# Cho một bình kín có 9 quả banh: 2 quả màu trắng, 3 quả xanh dương và 4 quả màu đỏ. 
# Biết rằng mỗi quả có xác suất được chọn như nhau.
print("=4A="*10)


# a/ Create a set to save all the balls. Call the 2 white balls &#39;W1&#39; and &#39;W2&#39;.
# Similiarly, 3 blue balls are &#39;B1&#39;, &#39;B2&#39;, &#39;B3&#39; and 4 red balls are &#39;R1&#39;, &#39;R2&#39;, &#39;R3&#39;. Save
# them in a variable named URN.
# a/ Tạo một tập hợp để lưu các quả banh. Ký hiệu 2 quả banh màu trắng là &#39;W1&#39;, &#39;W2&#39;. Tương tự cho 3 quả xanh
# dương là &#39;B1&#39;, &#39;B2&#39;, &#39;B3&#39; và 4 quả màu đỏ là &#39;R1&#39;, &#39;R2&#39;, &#39;R3&#39;. &#39;R4&#39;. Lưu vào biến URN.
URN = list(''.join(s) for s in itertools.product('W', '12')) + list(''.join(s) for s in itertools.product('B', '123')) + list(''.join(s) for s in itertools.product('R', '1234')) 
print('URN', URN)

# b/ Find the subset of 3 balls from set URN (regardless the order). 
# Save your result in variable U3.
# b/ Tìm tập con gồm 3 quả banh từ tập hợp URN trên (không phân biệt thứ tự). 
# Lưu kết quả của tập con đó vào biến U3.
U3 = list(itertools.combinations(URN, 3))
print('U3', U3)
# print('U3', len(U3))


# c/ List all the cases that 3 balls in question (b) including 1 white ball, 1 blue ball, and 1 red ball. 
# Save your result in variable white1blue1red1.
# c/ Liệt kê các trường hợp 3 quả banh được chọn ở câu (b) có một quả banh màu trắng, 
# một quả banh màu xanh dương và một quả banh màu đỏ, kết quả lưu vào biến white1blue1red1.
white1blue1red1 = [s for s in U3 if ''.join(s).count('W') == 1 and ''.join(s).count('B') == 1 and ''.join(s).count('R') == 1]
print('white1blue1red1', white1blue1red1)
# print(len(white1blue1red1))

# d/ Find the probability that randomly choose 3 balls including 1 white ball, 1 blue ball, and 1 red ball.
#  Save your result in variable P.
# d/ Tính xác suất chọn ngẫu nhiên 3 quả banh trong đó có một quả banh màu trắng, một quả banh màu xanh dương và một quả banh màu đỏ,
#  kết quả lưu vào biến P.
P = len(white1blue1red1) / len(U3)
print('P=', P)

# ex5
# Given an deck of 52 cards. Randomly choose 5 cards. 
# Find the probability that these 5 cards make a straight.
# Cho bộ bài tây 52 lá. Rút ngẫu nhiên 5 lá bài. Tính xác suất 5 lá bài tạo thành một sảnh.
print("=5A="*10)

desk5 = list(itertools.product({'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'}, {'♡', '♢', '♣', '♠'}))
desk5 = [''.join(s) for s in desk5]
print('desk5', desk5)
print(len(desk5))

def checkStraight(fiveCards):
  dictConvert = {
    '1': 14,
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
    'K': 13
  }
  sorted = [dictConvert[s[0]] for s in fiveCards]
  sorted.sort()

  for i in range(4):
    if sorted[i] - sorted[i+1] != -1:
      return False

  return True

# a/ Theorical probability
# a/ Xác suất lý thuyết.
# choose5Cards = list(itertools.permutations(desk5, 5))
choose5Cards = list(itertools.combinations(desk5, 5))
# print(choose5Cards)
count = 0
for i in range(len(choose5Cards)):
  if checkStraight(choose5Cards[i]):
    # += 5! = 120
    count += 120
  # print(choose5Cards[i])
P = count / (len(choose5Cards) * 120)
# print('P=', P, count, (len(choose5Cards) * 120))
print('P lý thuyết =', P)

# b/ Practical probability
# b/ Xác suất thực nghiệm
times = 1000000
count = 0
for i in range(times):
  sample = ''.join(random.sample(desk5, k=5))
  # print(sample[0], sample[2], sample[4], sample[6])
  if checkStraight(choose5Cards[i]):
    # print(sample)
    count += 1

P = count / times
print('P thực nghiệm =', P)

# ex6
print("=6A="*10)
# Let set E = {0,1,2,3,4,5}
# Cho tập hợp E = {0,1,2,3,4,5}
E = {0,1,2,3,4,5}

# a/ List all 3-digits numbers in which every digit is an element in E.
# a/ Liệt kê các số có 3 chữ số, các chữ số được tạo từ các phần tử trong tập hợp E.
# print(list(itertools.product(E, repeat=3)))
# 5*6*6 = 180
threeDigitsNum = [int(''.join(str(s) for s in num)) for num in list(itertools.product(E, repeat=3)) if int(''.join(str(s) for s in num)) >= 100]
# threeDigitsNum = []
print('threeDigitsNum', threeDigitsNum)
print(len(threeDigitsNum))

# b/ List all 4-digits numbers in which all digits are pairwise different and every digit is an element in E.
# b/ Liệt kê các số có 4 chữ số (đôi một khác nhau), các chữ số được tạo từ các phần tử trong tập hợp E.
# 6*5*4*3 - 1*5*4*3 = 360 - 60 = 300 (ABCD - 0EFG)
fourDigitsNum = [int(''.join(str(s) for s in num)) for num in list(itertools.permutations(E, 4)) if int(''.join(str(s) for s in num)) >= 1000]
print('fourDigitsNum', fourDigitsNum)
print(len(fourDigitsNum))

