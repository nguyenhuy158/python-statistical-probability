import random

MIN = 26
MAX = 26 * 26 * 26


def myReplace(input, source, destination):
    output = ""
    for index in range(len(input)):
        try:
            output += destination[source.index(input[index])]
        except:
            output += input[index]
    return output


def Encryption(input):
    # assign output
    output = input

    # template
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    substitutionAlphabet = list("--------------------------")

    # create substitution alphabet
    for i in range(len(alphabet)):
        index = random.randint(MIN, MAX) % 26
        while substitutionAlphabet[index] != "-":
            index = random.randint(MIN, MAX) % 26
        substitutionAlphabet[index] = alphabet[i]

    # store key
    writeToFile("./key.txt", " ".join(alphabet) + "\n" + " ".join(substitutionAlphabet))

    # encryption
    output = myReplace(input, alphabet, substitutionAlphabet)
    # print("source     ", alphabet)
    # print("destination", substitutionAlphabet)
    return output


def Decryption(input):
    output = input

    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    frequencyAlphabet = {char: output.count(char) for char in alphabet}
    sort_orders = sorted(frequencyAlphabet.items(), key=lambda x: x[1], reverse=True)

    letterFrequencies = [
        "e",
        "t",
        "a",
        "i",
        "n",
        "o",
        "s",
        "h",
        "r",
        "d",
        "l",
        "u",
        "c",
        "m",
        "f",
        "w",
        "y",
        "g",
        "p",
        "b",
        "v",
        "k",
        "q",
        "j",
        "x",
        "z",
    ]

    frequencyAlphabet = [i[0] for i in sort_orders]
    # print("source     ", letterFrequencies)
    # print("destination", frequencyAlphabet)

    # output = frequencyAlphabet
    output = myReplace(input, frequencyAlphabet, letterFrequencies)
    return output


def readFromFile(path):
    output = ""
    with open(path, mode="r") as fileInput:
        output = fileInput.readline()
    return output


def writeToFile(path, data=""):
    with open(path, mode="w") as fileOutput:
        fileOutput.write(data)


def main():
    plainText = readFromFile("./input.txt")

    result = Encryption(plainText)
    writeToFile("./ciphertext.txt", result)

    result = Decryption(result)
    writeToFile("./plainText.txt", result)


if __name__ == "__main__":
    main()
