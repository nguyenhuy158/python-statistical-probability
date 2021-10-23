# from 52000668 import formalConvert

formExist = 'Exist x in D such that P(x)'
formForAll = 'For all x in D, P(x)'
formExistPQ = 'Exist x in D such that P(x) -> Q(x)'
formForAllPQ = 'For all x in D, P(x) -> Q(x)'

# ex 1
print('-'*5, 'cau 1', '-'*5)
# For all fishes, they need water to survive.
print('\n- For all fishes, they need water to survive.')
D = 'fishes'
P = 'need water to survive.'
print("D is '{}'".format(D))
print("P is '{}'".format(P))
print("Formal form :", formForAll)

# Exist a person, who is left handed
print('\n- Exist a person, who is left handed')
D = 'people'
P = 'is left handed'
print("D is '{}'".format(D))
print("P is '{}'".format(P))
print("Formal form :", formExist)

# Exist an employee in the company, who is late to work everyday.
print('\n- Exist an employee in the company, who is late to work everyday.')
D = 'employees in the company'
P = 'is late to work everyday'
print("D is '{}'".format(D))
print("P is '{}'".format(P))
print("Formal form : ", formExist)

# For all fishes in this pond, they are Koi fish.
print('\n- For all fishes in this pond, they are Koi fish.')
D = 'fishes in this pond'
P = 'are Koi fish.'
print("D is '{}'".format(D))
print("P is '{}'".format(P))
print("Formal form :", formForAll)

# There is at least one creature in the ocean, it can live on land
print('\n- There is at least one creature in the ocean, it can live on land')
D = 'creatures in the ocean'
P = 'can live on land'
print("D is '{}'".format(D))
print("P is '{}'".format(P))
print("Formal form :", formExist)


# Every students in class A did not pass the test
print('\n- Every students in class A did not pass the test')
D = 'students in class A'
P = 'did not pass the test'
print("D is '{}'".format(D))
print("P is '{}'".format(P))
print("Formal form :", formForAll)


# ex2
# 1 ∃
# 2 ∀
preFix = {'For all': 2, 'Exist': 1,
          'There is at least one': 1, 'Every': 2, 'All': 2,
          'For every': 2}

irregularNouns = {
    'cactus': 'cacti',
    'child': 'children',
    'foot': 'feet',
    'goose': 'geese',
    'man': 'men',
    'mouse': 'mice',
    'person': 'people',
    'tooth': 'teeth',
    'woman': 'women'
}


def handlePreFix(s):
    for pre in preFix.keys():
        if s.startswith(pre):
            return s.find(pre) + len(pre) + 1

    return 0


# ham isExits tra ve true <=> ∃ va nguoc lai
def isExits(s):
    for pre, value in preFix.items():
        if s.startswith(pre):
            return value == 1


# doi danh tu dac biet neu co
# va them s vao sau neu co
def changeNoun(d):
    # [first word] d
    # d se la phan con lai
    firstWord = d[:len(d) if d.count(' ') == 0 else d.find(' ')]
    d = d[len(d) if d.count(' ') == 0 else d.find(' ') + 1:]
    if (firstWord in irregularNouns.keys()):
        return irregularNouns.get(firstWord) + d

    return firstWord + 's ' + d


def replaceAorAn(d):
    if d.startswith('a '):
        d = d[2:]
    if d.startswith('an '):
        d = d[3:]
    return d


def handleD(s):
    # get prefix
    d = s[handlePreFix(s): s.find(',')]

    # th1: ∃
    # th2: for eveyr ex4
    if(isExits(s) or (s.startswith('For every'))):
        # remove a/an if possible
        d = replaceAorAn(d)
        # change irregular nouns and add s
        d = changeNoun(d)

    return d


def handleP(s):
    # remove pre
    s = s[s.find(','):]
    # remove first space
    s = s[s.find(' ') + 1:]
    # remove N
    s = s[s.find(' ') + 1:]

    return s


def handleF(s):
    for entry in preFix.items():
        # 1 ∃
        if s.startswith(entry[0]) and entry[1] == 1:
            return formExist

        # 2 ∀
        if s.startswith(entry[0]) and entry[1] == 2:
            return formForAll


def formalConvert(s):
    D = handleD(s)
    P = handleP(s)
    F = handleF(s)
    return [D, P, F]


print('-'*5, 'cau 2', '-'*5)
s = 'For all fishes, they need water to survive'
print(formalConvert(s))
s = 'Exist a person, who is left handed'
print(formalConvert(s))
s = 'Exist an employee in the company, who is late to work everyday.'
print(formalConvert(s))
s = 'For all fishes in this pond, they are Koi fish.'
print(formalConvert(s))
s = 'There is at least one creature in the ocean, it can live on land'
print(formalConvert(s))
s = 'Every students in class A, did not pass the test'
print(formalConvert(s))
s = 'All primes, it is odd.'
print(formalConvert(s))
s = input("enter my sentence: ")
# print(s.capitalize())
print(formalConvert(s.capitalize()))

# ex3
# (a) For all people, if they are blond then they are westerners.
# (b) Exist a person, whose hair is black but is a westerner.
# (c) For all students, if they study correctly then they have high score.
# (d) For every mammal, if they live in the sea, they are either dolphins or whales.
# (e) For every bird, if they don't have wings and can swim then they are penguins.
# (f) Exist a bird, who have wing but can't fly.
print('-'*5, 'cau 3', '-'*5)

print("\n- For all people, if they are blond then they are westerners")
print("D is 'people'")
print("P is 'is blond'")
print("Q is 'is westerners'")
print("Formal form : ", formForAllPQ)

print("\n- Exist a person, whose hair is black but is a westerner")
print("D is 'people'")
print("P is 'hair is black'")
print("Q is 'is a westerner'")
print("Formal form : ", formExistPQ)

print("\n- For all students, if they study correctly then they have high score")
print("D is 'students'")
print("P is 'study correctly'")
print("Q is 'has high score'")
print("Formal form : ", formForAllPQ)

print("\n- For every mammal, if they live in the sea, they are either dolphins or whales")
print("D is 'mammals'")
print("P is 'lives in the sea'")
print("Q is 'is either dolphins or whales'")
print("Formal form : ", formForAllPQ)

print("\n- For every bird, if they don't have wings and can swim then they are penguins")
print("D is 'birds'")
print("P is 'don't have wings and can swim'")
print("Q is 'is penguins'")
print("Formal form : ", formForAllPQ)

print("\n- Exist a bird, who have wing but can't fly")
print("D is 'birds'")
print("P is 'has wing'")
print("Q is 'can't fly'")
print("Formal form : ", formExistPQ)


# ex4
tuLamMoc = {
    'who ': 'but ',
    'whose ': 'but ',
    'if ': 'then ',
}

pluralVerb = {
    'are': 'is',
    'have': 'has',
    'were': 'was',
}


# convert:  if ... ,
# to:       if ... then
def fixIfThen(s):
    return s.replace(', ', ' then ')


def handlePluralVerb(s):
    for verb in pluralVerb.items():
        # print(verb)
        if verb[0] in s:
            return s.replace(verb[0], verb[1])
    return s


def handlePluralNouse(s):
    verbs = {
        'fishes': 'fish',
        'students': 'student',
        'cries': 'cry',
        'flies': 'fly',
        'tries': 'try',
        'pushes': 'push',
        'catches': 'catch',
        'buzzes': 'buzz',
        'goes': 'go'
    }
    for verb in verbs.items():
        if (verb[0] in s):
            return s.replace(verb[0], verb[1])

    for verb in pluralVerb.items():
        if verb[1] in s:
            # print(s[s.find(verb[1]) + len(verb[1]) + 1:])
            # print(s[s.find(verb[1]) + len(verb[1]) + 1:][-1])
            # print(s[s.find(verb[1]) + len(verb[1]) + 1:][-1] == 's')
            if (s[s.find(verb[1]) + len(verb[1]) + 1:][-1] == 's'):
                return s[:-1]

    return s


def handleIfThen(P, Q):
    # print(P, Q)
    P = P[P.find(' ')+1:]
    Q = Q[Q.find(' ')+1:]
    return [P, Q]


def handlePQ(s):
    s = s[s.find(', ') + 2:]
    for formExample in tuLamMoc.items():
        s = fixIfThen(s)

        if (formExample[0] in s and formExample[1] in s):
            P = s[s.find(formExample[0]) + len(formExample[0]): s.find(formExample[1])]
            Q = s[s.find(formExample[1]) + len(formExample[1]):]

            if (formExample == ('if ', 'then ')):
                [P, Q] = handleIfThen(P, Q)
            return [P, Q]

    return ['', '']


def handleFPQ(s):
    for entry in preFix.items():
        # 1 ∃
        if s.startswith(entry[0]) and entry[1] == 1:
            return formExistPQ

        # 2 ∀
        if s.startswith(entry[0]) and entry[1] == 2:
            return formForAllPQ


def formalConvertPQ(s):
    D = handleD(s).strip()
    [P, Q] = handlePQ(s)
    F = handleFPQ(s)
    P = handlePluralVerb(P)
    Q = handlePluralVerb(Q)
    P = handlePluralNouse(P).strip()
    Q = handlePluralNouse(Q).strip()
    return [D, P, Q, F]


print('-'*5, 'cau 4', '-'*5)
print(formalConvertPQ("For all people, if they are blond then they are westerners"))
print(formalConvertPQ("Exist a person, whose hair is black but is a westerner"))
print(formalConvertPQ(
    "For all students, if they study correctly then they have high score"))
print(formalConvertPQ(
    "For every mammal, if they live in the sea, they are either dolphins or whales"))
print(formalConvertPQ(
    "For every bird, if they don't have wings and can swim then they are penguins"))
print(formalConvertPQ("Exist a bird, who have wing but can't fly"))


# ex5
def nega(s):
    [D, P, F] = formalConvert(s)
    noun = s[s.find(', ') + 2: s.find(P) - 1]
    if F == formForAll:
        return "Exist {} such that {} not {}".format(handlePluralNouse(D), noun, P)
    else:
        return "For all {}, {} not {}".format(handlePluralNouse(D), noun, P)
    return ''


print('-'*5, 'cau 5', '-'*5)
print('\n- For all fishes, they need water to survive.')
print(nega('For all fishes, they need water to survive.'))

print('\n- Exist a person, who is left handed')
print(nega('Exist a person, who is left handed'))

print('\n- Exist an employee in the company, who is late to work everyday.')
print(nega('Exist an employee in the company, who is late to work everyday.'))

print('\n- For all fishes in this pond, they are Koi fish.')
print(nega('For all fishes in this pond, they are Koi fish.'))

print('\n- There is at least one creature in the ocean, it can live on land')
print(nega('There is at least one creature in the ocean, it can live on land'))


print('\n- Every students in class A, did not pass the test')
print(nega('Every students in class A, did not pass the test'))


print('-'*5, 'cau 6', '-'*5)
#                   ∀x ∈ D, P(x)    →   Q(x)
# Negation:         ∃x ∈ D, P(x)    ∧   ¬Q(x)
# Contrapositive:   ∀X ∈ D, ¬Q(x)   →   ¬P(x)
# Converse:         ∀X ∈ D, Q(x)    →   P(x)
# Inverse:          ∀X ∈ D, ¬P(x)   →   ¬Q(x)

#                   ∃x ∈ D, P(x)    →   Q(x)
# Negation:         ∀x ∈ D, P(x)    ∧   ¬Q(x)
# Contrapositive:   ∃x ∈ D, ¬Q(x)   →   ¬P(x)
# Converse:         ∃x ∈ D, Q(x)    →   P(x)
# Inverse:          ∃x ∈ D, ¬P(x)   →   ¬Q(x)
print("0: For all planets, if they have human, they have life.")
print("Negation : There is a planet, it has human but doesn't have life")
print("Contrapositive : For all planets, if they don't have life then they don't have human")
print("Converse : For all planets, if they have life, they have human")
print("Invert : For all planets, if they don't have life, they don't have human")

print("a: For all people, if they are blond then they are westerners")
print("Negation : There is a person, it is blond but is not westerners")
print("Contrapositive : For all people, if they are not westerners then they are not blond")
print("Converse : For all people, if they are westerners then they are blond")
print("Invert : For all people, if they are not blond then they are not westerners")

print("b: Exist a person, whose hair is black but is a westerner")
print("Negation : For all people, whose hair is black but is not westerners")
print("Contrapositive : Exist a person, if they are not a westerner then they hair is not black")
print("Converse : Exist a person, if they is a westerner then they hair is black")
print("Invert : Exist a person, if they hair is not black, they is not a westerner")

print("c: For all students, if they study correctly then they have high score")
print("Negation : There is a student, it studies correctly but has not high score")
print("Contrapositive : For all students, if they have not high score then they don't study correctly")
print("Converse : For all students, if they have high score, they study correctly")
print("Invert : For all students, if they don't study correctly then they have not high score")

print("d: For every mammal, if they live in the sea, they are either dolphins or whales")
print("Negation : There is a mammal, it lives in the sea but is not not dolphins and not whales")
print("Contrapositive : For every mammal, if they are not either dolphins or whales then they don't live in the sea")
print("Converse : For every mammal, if they are either dolphins or whales, they live in the sea")
print("Invert : For every mammal, if they don't live in the sea, they are not dolphins and not whales")

print("e: For every bird, if they don't have wings and can swim then they are penguins")
print("Negation : There is a bird, it don't have wings and can swim but is not penguins")
print("Contrapositive : For every bird, if they are not penguins then they have wings or can not swim")
print("Converse : For every bird, if then they are penguins then they don't have wings and can swim")
print("Invert : For every bird, if they have wings or can not swim then they are not penguins")

print("f: Exist a bird, who have wing but can't fly")
print("Negation : For all birds, it have wing but can fly")
print("Contrapositive : Exist a bird, if they can fly then they have not wing")
print("Converse : Exist a bird, if they can't fly then they have wing")
print("Invert : Exist a bird, if they have not wing then can fly")
#                   ∃x ∈ D, P(x)    →   Q(x)
# Negation:         ∀x ∈ D, P(x)    ∧   ¬Q(x)
# Contrapositive:   ∃x ∈ D, ¬Q(x)   →   ¬P(x)
# Converse:         ∃x ∈ D, Q(x)    →   P(x)
# Inverse:          ∃x ∈ D, ¬P(x)   →   ¬Q(x)
