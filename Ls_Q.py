def q1():
    list1 = [5, 10, 15, 20, 25, 50, 20]
    lent = len(list1)
    for i in range(lent):
        list1.pop()
    print(list1)


def q2():
    list1 = [5, 10, 15, "ABCD", 20, 25]
    find = list1.index("ABCD", 0)
    if find == "0":
        print("Not in list")
    else:
        print("Element present in the list")


def q3():
    name = ['white', 'brown', 'golden', 'black']
    animal = ['cat', 'dog', 'fish', 'goat']
    age = [1, 2, 2, 6]
    z = zip(name, animal, age)
    for a, b, c in z:
        print(a, b, c, sep='\t')


def q4():
    list1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    list1.pop(0)
    list1.pop(3)
    list1.pop(3)
    print(list1)


def q5():
    list1 = [[], [], []]
    list1[0].append("# # #")
    list1[1].append("# # # # # #")
    list1[2].append("# # # # # # # # #")
    print(list1)


def q6():
    list1 = ['Cat', 'Dog']
    list2 = []
    n = 5
    for i in range(1, n + 1):
        list2.append('cat' + str(i))
        list2.append('dog' + str(i))
    print(list2)


def q7():
    count = 0
    list1 = ['abc', 100, 55, "xyz", 600, True, [88, 195, "pqrs", 335], 667, 'ijk', 699]
    for i in (list1):
        if (isinstance(i, int)):
            if (i == True):
                continue
            else:
                count += 1
        else:
            for a in i:
                if (isinstance(a, int)):
                    if (a == True):
                        continue
                    else:
                        count += 1

    print(count)


def q8():
    list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
    list2 = [[], [], []]
    for i in range(len(list1)):
        list2[i % 3].append(list1[i])
    print(list2)


def q9():
    list1 = [1, 3, 5, 7, 9, 10]
    list2 = [2, 4, 3, 6, 8]
    list3 = []
    list1.pop()
    list3.append(list1 + list2)
    print(list3)


ch = 'y'
while ch != 'n':
    print("Choose Question Number (1-9) : ")
    a = int(input())
    print("")
    if a == 1:
        q1()
    elif a == 2:
        q2()
    elif a == 3:
        q3()
    elif a == 4:
        q4()
    elif a == 5:
        q5()
    elif a == 6:
        q6()
    elif a == 7:
        q7()
    elif a == 8:
        q8()
    elif a == 9:
        q9()
    print("")
    print("Thank You Buddy!")
    print("Do you want to check another answer(y/n):")
    ch = input()