
print("Day 4 Task\n")

def task1_0():
    print("Task 0\n")
    print("42 > 12 return True\n" )
    print("12 = 12 retourne une erreur car il un seul égale signifie qu'on attribue une valeur à une variable et un int ne peut pas etre une variable \n" )
    print("12 == 12 return True car ici il y a deux égales\n" )
    print(" \" Hello\" == \" World\" retourne False car les deux chaines de caractères sont différentes\n" )
    print ("218 >= 118 return True car l'égalité est vrai\n" )
    print("\"a\".upper() == \"A\" retourne True \n" )
    print("1*2*3*4 <= 9 retourne False \n")
    print("\"z\" in \"azerty\" retourne True car z est dans azerty\n")


def AskNumber():
    nbr = int(input("Entrer un numéro : "))
    return nbr


def AskString():
    string = input("Entrer une chaine de caractère : ")
    return string
#
# def task1_1():
#     print("Task 1\n")
#     nbr = AskNumber()
#     if nbr == 42 :
#         print("Vous avez trouvé la réponse à la grande question de la vie, de l'univers et de tout le reste !")
#     else:
#         print("Mauvaise réponse !")
#
#
# def task1_2():
#     print("Task 2\n")
#     nbr = AskNumber()
#     if nbr % 2 == 0:
#         print("even \n")
#     else:
#         print("odd \n")
#
#
# def task1_3():
#     print("task 3\n")
#     str = AskString()
#     if str == "Open Sesame":
#         print("Bienvenue !")
#     elif str == "will you open you damn gtrqjgjklasdg" :
#         print("access fcking denied")
#     else:
#         print("access denied")
#
#
# def task1_4():
#     print("task 4\n")
#     nbr = AskNumber()
#     if nbr == 42 or nbr <= 21 or nbr%2 == 0 or (nbr % 2) < 21 or (nbr %2 ==1 and nbr >= 45):
#         print("OK")
#     else:
#         print("You got it wrong")
#
#
# def task1_5():
#     print("task 5\n")
#     a = 41
#     b = 42
#     if a == b:
#         print("a and b are equal")
#     elif a <= b:
#         print("a is less or equal than b")
#     elif a != b:
#         print("a and b are different")
#
#
# def task2_0():
#     print("task 0\n")
#     for i in range(1, 1001):
#         print(i,"\n")
#
#
# def task2_1():
#     print("task 1\n")
#     str = AskString()
#     for i in str:
#         print(i*2, end="")
#
#
# def task2_2():
#     print("task 2\n")
#     for i in range(1, 10001):
#         if i%7 == 0:
#             print(f"{i} est un multiple de 7")
#
#
# def task2_3():
#     print("task 3\n")
#     for i in range(-30,31):
#         if i%3 == 0:
#             print(f"{i}Fizz")
#         elif i%5 == 0:
#             print(f"{i}Buzz")
#         elif i%3 == 0 and i%5 == 0:
#             print(f"{i}FizzBuzz")
#         else:
#             print(i)
#

# def task2_4():
#     print("task 4\n")
#     for i in range(99,0,-1):
#         if i == 1:
#             print(f"{i} bottle of age appropriate bottles on the wall")
#             break
#         print(f"{i} bottles of age appropriate bottles on the wall")
#
#
def task2_5():
    print("task 5\n")
    nbr = AskNumber()
    for i in range(2, nbr // 2 + 1):
        multiples = [j for j in range(nbr - 1, 1, -1) if j % i == 0]
        if multiples:
            print(multiples)


# def task2_6():
#     print("task 6\n")
#     nbr = AskNumber()
#     str = AskString()
#     if nbr ==0 :
#         return None
#     elif any(char in str for char in "aeiouy"):
#         print(nbr)
#     elif nbr >= 42 :
#         print(nbr)
#     else:
#         print(str)
#

# def task3_1():
#     print("task 1\n")
#     print("Give a key")
#     nbr = AskNumber()
#     print("Give a message to encrypt")
#     str = AskString()
#     for i in str:
#         print(chr(ord(i) + nbr), end="")
#
# def task3_15():
#     print("task 1.5\n")
#     print("Give a key to decrypt")
#     nbr = AskNumber()
#     print("Give a message to decrypt")
#     str = AskString()
#     for i in str:
#         print(chr(ord(i) - nbr), end="")
#

# def task3_2():
#     print("task 2\n")
#     print("Give a text to encrypt")
#     toCrypt = AskString()
#     print("Give a key")
#     key = AskString()
#     temp = len(toCrypt) - len(key)
#


#     for i in toCrypt:
#         for j in key:
#             print(chr(ord(i) + ord(j)), end="")
#             break
#     print("\n")
#     print("Give a text to decrypt")
#     toDecrypt = AskString()
#     print("Give a key")
#     key = AskString()
#     for i in toDecrypt:
#         for j in key:
#             print(chr(ord(i) - ord(j)), end="")
#             break