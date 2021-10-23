# P = "Phong has Visa"
# S1 = "If Phong can fly, Phong will go to America"
# S2 = "If Phong has Visa, Phong will go to America"
# S3 = "If Phong can speak English, Phong will go to America"
# Conclusion: C = "Phong goes to America"

print("P and S2 -> C")
print("If Phong has Visa, Phong will go to America (by S2)")
print("Phong has Visa (by P)")
print("C: Phong goes to America (by Modus Ponens)")


# P = "It’s hot yesterday"
# S1 = "If it’s hot, it will rain the next day"
# S2 = "If and only if it’s not rain, Nam goes outside" <=>
# if it's not rain, Nam goes outside ^ if Nam goes outside, it's not rain
# S3 = "If it’s not hot, Nam will go outside"
# Conclusion: C = "Nam goes outside"

print("S1 and P -> C1")
print("If it’s hot, it will rain the next day (by S1)")
print("It’s hot yesterday (by P)")
print("C1: It's rain today (by Modus Ponens)")

print("C1 and S2 -> C2")
print("If and only if it’s not rain, Nam goes outside (by S2)")
print("if it's not rain, Nam goes outside ^ if Nam goes outside, it's not rain (by sepecialization)")
print("It's rain today (by C1)")
print("C2: Nam doesn't goes outside (by Modus Tollens)")


# Q = "An wake up late"
# R = "The traffic is flowing smooth"
# S1 = "The traffic is always heavy on school day"
# S2 = "If An wake up late, he will be late for school on school day"
# S3 = "An only have to go to school on school day"
# S4 = "If An don’t have to go to school, An can’t be late for school"
# Conclusion: C = "An is late for school"

print("S1 and R -> C1")
print("The traffic is always heavy on school day (by S1)")
print("The traffic is flowing smooth (by R)")
print("C1: It is not school day (by Modus Ponens)")

print("S2 and C1 -> C2")
print("If An don’t have to go to school, An can’t be late for school (by S4)")
print("It is not school day (by C1)")
print("C: An is not late for school (by Modus Ponens)")
