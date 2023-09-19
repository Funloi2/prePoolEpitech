import random

wordList = ["hangman", "game", "python", "computer", "science", "programming", "mathematics", "player", "condition",
        "reverse", "water", "board", "geeks"]

dashWord = []
score = 10

def choiceMenu():
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice < 1 or choice > 2:
                print("Please enter a valid choice")
                continue
            else:
                return choice
        except ValueError:
            print("Please enter a number")


def playGame():
    global score
    global dashWord
    dashWord = []
    score = 10
    word = random.choice(wordList)
    dashArray(word)
    while True:
        print(word)
        printDashWord()
        printScore(score)
        letter = askString()
        if checkWord(letter, word):
            print("You win!")
            print("The word was: " + "".join(word))
            print("\n")
            break
        elif letter in word:
            checkLetter(letter, word)
            if "_" not in dashWord:
                print("You win!")
                print("The word was: " + "".join(word))
                print("\n")
                break
        else:
            score -= 1
            if score == 0:
                print("You lose!")
                print("The word was: " + "".join(word))
                print("\n")
                break
    return None
def printMenu():
    print("Welcome to Hangman!")
    print("1. Play Game")
    print("2. Exit")
    print("\n")


def printGameMenu():
    print("1. Play Again")
    print("2. Exit")
    print("\n")

def askString():
    while True:
        try:
            string = str(input("Enter a string: "))
            if string == "":
                print("Please enter a valid string")
                continue
            else:
                return string
        except ValueError:
            print("Please enter a string")


def dashArray(word):
    for i in range(0, len(word)):
        dashWord.append("_")
    return None


def checkLetter(letter, word):
    for i in range(0, len(word)):
        if letter == word[i]:
            dashWord[i] = letter
    return None


def checkWord(wordInput, word):
    if wordInput == word:
        return True
    return False


def printDashWord():
    print(dashWord)
    return None


def printScore(score):
    if score == 1:
        print("Turn left: " + str(score))
        return None
    print("Turns left: " + str(score))
    return None


def getLength(word):
    return len(word)


def printDash(word):
    for i in range(0, len(word)):
        print("_", end="")
    print("\n")


def printWord(word):
    print(word)