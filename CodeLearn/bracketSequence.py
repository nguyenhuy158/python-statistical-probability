# ()() -> true

def regularBracketSequence(sequence):
    ans = 0
    for i in sequence:
        if i == '(':
            ans += 1
        else:
            if not ans:
                return False
            ans -= 1

    if ans:
        return False
    return True


print(regularBracketSequence('())()'))
