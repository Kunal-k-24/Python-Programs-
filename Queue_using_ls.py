que=[]
while True:
    print("")
    print("Select Any Operation..")
    print("         1 - ENQUEUE Operation")
    print("         2 - DEQUEUE Operation")
    print("         3 - Display Operation ")
    print("         4 - Exit")
    print("")
    ch=int(input())
    if ch == 1 :
        print("Enter Element you want to ENQUEUE: ",sep='/n')
        ele=int(input())
        que.append(ele)
        print("Element ENQUEUED into Queue !",sep='/n')
        print("")
        continue
    elif ch == 2:
        if len(que)==0:
            print("Queue Underflow!")
            print("")
        else:
            print(f"Element {que[0]} DEQUEUED...")
            que.pop(0)
            print("")
        continue
    elif ch == 3:
        if len(que)==0:
          print("Queue is Empty !",sep='/n')
          print("")
        else:
            print("Queue Contains...")
            print("")
            for i in reversed(range(len(que))):
                print(que[i])
    elif ch == 4:
        break

    else :
        print("Invalid Input Try Again !")
        print("")
        continue