import os
import time

nbrSandwich = 0


def task1_0():
    print("task 0\n")
    print("These code create 2 functions, the first one returns the double of the value x + 1 that have been passed "
          "as parameter, the second one returns 7, the rest of  the code is just practical exemple of the use of "
          "these codes\n")


def bread():
    print("<//////////////////////>")


def tomato():
    print("0 0 0 0 0 0 0 0 0 0 0 0")


def lettuce():
    print("~~~~~~~~~~~~~~~~~~~~~~~")


def ham():
    print("=======================")


def askNumber():
    while True:
        try:
            number = int(input("Enter a number: "))
            if number < 0:
                print("Please enter a positive number")
                continue
            else:
                nbrSandwich = number
                return number
        except ValueError:
            print("Please enter a number")


def askOption():
    while True:
        try:
            string = str(input("Enter a string: "))
            if string == "veg":
                return string
            elif string == "" or string == " ":
                return "meat"
            else:
                print("Please enter a valid option")
                continue
        except ValueError:
            print("Please enter a string")


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


def task1_1():
    print("task 1\n")
    bread()
    lettuce()
    tomato()
    ham()
    bread()


def task1_2():
    print("task 2\n")
    for i in range(42):
        print(i + 1)
        sandwichMeat()
        print("\n")


def sandwichMeat():
    bread()
    lettuce()
    tomato()
    ham()
    bread()


def sandwichVeg():
    bread()
    lettuce()
    tomato()
    lettuce()
    tomato()
    bread()


def task1_3(nbrSandwich):
    print("task 3\n")
    for i in range(nbrSandwich):
        print(i + 1)
        sandwichMeat()
        print("\n")


def task1_4(option):
    print("task 4\n")
    if option == "veg":
        sandwichVeg()
    else:
        sandwichMeat()


def task_challenge(nbr, power):
    print("task challenge\n")
    startTime = time.time()
    res = 1
    for i in range(power):
        res = res * nbr
    endTime = time.time()

    print(endTime - startTime)


def task2_1():
    print("task 1\n")
    string = askString()
    task2_recursive1(string)


def task2_recursive1(string):
    string = string.lower()
    string = string.strip()
    lenString = len(string)
    if lenString == 0 or lenString == 1:
        print("Palindrome")
    elif string[0] == string[lenString - 1]:
        string = string[1:lenString - 1]
        task2_recursive1(string)
    else:
        print("Not a palindrome")

directory = os.getcwd()
def task2_2():
    print("task 2\n")
    task2_recursive2(os.getcwd())


def task2_recursive2(directory):
    items = os.listdir(directory)

    for item in items:

        item_path = os.path.join(directory, item)

        # Check if it's a file or directory
        if os.path.isfile(item_path):
            print("File:", item_path)
        elif os.path.isdir(item_path):
            print("Directory:", item_path)
            # Recursively list files and directories in subdirectories
            task2_recursive2(item_path)

    # lenDirectory = len(directory)
    # cpt = 0
    # print(directory)
    # if lenDirectory == 0:
    #     return print("No more files")
    # else:
    #     for i in range(lenDirectory):
    #         print(os.getcwd() + "\\" + directory[i])
    #         if os.path.isdir(directory[i]):
    #
    #             os.chdir(os.getcwd() + "\\" + directory[i])
    #             task2_recursive2(os.listdir())
    #             # print(os.chdir(os.getcwd() + "\\" + i))
    #             # print(directory2)
    #             # task2_recursive2(directory2)
    #         else:
    #             print("not a directory")
    #     task2_recursive2(path)
    #     cpt += 1




def funcA(string, nbr):
    cpt = 0
    for char in string:
        if char.islower():
            cpt += 1
    if cpt >= nbr:
        return True
    return False

def funcB(string, nbr):
    cpt = 0
    for char in string:
        if char.isupper():
            cpt += 1
    if cpt >= nbr:
        return True
    return False

def funcC(string, nbr):
    if len(string) >= nbr:
        return True
    return False

def funcD(string, nbr):
    cpt = 0
    for char in string:
        if not char.isalnum():
            cpt += 1
    if cpt >= nbr:
        return True
    return False

def funcE(string, nbr):
    cpt = 0
    for char in string:
        if char.isdigit():
            cpt += 1
    if cpt >= nbr:
        return True
    return False


def check_password(string2, nbr, string ):

    if string2 == "lower":
        return funcA(string, nbr)
    if string2 == "upper":
        return funcB(string, nbr)
    if string2 == "length":
        return funcC(string, nbr)
    if string2 == "special":
        return funcD(string, nbr)
    if string2 == "digit":
        return funcE(string, nbr)


def task3_1():
    try:

        print("task 1\n")
        print("entrer un mot de passe")
        string = askString()
        # nbr = askNumber()
        # string2 = askString()
        print(check_password("lower", 2, string) and check_password("special", 2, string))
    except ValueError:
        print("error")


def array_diff(a, b):
    for i in a :
        for j in b:
            if i == j :
                a.remove(i)
    return a

