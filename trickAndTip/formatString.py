# CodelearnIsAwesome -> codelearn is awesome

def amendTheSentence(s):
    lst = []
    for i in s:
        lst.append(i)
    print(f"{''.join(lst)}\n{s}")

    i = 0
    while i < len(lst):
        if lst[i].isupper() and i:
            lst[i] = lst[i].lower()
            lst.insert(i, ' ')
        i += 1

    lst[0] = lst[0].lower()
    return ''.join(lst)


print(amendTheSentence('vSKwWDjwIerQKMgVaAniorRJlerbKpDgvyKBLPNwSRWtylqKewNFtERNuUBBHAsGkTSSfdhQHJYvAighAdeG'))
