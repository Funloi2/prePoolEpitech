def test():
    try:
        listWordsScore = []
        with open('Hangman/score.txt', 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                print(line.strip().split("-"))
                if line.strip().split("-")[0] == "water":
                    listWordsScore.append(line.strip().split("-"))
        print(listWordsScore)
    except FileNotFoundError:
        print("File not found")
        return None