class rect:
    def __init__(self,length,breath):
        self.lenght = length
        self.breath = breath
    def area(self,lenght,breath):
        return self.lenght*self.breath
    def peri(self,lenght,breath):
        return 2*(lenght+breath)

ob1=rect(12,10)
a=ob1.area(12,10)
b=ob1.peri(12,10)
print(a)
print(b)
