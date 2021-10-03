# 1. Calculate and print the following expressions using python:

# 2. Print the expression from 1. with their result as a string; for example (a) will be printed as: `15*2+7*8=86`

# 3. Write a function S=sumN(n) to calculate the sum from 0 to n; for example sumN(2) should return 0+1+2=3; sumN(-5) should `return 0+(-1)+(-2)+(-3)+(-4)+(-5)=-15`

# 4. Write a function to print an input string then:

- (a) Remove all space `(" ")` then print the result string
- (b) Replace all space `(" ")` with `'_'` then print the result string

**Hint**: Use A=Input(“Input your string:”) to input a string to A from
keyboard. Use B=A.split() to make a list of words from a string for processing.
Use `C=" ".join(B)` to merge the list back into a string with a blank space
`" "` between words.

# 5. Write a function to calculate an operation between 2 positive integers using If for different operators cases. For example, input: 1+2 -> output: 3;

`input: 2*3 -> output: 6;`. . . the possible input operators
are: `+, -, *, /,%,^.`

**Hint**: you will need to separate the input string into 3 sub-strings: first
number; operator; second number.

**Hint2**: to convert a string such as `str1='23'` to number we use `number1=int(str1)` to get `number1=23`

# 6. Write a function to do the same job as previous exercise but using Dictionary instead of If

# 7. Write a function to calculate summation of 2 matrices `C=mSum(A,B)` where A,B,C are lists used to representation 3 matrices; if the product can’t be calculated due to matrix size print:`"Matrix dimension error".`

**Hint**: the summation of matrix A size `m × n` and B size `m × n` is matrix C size
`m × n` where: `Ci;j = Ai;j + Bi;j`

# 8. Write a function to calculate product of 2 matrices C=mProd(A,B); if the product can’t be calculated due to matrix size print:`"Matrix dimension error".`

# 9. Write functions to combine 2 strings p,q represent 2 statements whose first words are the subjects using:
- (a) `"if p, then q" result=ithCombine(p,q).`
- (b) `"p, and not q" result=panqCombine(p,q).`
- (c) `"not p, or q" result=npoqCombine(p,q)`

**for example**: `p="it sunny"`, `q="I go camping"` will give the output
- (a) if its sunny, then I go camping
- (b) it sunny and I not go camping
- (c) it not sunny, or I go camping
