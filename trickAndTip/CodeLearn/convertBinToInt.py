def messageFromBinaryCode(code):
    print(type(len(code) // 8))
    ans = ['' for x in range(len(code) // 8)]
    for i in range(0, len(code)):
        ans[i // 8] += code[i]

    print(ans)
    return ''.join([chr(int(x, 2)) for x in ans])

# 01... -> Hello!
print(messageFromBinaryCode('010010000110010101101100011011000110111100100001'))
