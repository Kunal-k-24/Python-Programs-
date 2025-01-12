def q1():
    ls1= [1, "hello", 3.14, True, None]
    tup1= (42, "world", 2.718, False, [1, 2, 3])
    ls1.append("new element")
    ls1.append(99)
    ls1.append([4, 5, 6])

    def prints(ls1,tup1):
        print("\nItems in List With There Types:\n")
        for i in ls1:
            print(f"{i} : {type(i)}")
        print("\nItems in Tuple With There Types:\n")
        for j in tup1:
            print(f"{j} : {type(j)}")
    prints(ls1,tup1)

def q2():
    def process_fp(fp):
        if isinstance(fp, list):
            return tuple(fp)
        elif isinstance(fp, tuple):
            return sorted(fp)
        elif isinstance(fp, str):
            return fp[::-1]
        elif isinstance(fp, bool):
            return not fp
        elif isinstance(fp, (int, float)):
            return fp ** 2
        else:
            print("Invalid Input !!")

def q3():
    ok= {0: 10, 1: 20}
    ok.update({2:30})
    print(ok)

def q4():
    dict1 = {1: 10, 2: 20}
    dict2 = {3: 30, 4: 40}
    dict3 = {5: 50, 6: 60}
    dict4={}
    dict4=dict1.copy()
    dict4.update(dict2)
    dict4.update(dict3)
    print(dict4)

def q5():
    dict1 = {"one": 10, "two": 20, "three": 30, "four": 40, "five": 50, "six": 60}
    for i in dict1:
        print(i,dict1[i])

def q6():
    dict1 = {"one": 10, "two": 20, "three": 30, "four": 40, "five": 50, "six": 60}
    a= list(dict1.keys())
    ind=0
    while True :
        a=a[ind]
        val=dict1[ind]
        print(f"{a} : {val}")
        ind=ind+1
q6()





