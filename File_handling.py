import random as omkar

def add_new_stud():
    name = input("Enter Student Name : ")
    mob = input("Enter Mobile Number : ")
    if len(mob)!=10:
        print("Enter Valid Number(Should be 10 digits!)")
        name = input("Enter Valid Mobile Number: ")
    email = input("Enter Email-Address : ")
    print("Generating Enrollment Number.......")
    raw_enr=omkar.randint(23510920,235109200584)
    raw_enr="KNT-"+str(raw_enr)
    print("Your Enrollment Number is : ",raw_enr)
    print("")
    fobj=open("Stud_info.txt","a")
    fobj.write(name+","+mob+","+email+","+raw_enr+'\n')
    fobj.close()
    print("")
    print("Student Registration Successful")
    print("")
def print_info():
    # accept enrollment number and search information
    # of that student in file and print it.
    pass

def delete_stud():
    # accept enrollment number and delete details of
    # that student from file.
    pass

while True:
    print("Select Operation")
    print("1 - Add New Student Record")
    print("2 - Print Student Information")
    print("3 - Delete Student Record")
    print("4 - Exit")
    ch = int(input("Provide your choice : "))

    if ch==1: add_new_stud()
    elif ch==2: print_info()
    elif ch==3: delete_stud()
    elif ch==4: exit(0)
