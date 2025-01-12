import random as shakti
from tkinter import *
j=1
f3=("Arial",16)
f1=("Marvel",24)
f2=("Marvel",48)
base = Tk()
base.geometry("600x600")
base.title("Mahajan Pandit")
def met1(e):
    a=str(e.x)
    b=str(e.y)
    if xcord==a and ycord==b:
        leb.configure(text="You Won!",font=f2)
    else:
      global j
      if j<3:
          leb2.configure(text="You Clicked here " + a + "x" + b+"\n", font=f3)
          j+=1
      elif j==3:
          base.destroy()
xcord = str(shakti.randint(0,600))
ycord = str(shakti.randint(0,600))
leb=Label(base)
leb2=Label(base)
leb3=Label(base)
leb.configure(text="You Have To Archive This Pixel " + xcord + "x" + ycord, font=f3)
leb.pack()
for i in range(1,4):
    leb3.configure(text="You Have "+str(i)+" Chances")
    leb3.place(x=237,y=511)
leb2.pack()
base.bind("<Button>",met1)
base.mainloop()