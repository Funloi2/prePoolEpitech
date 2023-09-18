import random
import time

listNB = []


def AskNumber():
    nbr = int(input("Entrer un numéro : "))
    return nbr

def AskString():
    string = input("Entrer une chaine de caractère : ")
    return string

def defineList():
    cpt = 0
    while cpt < 5:
        nbr = AskNumber()
        listNB.append(nbr)
        cpt += 1


def defineListSize():
    print("Choisir la taille de la liste")
    size = AskNumber()
    return size

def task1_0():
    defineListSize()
    defineList()

def task1_1():
    print("task 1\n")
    print(listNB[0])

def task1_2():
    print("task 2\n")
    lenList = len(listNB)
    print(listNB[lenList-1])


def task1_3():
    print("task 3\n")
    print("ajouter un element")
    addElem = AskNumber()
    listNB.append(addElem)


def task1_4():
    print("task 4\n")
    print(listNB)


def task1_5():
    print("task 5\n")
    del listNB[len(listNB)-1]


def task1_6():
    print("task 6\n")
    addElem = AskNumber()
    listNB.insert(0, addElem)
    print(listNB)


def task1_7():
    print("task 7\n")
    print(listNB[1:4])


def task1_8():
    print("task 8\n")
    list2 = []
    for i in range(len(listNB)-1, 0, -1):
        list2.append(listNB[i])
    print(list2)


def task1_9():
    print("task 9\n")
    for i in range(0, len(listNB),2):
        print(listNB[i], end=" ")


def task1__10():
    print("task 10\n")
    cpt = 17
    for i in range(0, len(listNB)):
        addElem = random.randint(0, 100)
        listNB.append(addElem)
    print(listNB)


def task1__11():
    print("task 11\n")
    first_line = [1,2,3]
    second_line = [4,5,6]
    print(first_line.extend(second_line), "\n")
    print([*first_line, *second_line])


def task2_1():
    print("task 1\n")
    newList = []
    for i in range(0, 10):
        newList.append(random.randint(0, 100))
    print(newList)
    for i in range(0, len(newList)-1):
        for j in newList:
            print(j*newList[i], end=" ")
        print("\n")


def task2_2():
    print("task 2\n")
    test = [x + 10 for x in [3,2,5,8,4]]
    print(test)

def task2_3():
    print("task 3\n")
    test = list(map(lambda x: x *x, [3,2,5,8,4]))
    print(test)


def task2_4():
    test = list(map(lambda x: x * x, [3, 2, 5, 8, 4]))
    min = test[0]
    max = 0
    for i in test:
        if i < min:
            min = i
        elif i > max:
            max = i
    print(min, max)


def task2_5():
    print("task 5\n")
    test = list(map(lambda x: x * x, [3, 2, 5, 8, 4]))
    for i in test:
        if i < 7 :
            print(i, end=" ")


def task2_6():
    print("task 6\n")
    test = list(map(lambda x: x * x, [3, 2, 5, 8, 4]))
    testSorted = sorted(test)
    newList = []
    temp = 0
    for i in range(len(testSorted)-1, 0, -1):
        newList.append(testSorted[i])
    print(newList)


def task2_7():
    print("task 7\n")
    temp = [x // 2 if x % 2 == 0 else x * 2 for x in [42, 3, 4, 18, 3,10]]
    print(temp)


def task2_8():
    print("task 8\n")
    temp = list(filter(lambda x : x > 10, [42, 3, 4, 18, 3,10]))
    print(temp)


def task2_9():
    print("task 9\n")
    test = [*enumerate([42, 3, 4, 18, 3,10])]
    print(test)


def task2__10():
    print("task 10\n")
    first_Name = ["Jean", "Max", "Luc", "Pierre", "Paul"]
    last_Name = ["Dupont", "Durand", "Duchemin", "Ducroc", "Ducastel"]
    magic = list(zip(first_Name, last_Name[::-1]))
    print(magic)
    print(magic[0])
    print(magic[3])
    print(magic[1][0])
    print(magic[0][1])
    print(magic[2])


def task2__11():
    print("task 11\n")
    newList = []
    startTime = time.time()
    for i in range(0, 1000000):
        newList.append(random.randint(0, 100000))
    newList.sort()
    endTime = time.time()
    print(endTime - startTime)

#
def task3_1():
    print("task 1\n")
    student = {
        "name" : "Arthur",
        "academicYear" : 2020
    }
    print(student)

def task3_2():
    print("task 2\n")
    student = {
        "name": "Arthur",
        "academicYear": 2020,
        "units": {
            "name": "Web Development",
            "credits": 5,
            "grade": "F"
        }
    }
    if any(char in student["units"]["grade"] for char in "ABCDE"):
        print("Wrong grade")
    if student["units"]["credits"] <0:
        print("Wrong credits")
    if student["units"]["name"] != "Web Development" or student["units"]["name"] != "Java" or student["units"]["name"] != "Network and System Administration" or student["units"]["name"] != "Computer Architecture":
        print("Wrong name")


def task3_3():
    grade_weight_maping = {
        "A": 4,
        "B": 3,
        "C": 2,
        "D": 1,
        "E": 0
    }
    unit = {
        "name": "Java",
        "credits": 5,
        "grade": "A"
    }
    unit2 = {
        "name": "Math",
        "credits": 5,
        "grade": "B"
    }
    unit3 = {
        "name": "Web Development",
        "credits": 5,
        "grade": "C"
    }
    student = {
        "name": "Arthur",
        "academicYear": 2020,
        "units": [unit, unit2, unit3],
        "total_credits": 0
    }
    for unit_info in student["units"]:
        credits = unit_info["credits"]
        grade = unit_info["grade"]
        weighted_grade = grade_weight_maping.get(grade, 0)  # Use 0 if grade is not found in mapping
        student["total_credits"] += credits * weighted_grade
    print("total credits:",student["total_credits"])
    GPA = student["total_credits"] / sum([unit["credits"] for unit in student["units"]])
    print("GPA:",GPA)


def task3_4():
    grade_weight_mapping = {
        "A": 4,
        "B": 3,
        "C": 2,
        "D": 1,
        "E": 0
    }

    student1 = {
        "name": "Arthur",
        "GPA" : 0,
        "academicYear": 2020,
        "total_credits": 0,
        "units": [
            {"name": "Java", "credits": 5, "grade": "A"},
            {"name": "Math", "credits": 5, "grade": "B"},
            {"name": "Web Development", "credits": 5, "grade": "C"}
        ]
    }

    student2 = {
        "total_credits": 0,
        "name": "Alice",
        "academicYear": 2021,
        "GPA": 0,
        "units": [
            {"name": "Python", "credits": 4, "grade": "B"},
            {"name": "Statistics", "credits": 4, "grade": "A"},
            {"name": "Database", "credits": 3, "grade": "A"}
        ]
    }

    student3 = {
        "total_credits": 0,
        "name": "Bob",
        "GPA": 0,
        "academicYear": 2019,
        "units": [
            {"name": "C++", "credits": 4, "grade": "C"},
            {"name": "Linear Algebra", "credits": 3, "grade": "B"},
            {"name": "Algorithms", "credits": 5, "grade": "A"}
        ]
    }
    students = [student1, student2, student3]
    for student in students:
        for unit_info in student["units"]:
            credits = unit_info["credits"]
            grade = unit_info["grade"]
            weighted_grade = grade_weight_mapping.get(grade, 0)
            student["total_credits"] += credits * weighted_grade
        student["GPA"] = round(student["total_credits"] / sum([unit["credits"] for unit in student["units"]]),1)
        print(student)


def task4_1():
    print("task 1\n")
    list1 =["Arthur", "Alice", "Bob"]
    list2 = ["Arthur", "Patrice", "Bob"]
    for i in list1:
        if i in list2:
            print("Welcome", i)
        else:
            print("Get lost")


def task4_2():
    list1 = ["Arthur", "Alice", "Bob", "Patrice", "Jean", "Luc", "Pierre", "Paul","Arthur", "Alice", "Bob", "Patrice"]
    index = 0
    while index < len(list1):
        item = list1[index]
        if list1.count(item) > 1:
            list1.remove(item)
        else:
            index += 1
    print(list1)
