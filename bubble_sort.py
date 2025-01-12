ls=[]
def bubble_sort(sid):
    n=len(sid)
    for i in range (n):
        for j in range(n-1-i):
            if(sid[j]>sid[j+1]):
                temp=sid[j]
                sid[j]=sid[j+1]
                sid[j+1]=temp

import array as pandit
a=int(input("Enter Count Of List You Want: "))
print(f"Enter Any {a} Values: ")
for i in range (1,a+1):
    ls.append(int(input()))
sid=pandit.array('i',ls)
print("Array Before Sort: ",sid)
bubble_sort(sid)
print("Array After Sort: ",sid)