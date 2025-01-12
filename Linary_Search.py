ls=[]
def linear_search(pan,cake):
    for i in range(len(pan)):
        if (pan[i]==cake):
            return i
    return (-1)
import array as ash
ct=int(input("Enter Count Of List You Want: "))
print(f"Enter Any {ct} Values: ")
for i in range (1,ct+1):
    ls.append(int(input()))
rec=ash.array('i',ls)
element= int(input("Enter Element to Search: "))
rec2=linear_search(rec,element)
if rec2 == -1:
    print("Element Not Found !!")
else :
    print(f"Element {element} is Found at Pos {rec2} .")