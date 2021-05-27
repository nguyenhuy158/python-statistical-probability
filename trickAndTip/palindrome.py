def pin(mark):
    for i in mark:
        print(i)
    print()


# QHD
def buildCheck(s):
    # step1 : set all table False
    # s[l][r]
    # + l = r -> True
    # + l(i) r(j)
    #   s[i] = s[j]
    # co 2 th co the xay ra
    # neu i j gan nhau thi s[i][j] -> True
    # ko thi s[i+1][j-1] <-> s[l+1][r-1] neu s[l+1][r-1] = True -> s[i][j] = True va nguoc lai
    n = len(s)
    mark = [[False for i in range(n)] for i in range(n)]
    for i in range(n - 1, 0 - 1, -1):
        mark[i][i] = True  # th chuoi co do dai la 1
        for j in range(i + 1, len(s)):
            mark[i][j] = (s[i] == s[j]) and (i == j - 1 or mark[i + 1][j - 1])

    pin(mark=mark)


def checkPalindrome(inputString):
    lst = []
    for i in inputString:
        lst.append(i)
    lst.reverse()

    if ''.join(lst) == inputString:
        return True

    return False


print(buildCheck('1211'))
