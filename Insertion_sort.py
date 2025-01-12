def insertion_sort(jo):
    for i in range (len(jo)):
        key=jo[i]
        j=i-1
        while(j>=0 and key<jo[j]):
            jo[j+1]=jo[j]
            j=j-1
        jo[j+1]=key
        print(jo)
        print("Key is :",key)
import array as new
ls=[]
a=int(input("Enter Count Of List You Want: "))
print(f"Enter Any {a} Values: ")
for i in range (1,a+1):
    ls.append(int(input()))
yo=new.array('i',ls)
print("Values Before Insertion Sort: ",yo)
print("")
insertion_sort(yo)
print("")
print("Values After Insertion Sort: ",yo)