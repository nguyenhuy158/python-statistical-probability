def thieves(x):
    if x <= 0:
        return 0
    if x == 1:
        return 1
    if x == 2:
        return 2

    # total = 0
    # for i in range(x - 1, 0, -1):
    #     total += thieves(i)
    # return x + total
    return x + thieves_sum(x - 1)


def thieves_sum(n):
    if n <= 0:
        return 0
    else:
        return thieves(n) + thieves_sum(n - 1)


def isSent(day, n=40):
    # print("n", n - thieves_sum(day))
    if thieves(day) <= (n - thieves_sum(day)):
        return True
    return False


def maxDay(n=40):
    print(n)
    day = 0
    while isSent(day, n):
        day += 1

    return day - 1


print("ngay cuoi ", maxDay(0))
print("ngay cuoi ", maxDay(100))
print("ngay cuoi ", maxDay(1000))

for i in range(10):
    day = i
    print(
        "day",
        day,
        "ten cuop phai sai di",
        thieves(day),
        "sai di duoc hay khong",
        isSent(day),
    )


# day = 1
# print(
#     "day",
#     day,
#     "ten cuop phai sai di",
#     thieves(day),
#     "sai di duoc hay khong",
#     isSent(day),
# )
# day = 2
# print(
#     "day",
#     day,
#     "ten cuop phai sai di",
#     thieves(day),
#     "sai di duoc hay khong",
#     isSent(day),
# )
# day = 3
# print(
#     "day",
#     day,
#     "ten cuop phai sai di",
#     thieves(day),
#     "sai di duoc hay khong",
#     isSent(day),
# )
# day = 4
# print(
#     "day",
#     day,
#     "ten cuop phai sai di",
#     thieves(day),
#     "sai di duoc hay khong",
#     isSent(day),
# )
# day = 5
# print(
#     "day",
#     day,
#     "ten cuop phai sai di",
#     thieves(day),
#     "sai di duoc hay khong",
#     isSent(day),
# )
