sets={"saket",225,True,26,"Dhananjay"}
def q1():
    for i in sets:
        print(i,sep='/n')

def q2():
    sets.add(22)
    print("Member Added Successfully!")
    print(sets)

def q3():
    a=sets.pop()
    print(f"{a} Item Removed !")

def q4():
    sets.discard(26.88)
    print(sets)

def q5():
    lent=len(sets)
    print(lent)

def q6():

    sm_ele=None
    mx_ele=None
    for element in sets:
        if isinstance(element,int)and element is not True and element is not False:
            if sm_ele is None or element <sm_ele:
                sm_ele=element
            if mx_ele is None or element>mx_ele:
                mx_ele=element
    if mx_ele is not None and sm_ele is not None:
        print(f"Smallest Element is {sm_ele}")
        print(f"Largest Element is {mx_ele}")
    else:
        print("There is no integer value in given set!")

def q7():
    sets.clear()
    print(sets)

def q8():
    element=26
    if element in sets:
        print("Element Present in the set!!")
    else:
        print("Element is not present in set!!")

                                     #Assignment 2

def q11():
    set1 = {10, 20, 30, 40}
    set2 = {20, 40, 50}
    a= set1.difference(set2)
    print(a)

def q12():
    set1 = {10, 20, 30, 40, 50}
    for i in range (3):
        set1.discard(10)
        set1.discard(20)
        set1.discard(30)
    print(set1)

def q13():
    set1 = {10, 20, 30, 40, 50}
    set2 = {60, 70, 80, 90, 10}
    rec= set1.intersection(set2)
    print(rec)

def q14():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    roll=set1.symmetric_difference(set2)
    print(roll)

def q15():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    reo=set1.difference(set2)
    for i in reo:
        set1.remove(i)
    print(set1)

def q16():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    reo = set1.intersection(set2)
    print(reo)
    print(type(reo))

def q17():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    orc=set1.union(set2)
    print(orc)



# Two Assignment Complited !!