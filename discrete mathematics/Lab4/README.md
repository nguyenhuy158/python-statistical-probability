# LAB 4

## 1. Prove/Disprove the conclusion C using the given data

```bash
(a) Given:
P ="Phong has Visa"
S1="If Phong can fly, Phong will go to America"
S2="If Phong has Visa, Phong will go to America"
S3="If Phong can speak English, Phong will go to America"
Conclusion : C ="Phong goes to America"
```

```bash
(b) Given:
P ="It’s hot yesterday"
S1="If it’s hot, it will rain the next day"
S2="If and only if it’s not rain, Nam goes outside"
S3="If it’s not hot, Nam will go outside"
Conclusion : C ="Nam goes outside"
```

```bash
(c) Given:
Q ="An wake up late"; R ="The traffic is flowing smooth"
S1="The traffic is always heavy on school day"
S2="If An wake up late, he will be late for school on school day"
S3="An only have to go to school on school day"
S4="If An don’t have to go to school, An can’t be late for school"
Conclusion : C ="An is late for school"

```

```bash
(d) Given:
P ="∃x, y ∈ R, (x + y)^2 ≤ x^2 + y^2 ";
Q ="∀x, y ∈ Z+ , x + y ≥ x + y"
R ="∀x, y ∈ Z+ , x + y + 2√(xy) ≥ x + y"
T ="∀x, y ∈ Z+ , √(x + y) ≥ 0"
S1 ="∀x, y ∈ Z+ , x^2 ≥ y^2 → x ≥ y"
S2 ="∀x, y ∈ Z+ , x ≥ y → x^2 ≥ y^2 "
S3 ="∀x, y ∈ R+ , x ≥ y → x^2 ≥ y^2 "
S4 ="∀x, y ∈ R+ , x^2 ≥ y^2 → x ≥ y"
Conclusion : C ="∀x, y ∈ Z+ , √x + √y ≥ √(x + y)"
```

Guide:Student should print which given data used to Prove/Disprove the conclusion in order:

For example:

```python
print("P and S2 -> C")
print("P : % s " % ( P ))
print("S2 : % s " % ( S2 ))
print("C : % s " % ( C ))
```

## 2 Prove/Disprove the following

`(a) ∃x ∈ Z, 0 ≤ x ≤ 100, x 2 = 15 2 + 16 2`

`(b) ∃x ∈ Z, 0 ≤ x ≤ 100, x 2 = 12 2 + 16 2`

`(c) ∃x ∈ Z, −50 ≤ x ≤ 50, x 2 ≥ 99x`

`(d) ∃x ∈ Z, 50 ≤ x ≤ 100, x(x + 1)(x + 2)%6 6 = 0`

`(e) ∃x, y ∈ Z, 0 ≤ x ≤ 100, √x + √y = √(x + y)`

Then print the proof that the statements are valid or invalid such as:

"the given statement is correct when x equal to ..."or

"the given statement is incorrect for all values x within the given domain."

**Hint:** Using Loop to test every possible cases in the given domains.

## 3. Print the negated statements from the following statement then prove/disprove them

`(a) ∀x ∈ Z, 0 ≤ x ≤ 100, x^3 >= x`

`(b) ∀x ∈ Z, 0 ≤ x ≤ 100, and x is even, x ∗ 3 + 1 is a prime number`

`(c) ∀x ∈ Z, 1 ≤ x, y ≤ 100, and x is even, x ∗ 5 + 3 is a prime number`

`(d) ∀c ∈ Z, 0 < c ≤ 100, c%4 = 0, ∃a, b ∈ Z + , c^2 = a^2 + b^2`

`(e) ∀c ∈ Z, 0 < c ≤ 100, c%5 = 0, ∃a, b ∈ Z + , c^2 = a^2 + b^2`

`(f) ∃c ∈ Z, 0 < c ≤ 100, c^2 ≤ c`

**Note:** the negated statements is logical in equivalent to the original state-
ments.

## 4 Prove/disprove that

![image](/41.png)
![image](/42.png)

## 5 Prove/Disprove the following arguments manually without using truth table

![image](/5.png)
