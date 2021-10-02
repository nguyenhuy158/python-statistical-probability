# CodelearnIsAwesome -> codelearn is awesome

def amendTheSentence(s):
    lst = []
    for i in s:
        lst.append(i)

    # print teamplate string
    print('way1:', f"{''.join(lst)}\n{s}")
    print('way2:', '%s\n%s' % (''.join(lst), s))
    print('way3:', '{}\n{}'.format(''.join(lst), s))

    i = 0
    while i < len(lst):
        if lst[i].isupper() and i:
            lst[i] = lst[i].lower()
            lst.insert(i, ' ')
        i += 1

    lst[0] = lst[0].lower()
    return ''.join(lst)


print(amendTheSentence('vSKwWDjwIerQKMgVaAniorRJlerbKpDgvyKBLPNwSRWtylqKewNFtERNuUBBHAsGkTSSfdhQHJYvAighAdeG'))
