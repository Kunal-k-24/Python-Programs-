from tkinter import *

base = Tk()
base.geometry("300x300")
base.title("First GUI Frame")
base.configure(bg="gray")

def event_method():
    print("hello all")

f1 = ("Arial Bold", 18)
f2 = ("Comic Sans MS", 22)


btn = Button(base, text="Submit", font=f1, fg="yellow", command=event_method)
lb = Label(base, text="Enter Password", font=f2, fg="sky blue")
txt = Entry(base, font=f1, show="*")

btn.place(x=300,y=100)
lb.pack()
txt.pack()

# step 5: showing base
base.mainloop()