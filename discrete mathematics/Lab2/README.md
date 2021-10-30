# 1. Write python functions to calculate:

- logical implies `r = lImplies(p, q)`
- logical and `r = lAnd(p, q)`
- logical or `r = lOr(p, q)`
- logical xor(!=) `r = lXor(p, q)`
- logical not r = `lNot(p, q)`
- logical equivalent(==) `r = lEquivalent(p, q)`

where p, q and r are logical variables
**Hint**: to define a function in python we use:

```
def function(inputVariables):
    # calculate
    pass

```

# 2. Write python functions to calculate:

- logical implies `R=lLImplies(P,Q)`
- logical and `R=lLAnd(P,Q)`
- logical or `R=lLOr(P,Q)`
- logical xor `R=lLXor(P,Q)`
- logical not `R=lLNot(P)`
- logical equivalent `R=lLEquivalent(P,Q)`

where P,Q and R are 3 lists of logical variables for example with:

`P= [True, True, False, False]; `

`Q= [True, False, True, False]: `

Then we have:
| P | Q | lLIpmlies(P,Q) | lLAnd(P,Q) | lLOr(P,Q) | lLXor(P,Q) | lLNot(P) | lLEquivalent(P,Q) |
| --- | --- | -------------- | ---------- | --------- | ---------- | -------- | ----------------- |
| T | T | T | T | T | F | F | T |
| T | F | F | F | T | T | F | F |
| F | T | T | F | T | T | T | F |
| F | F | T | F | F | F | T | T |

# 3. Write python program to calculate and print truth table for following expressions:

p∧q→r

r→p∧q

The table should contain a row for each possible combination of values for variables p, r and q and columns for the final result as well as each relevant Boolean subexpression.

**Hint**:import function product from libraryitertools.
use `intertools.product():`

`table = list(intertools.product([False, True], repeat=n))`

result for `n = 3`:

```
[
    (False, False, False),
    (False, False, True),
    (False, True, False),
    (False, True, True),
    (True, False, False),
    (True, False, True),
    (True, True, False),
    (True, True, True),
]
```

# 4. Write python programs to calculate and print truth table for following expressions.

- `p∨q→p∧q→¬p∨¬q`

- `¬p∨(q∧r)→r `

- `(p→q)∧(q→r) `

- `(p∨(q∧r))↔((p∨q)∧(p∨r)) `

- `p∨q→¬r∨t `

- `p∨t→q→(r→t) `

- `(p∨(q∧r))↔(((p∨q)∧(p∨r))∧(t∨¬t)) `

# 5. Write python programs to tell if the following formulas are equivalent:(The programs should print “equivalent” or “Inequivalent” as result)

- `p≡¬(¬p) `

- `¬(¬q∧p)∧(q∨p)≡q `

- `¬(p∨q)≡(¬p∨¬q) `

- `(p∨q)→r≡(p→r)∧(q→r) `

- `¬(p∧q)≡(¬p∧¬q) `

- `(p∨¬q)→¬p≡(p∨(¬q))→¬p`

- `¬(p∨q)≡(¬p∧¬q)`

# 6. Write python programs to show the validity of the following argument:(the programs should simply print “INVALID” or “VALID” as result)
