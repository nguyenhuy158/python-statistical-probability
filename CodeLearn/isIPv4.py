def isIPv4Address(inputString):
    inputString = inputString.split('.')
    print(len(inputString), inputString)
    if len(inputString) != 4:
        return False

    for i in inputString:
        if len(i) and i.isnumeric():
            if int(i) < 0 or int(i) > 255:
                return False
        else:
            return False
    return True


print(isIPv4Address('1.254.255.1a'))