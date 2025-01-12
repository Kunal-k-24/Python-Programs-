def add (x,y):
    return x+y
a1=add(10,20)
print(a1)
def sub (a=10,b=7):
    return a-b
a2=sub()
print(a2)
def prints(*a):
    return a
strs =prints(10,20,30,40,50,60,70)
print(strs)
def prints2(**b):
    return b
strs2=prints2(a=1,b=7,c=8,d=11,f=7)
print(strs2)

def prints3(*a,**b):
    return a,b
str3=prints3(10,20,40,50,80,a=1,b=10,c=9)
print(str3)
def prints4(*a,ab=10,b=77,c=72,d=98):
    return ab,b,c,d,a
strs4=prints4(50,20,30,40,50,60)
print(strs4)
def prints5(ac=22,cd=99,**a):
    return a,ac,cd
strs5=prints5(ab=58,b=67)
print(strs5)
dog= lambda x,y: x+y
sum=dog(10,20)
print(sum)
fog=lambda d,s: d-s
sub=fog(48,68)
print(sub)
log=lambda h,j:h if h>j else j
print(log(23,45))