class letter:
    def __init__(self, morse, english):
        self.morse = str(morse)
        self.english = str(english)


letters = (
    letter(".-", "A"), letter("-...", "B"), letter("-.-.", "C"),
    letter("-..", "D"), letter(".", "E"), letter("..-.", "F"),
    letter("--.", "G"), letter("....", "H"), letter("..", "I"),
    letter(".---", "J"), letter("-.-", "K"), letter(".-..", "L"),
    letter("--", "M"), letter("-.", "N"), letter("---", "O"),
    letter(".--.", "P"), letter("--.-", "Q"), letter(".-.", "R"),
    letter("...", "S"), letter("-", "T"), letter("..-", "U"),
    letter("...-", "V"), letter(".--", "W"), letter("-..-", "X"),
    letter("-.--", "Y"), letter("--..", "Z"), letter(".----", "1"),
    letter("..---", "2"), letter("...--", "3"), letter("....-", "4"),
    letter(".....", "5"), letter("-....", "6"), letter("--...", "7"),
    letter("---..", "8"), letter("----.", "9"), letter("-----", "0"),
    letter("   ", "`"), letter("       ", " "), letter(".-.-.-", "."),
    letter("..--..", "?"), letter("--..--", ","), letter(".-...", "&"),
    letter(".----.", "'"), letter(".--.-.", "@"), letter("-.--.-", ")"),
    letter("-.--.", "("), letter("---...", ":"), letter("-...-", "="),
    letter("-.-.--", "!"), letter("-....-", "-"), letter("-..-.", "%"),
    letter(".-.-.", "+"), letter(".-..-.", '"'), letter("-..-.", "/")
)


def transformString(str):
    s = ""
    for i in range(len(str)):
        if str[i] != " ":
            s += str[i]
            s += "`"
        else:
            s += " "
    else:
        return(s)


def convertListToString(l):
    str = ""
    for i in l:
        str += i
    return str


def convertCodeToLetters(code):
    list = []
    w = 0
    sc = 0
    for i in code:
        if i != " ":
            try:
                list[w].append(i)
                sc = 0
            except:
                list.append([])
                list[w].append(i)
                sc = 0
        else:
            sc += 1
            if sc == 3:
                w += 1

    for i in range(len(list)):
        list[i] = convertListToString(list[i])

    return list


def getLetterMorseToEnglish(str):
    for i in letters:
        if i.morse == str:
            return i.english
    else:
        return "failed"


def getLetterEnglishToMorse(l):
    for i in letters:
        if i.english == l:
            return i.morse
    else:
        return "failed"


def englishToMorse(str):
    str = str.upper()
    str = transformString(str)
    code = ""
    for i in str:
        l = getLetterEnglishToMorse(i)
        code = code + l

    return code


def morseToEnglish(code):
    code = convertCodeToLetters(code)
    str = ""
    for i in code:
        l = getLetterMorseToEnglish(i)
        str += l

    return str


def main():
    print("1 -> English To Morse")
    print("2 -> Morse To English")
    try:
        n = int(input("Enter Your Number: "))
    except:
        print("Failed")
        main()
    if n == 1:
        i = input("Enter Your Message: ")
        print(f"Your Code Is: {englishToMorse(i)}")
    elif n == 2:
        i = input("Enter Your Code: ")
        print(f"Your Sentence Is: {morseToEnglish(i)}")
    else:
        print("Failed")
        main()
    i = str(input("Do You Want To Translate Again(y/n): ")).lower()
    if i == "y":
        main()


if __name__ == '__main__':
    main()
