import random
from datetime import date

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
    score = 10
    word = random.choice(openFile())
    dashArray(word)
    highScoreData = getHighScore(getScore("python"))
    if highScoreData is None:
        highScore = 0
    else:
        highScore = highScoreData[0][2]
    while True:
        printDashWord()
        printScore(score)
        letter = askString()
        if letter == word:
            if score > int(highScore):
                saveScore(word, score)
                printNewHighScore(word, score)
            else:
                printWin(word, highScore)
            break
        elif letter in word:
            checkLetter(letter, word)
            if "_" not in dashWord:
                printWin(word, highScore)
                break
        else:
            score -= 1
            if score == 0:
                printLose(word)
                break
    return None


def printNewHighScore(word, score):
    print("You have a new high score!")
    print("The word was: " + word)
    print("You guessed the word in " + str(10-score) + " turns")
    print("\n")


def printWin(word, highScore):
    print("You won!!")
    print("The word was: " + "".join(word))
    print("You guessed the word in " + str(10 - score) + " turns")
    print("The high score for this word is: " + (10-highScore))
    print("\n")


def printLose(word):
    print("You lose!")
    print("The word was: " + "".join(word))
    print("\n")




def askString():
    while True:
        try:
            string = str(input("Enter a word or a letter: "))
            if string == "":
                print("Please enter a valid word or a valid letter")
                continue
            else:
                return string
        except ValueError:
            print("Please enter a valid word or a valid letter")


def dashArray(word):
    for i in range(0, len(word) - 1):
        dashWord.append("_")
    return None


def checkLetter(letter, word):
    for i in range(0, len(word)):
        if letter == word[i]:
            dashWord[i] = letter
    return None


def printDashWord():
    print(dashWord)
    return None


def printScore(score):
    if score == 1:
        print("Turn left: " + str(score))
        return None
    print("Turns left: " + str(score))
    return None


def openFile() -> list:
    try:
        wordListFile = []
        with open('words.txt') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                wordListFile.append(line.strip())
        return wordListFile
    except FileNotFoundError:
        print("File not found")
        wordListFile = []
        return wordListFile


def getScore( word):
    try:
        listWordsScore = []
        with open('score.txt', 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                if line.strip().split("-")[0] == word:
                    listWordsScore.append(line.strip().split("-"))
        return listWordsScore
    except FileNotFoundError:
        print("File not found")
        return None


def getHighScore(listWordScore):
    index = 0
    if len(listWordScore) == 1 or listWordScore is None:
        return listWordScore
    else:
        for i in listWordScore:
            if i[2] > listWordScore[index][2]:
                index = listWordScore.index(i)
        return listWordScore[index]


def saveScore(word, score):
    try:
        dateOfScore = date.today()
        formatDate = dateOfScore.strftime("%d/%m/%Y")
        with open('score.txt', 'a') as f:
            f.write(word + "-" + formatDate + "-" + str(score) + "\n")
    except FileNotFoundError:
        print("File not found")
        return None

