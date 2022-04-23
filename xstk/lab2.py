import random
import itertools
from itertools import product
from fractions import Fraction

N = 100000

# === 1 ====
def simualtor_dice1(n):
  count = 0
  for time in range(n):
    dieOne = random.randint(1, 6)
    dieTwo = random.randint(1, 6)
    if dieOne % 2 == dieTwo % 2 == 0:
      count += 1
  return count / n;

# 9/36 = 0.25
print("1", simualtor_dice1(N))

# === 2 ====
def simualtor_dice2(n):
  count = 0
  for time in range(n):
    dieOne = random.randint(1, 6)
    dieTwo = random.randint(1, 6)
    if (dieOne % 2 + dieTwo % 2) == 1:
      count += 1
  return count / n;

# 0.5 
print("2", simualtor_dice2(N))


# === 3 ====
def simualtor_dice3(n):
  count = 0
  for time in range(n):
    dieOne = random.randint(1, 6)
    dieTwo = random.randint(1, 6)
    if dieOne == dieTwo:
      count += 1
  return count / n;

# 6/36 = 0.16666666666
print("3", simualtor_dice3(N))


# === 4 ====
def simualtor_dice4(n):
  count = 0
  for time in range(n):
    dieOne = random.randint(1, 6)
    dieTwo = random.randint(1, 6)
    if (dieOne == 1 and dieTwo == 6) or (dieOne == 6 and dieTwo == 1):
      count += 1
  return count / n;

# 2/36 = 0.05555555555
print("4", simualtor_dice4(N))


# === 5 ====
def simualtor_dice5(n):
  count = 0
  for time in range(n):
    dieOne = random.randint(1, 6)
    dieTwo = random.randint(1, 6)
    if (dieOne + dieTwo > 6):
      count += 1
  return count / n;

# 21/36 = 0.58333333333
print("5", simualtor_dice5(N))


# === 6 ====
def simualtor_poker1(n):
  Ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
  Suits = {'♡', '♢', '♣', '♠'}
  Cards = list(product(Ranks , Suits))
  
  count = 0
  for time in range(n):
      fiveCards = set()
      while len(fiveCards) < 5:
        tempIndex = random.randint(0, 51)
        fiveCards.add(tempIndex)

      tempCards = ''.join([Cards[i][1] for i in list(fiveCards)])
      # print(tempCards)
      if tempCards == '♡♡♡♡♡':
        count += 1

  return count / n

print("6", simualtor_poker1(N))

# === 7 ====
def simualtor_poker2(n):
  Ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
  Suits = {'♡', '♢', '♣', '♠'}
  Cards = list(product(Ranks , Suits))

  count = 0
  for time in range(n):
    fiveCards = set()
    while len(fiveCards) < 4:
      tempIndex = random.randint(0, 51)
      fiveCards.add(tempIndex)

    tempCards = ''.join([Cards[i][1] for i in list(fiveCards)])

    pattern = [''.join(i) for i in list(itertools.permutations(['♡', '♢', '♣', '♠']))]

    if tempCards in pattern:
      count += 1

  return count / n

# 0.07
print("7", simualtor_poker2(N))

# === 8 ====
def P(event, space):
  return Fraction(len(event & space), len(space))

def cross(A, B):
  return {a + b for a in A for b in B}

urn = cross('W', '12345678') | cross('B', '123456') | cross('R', '123456789')
# print(urn)

def combos(items, n):
  return {' '.join(combo) for combo in itertools.combinations(items, n)}

U8 = combos(urn, 6)
w2b2r2 = {s for s in U8 if s.count('R') == 2 and s.count('B') == 2 and s.count('W') == 2}
print('8', P(w2b2r2, U8))
