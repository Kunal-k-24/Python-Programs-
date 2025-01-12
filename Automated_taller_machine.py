userb=10000
userp=7058
ch1='y'
transection_hs=[]


def check(amt):
    userb = amt
    if pin2 == userp:

        while True:

            print('''                                   1.Deposit Money
                                   2.Withdraw Money 
                                   3.Check Balance
                                   4.Transaction History              ''', sep='/n')
            print('Enter Operation You Want to Perform:')
            ch = int(input())
            if ch == 1:
                amt_to_dep = int(input("Enter Amount to Deposit: "))
                userb = userb + amt_to_dep
                print("Amount Deposit Successfully!!", sep='/n')
                transection_hs.append(f"{amt_to_dep} inr was deposited.               Acc Balance : {userb}")


            elif ch == 2:
                print("Enter Amount to Withdraw :", sep='/n/n')
                amt_to_withd = int(input())
                if amt_to_withd > userb:
                    print("Insufficient Balance",sep='/n')
                else:
                    userb = userb - amt_to_withd
                    print("Amount Withdrawn Successful,Collect Your Cash.", sep='/n')
                    transection_hs.append(f"{amt_to_withd} inr was Withdrawn.              Acc Balance : {userb}")
                    print("Do you want to check your balance(y/n)", sep='/n')
                    ch3 = input()
                    if ch3 == 'y':
                        print(f'Current Balance is : {userb}')


            elif ch == 3:
                print(f'Your Current Balance is : {userb}')
                transection_hs.append(f"Checked Acc Balance.                 Acc Balance: {userb}")

            elif ch == 4:
                if len(transection_hs)==0:
                    print("Nothing to Show anything!")
                    print("You did not made any transaction in last 30 days!")
                else:
                    for i in transection_hs:
                        print(i,sep='/n')

            print("")
            print('Do You Want to Perform Another Operation(y/n)')
            che = input()
            if che == 'y':
                continue
            if che == "n":
                break
    else:
        print("Wrong Pin!!")

print("Welcome to Fakir Bank Of India",sep='/n/n/n')
print('Successfully Detected Debit Card Details....',sep='/n')
print("Enter Your Pin: ",sep='/n')
pin2=int(input())
if pin2 == userp:
    while ch1=='y' :

        print('''                            1.Deposit Money
                            2.Withdraw Money 
                            3.Check Balance
                            4.Transaction History              ''',sep='/n')
        print('Enter Operation You Want to Perform:')
        ch=int(input())
        if ch ==1 :
                amt_to_dep=int(input("Enter Amount to Deposit: "))
                userb=userb+amt_to_dep
                print("Amount Deposit Successfully!!",sep='/n')
                transection_hs.append(f"{amt_to_dep} inr was deposited.               Acc Balance : {userb}")


        elif ch == 2 :
                print("Enter Amount to Withdraw :",sep='/n/n')
                amt_to_withd=int(input())
                if amt_to_withd > userb:
                    print("Insufficient Balance", sep='/n')
                elif amt_to_withd<100:
                    print("You can't Withdraw amount less than 100 inr!",sep='/n')
                else:

                    userb = userb - amt_to_withd
                    print("Amount Withdrawed,Collect Your Cash.", sep='/n')
                    transection_hs.append(f"{amt_to_withd} inr was Withdrawn.              Acc Balance : {userb}")
                    print("Do you want to check your balance(y/n)", sep='/n')
                    ch3 = input()
                    if ch3 == 'y':
                        print(f'Current Balance is : {userb}')



        elif ch == 3:
                print(f'Your Current Balance is : {userb}')
                transection_hs.append(f"Checked Acc Balance.                 Acc Balance: {userb}")


        elif ch == 4:
            if len(transection_hs)==0:
                print("Nothing to Show anything!")
                print("You did not made any transaction in last 30 days!")
            else:
                for i in transection_hs:
                    print(i, sep='/n')
                    print("")


        print("")
        print("Do You Want To Perform Another Task(y/n): ")
        ch1=input()
else :
    print("Wrong Pin!!")
    a = 4
    while a>1:
        print(f"You Have {a-1} Attempts Only! ")
        pin2=int(input())
        a=a-1
        if a == 0:
            print("Limit Exceeds You are Blocked !!!")
            break
        if pin2 == userp:
            check(userb)
            break
