# The Logic of Compound Statements

# Exercises

## 1

Determine and print domain D, predicate P of the following expression then write the statement in formal form:

- (a) For all fishes, they need water to survive.
- (b) Exist a person, who is left handed
- (c) Exist an employee in the company, who is late to work everyday.
- (d) For all fishes in this pond, they are Koi fish.
- (e) There is at least one creature in the ocean, it can live on land
- (f) Every students in class A did not pass the test

**Example**: "For all students, they need to attend classes and do homework." The answer is:

D is "students"

P is "need to attend classes and do homework"

Formal form: For all x in D, P(x)

The answer can be obtain with the following code:

```
# For all students, they need to attend classes and do homework.
print ("D is ’students’")
print ("P is ’need to attend classes and do homework’")
print ("Formal form : For all x in D, P(x)")
```

## 2

Write a function [D,P,F]=formalConvert(S) to extract D and P then convert the statement S from Exercise 1. excluded (f) to formal form F.

**Hint**: D contains the words between For all/ Exist/ There is at least one and a comma (,);

P contains the words after the first word from the comma (,).

## 3

Determine and print domain D, predicate P and Q of the following expression then write the statement in formal form:

For example: with (a) D is "people", P is "is blond", Q is "is westerner".

formal statement: for all x in D, P(x) then Q(x). You can print them like in Exercise 1.

- (a) For all people, if they are blond then they are westerners.
- (b) Exist a person, whose hair is black but is a westerner.
- (c) For all students, if they study correctly then they have high score.
- (d) For every mammal, if they live in the sea, they are either dolphins or
  whales.
- (e) For every bird, if they don’t have wings and can swim then they are
  penguins.
- (f) Exist a bird, who have wing but can’t fly.

## 4

Write a function [D,P,Q,F]=formalConvertPQ(S) to extract D, P and Q then convert the statement S from 3. to formal form F.

## 5

Write a function N=nega(A) to calculate and print the negation of statement from Exercise 1. excluded (f)
For example: output of 1.(a) is: Exist fish, they not need water to lives.

## 6

Print Negation, Contra-positive, Converse, Inverse of all the above state-
ments from in informal statement from Exercise 3.;

**Hint**: Most statements in Exercise 3. has the form `∀x ∈ D, P(x) → Q(x)`

`Negation: ∃x ∈ D, P(x) ∧ ¬Q(x)`

`Contrapositive: ∀X ∈ D, ¬Q(x) → ¬P(x)`

`Converse: ∀X ∈ D, Q(x) → P(x)`

`Inverse: ∀X ∈ D, ¬P(x) → ¬Q(x)`


For example: `For all planets, if they have human, they have life.` The answer is as follow:

```
print("Negation : There is a planet, it has human but doesn't have life")

print("Contrapositive : For all planets, if they don't have life then they don't have human")

print("Converse : For all planets, if they have life, they have human")

print("Invert : For all planets, if they don ’t have life, they don't have human")
```
