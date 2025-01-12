st=[]
while True:
    print("")
    print("Select Any Operation..")
    print("         1 - PUSH Operation")
    print("         2 - POP Operation")
    print("         3 - Display Operation ")
    print("         4 - Exit")
    print("")
    ch=int(input())
    if ch == 1 :
        print("Enter Element you want to Push: ",sep='/n')
        ele=int(input())
        st.append(ele)
        print("Element Pushed into Stack !",sep='/n')
        print("")
        continue
    elif ch == 2:
        if len(st)==0:
            print("Stack Underflow!")
            print("")
        else:
            print(f"Top Element {st[-1]} Poped Out..")
            st.pop()
            print("")
        continue
    elif ch == 3:
        if len(st)==0:
          print("Stack is Empty !",sep='/n')
          print("")
        else:
            print("Stack Contains...") 
            print("")
            for i in reversed (range(len(st))):
                print(st[i])
    elif ch == 4:
        break

    else :
        print("Invalid Input Try Again !")
        print("")
        continue