import hangman

def main():
    hangman.printMenu()
    choice = hangman.choiceMenu()
    while choice != 2:
        hangman.playGame()
        hangman.printGameMenu()
        choice = hangman.choiceMenu()
    print("Goodbye!")

main()