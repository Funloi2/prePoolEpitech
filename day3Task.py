import re


def strChain():
    # strChain = input("Enter a string: ")
    return "Word String"


def task00():
    print("STRINGS \n")
    print("Exo 0 \n")
    print(strChain())


def task01():
    print("Exo 1 \n")
    print(strChain()[0])
    print(strChain()[4])


def task02():
    print("Exo 2 \n")
    print(strChain()[-1])


def task03():
    print("Exo 3 \n")
    print(strChain()[4:9])


def task04():
    print("STRING METHODS \n")
    print("Exo 1 \n")
    print(strChain().lower())


def task05():
    print("Exo 2 \n")
    print("tutu on the tuki-kata".replace("tu", "ta"))


def task06():
    print("Exo 3 \n")
    string = " hello world " # this line stores the string " hello world " in the variable string
    position = string.find("a") # this line stores the position of the first occurrence of the letter "a" in the variable position
    print(position) # this line prints the value of the variable position


def task07():
    print("Exo 4 \n")
    print(strChain()[:: -2][:5][:: -1][3:])

def task08():
    print("Exo 5 \n")
    print(strChain()[-2])


def task09():
    print("Exo 6 \n")
    for loop in range(10):
        print(loop + 1 , strChain())


def task010():
    print("Exo 7 \n")
    s1 = " Hello "
    s2 = 42
    # concat = s1 + s2
    print(s1, s2)


def task011():
    print("Exo 8 \n")
    string1 = "42"
    string2 = " is"
    string3 = " the answer"
    concat = string1 + string2 + string3
    print(" The string \"", concat, "\" contains 16 characters ).")


def task012():
    print("Exo 9 \n")
    string = "thE Cat’s tactic wAS tO surpRISE thE mIce iN tHE gArdeN"
    count = 0
    countWord = ["cat", "mice", "garden"]
    for word in countWord:
        count += string.lower().count(word)
    for word in countWord:
        count += string.lower()[::-1].count(word)
    print(count)


def askName():
    return input("Enter your name: ")


def askNumber():
    return int(input("Enter a number: "))

def task013():
    print("INPUT \n")
    print("Exo 1 \n")
    print("Hello", askName(), "!")


def task014():
    print("Exo 2 \n")
    print("Hello", askName().capitalize(), "!")


def task015():
    print("Exo 3 \n")
    number1= askNumber()
    number2= askNumber()
    print("The sum of", number1, " + ", number2, "is equal to", number1 + number2, ".")


def task016():
    print("Exo 4 \n")
    print("Enter a whole number:")
    number1 = askNumber()
    print(type(number1))


def askSentences():
    return input("Enter sentences: ")


def task017():
    print("Exo 5 \n")
    sentences = askSentences()
    sentence_pattern = r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!) "
    sentence = re.split(sentence_pattern, sentences)
    finalSentence = ""
    for i in range(len(sentence)):
        finalSentence += sentence[i].split(" ")[0] + " "
    print(finalSentence)
