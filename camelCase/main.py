# input camel case
# output camelCase

s = input("enter string: ")
s = s.title()
s = s.split()
s[0] = s[0].lower()
s = ''.join(s)
print(s)