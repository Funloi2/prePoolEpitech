import math


def exo1():
    print("Exo 1 \n")
    print(1 + 1)
    print(30 + 12)
    print(777 + (-735))
    print(1 + 2 + 3 + 5 + 7 + 11 + 13, "\n")


def exo2():
    print("Exo 2 \n")
    print(84 - 42)
    print(0 - (-42))
    print((-6) * (-7))
    print(2 + 5 * 8)
    print((3 + (3 * 4 - 2 * 2) * 3 - 2) * 2 - 3, "\n")


def exo3():
    print("Exo 3 \n")
    print(84 / 2)
    print(84 // 2, "\n")


# def exo4():
#     print("Exo 4 \n")
#     print(84 / (8 + (-3) + (-7) + 2))


def exo5():
    print("Exo 5 \n")
    x = 1 + 11 + 111 + 1111 + 11111 + 111111 + 1111111 + 11111111 + 111111111
    print(x)
    for i in range(2, 8):
        result = x ** i
        print(f"x^{i} =", result)
    y = 1 + 11 + 111 + 1111 + 11111 + 111111 + 1111111 + 11111111 + 111111111 + 1111111111
    for i in range(2, 8):
        result = y ** i
        print(f"y^{i} =", result)
    z = 1 + 11 + 111 + 1111 + 11111 + 111111 + 1111111 + 11111111 + 111111111 + 11111111111
    for i in range(2, 8):
        result = z ** i
        print(f"z^{i} =", result)
    print("\n")


def exo5_2():
    x = 1
    nbrRepeat = int(input("combien de repetition?"))
    result = x
    for i in range(1, nbrRepeat):
        x = x * 10 + 1
        result = result + x
    print(result)
    nbrPuissance = int(input("combien de puissance?"))
    x = result
    for i in range(2, nbrPuissance):
        result = x ** i
        print(f"x^{i} =", result)
    print("\n")


def exo6():
    print("Exo 6 \n")
    print(17 ** 1024, "\n")


def exo7():
    print(42 / 4)
    print(42 // 4)
    print(42 % 4)


def exo8():
    print("Exo 8 \n")
    nbr = int(input("Enter number : "))
    if nbr % 2 == 0:
        print("even \n")
    else:
        print("odd \n")


def exo9():
    print("Exo 9 \n")
    nbr = int(input("Entrer un numéro : "))
    res = 0
    while nbr > 0:
        reste = nbr % 10
        res = res + reste
        nbr = nbr // 10
    print(res, "\n")


def exo10():
    print("Exo 10 \n")
    nbr = float(input("Enter a number: "))
    intNbr = int(nbr)
    print(intNbr, " \n")


def exo11():
    print("Exo 11 \n")
    nbr = float(input("Enter a number: "))
    intNbr = int(nbr)
    decNbr = nbr - intNbr
    print(decNbr, " \n")


def exo12():
    print("Exo 12 \n")
    nbTerms = 1000000
    piApprox = 0
    for i in range(nbTerms):
        if i % 2 == 0:
            piApprox += 4 / (2 * i + 1)
        else:
            piApprox -= 4 / (2 * i + 1)

    print("Approximation of π:", round(piApprox, 6), "\n")


def exo13_2():
    print("Exo 13 \n")
    n_terms = 1000000
    pi_approximation = 0
    for i in range(n_terms):
        if i % 2 == 1:
            pi_approximation = (i**2) / range_exo13(i)
    pi_approximation += 3
    print("Approximation of the π:", round(pi_approximation, 6))

def range_exo13(i):
    return 6 + (i**2/((i-1)**2 * (i+1)**2))

def exo13():
    n_terms = 1000000
    pi_approximation = 0

    for i in range(n_terms):
        term = ((-1) ** i) / (2 * i + 1)
        pi_approximation += term

    pi_approximation *= 4

    print("Approximation of π:", round(pi_approximation, 6))


def exo14():
    denominator = int(input("Dénominateur"))
    numerateur = int(input("Numérateur"))
    gcd = math.gcd(numerateur, denominator)

    reduced_numerator = numerateur // gcd
    reduced_denominator = denominator // gcd

    print(f"{numerateur}/{denominator} = {reduced_numerator}/{reduced_denominator}")




exo1()
exo2()
exo3()
# exo4()
exo5()
# exo5_2()
exo6()
exo7()
# exo8()
exo9()
# exo10()
# exo11()
exo12()
exo13_2()
exo14()
