class rectangle:

    def __init__(self,lenght=0,breadth=0):
        self.lenght= lenght
        self.breadth= breadth

    def inputs(self):
        self.lenght=int(input("Enter Length of Rectangle: "))
        self.breadth =int(input("Enter Breadth of Rectangle: "))
    def area(self):
        area = self.lenght * self.breadth
        print("Area of rectangle is :",area)

    def peri(self):
        peri = 2*(self.lenght+self.breadth)
        print("The perimeter of rectangle is : ",peri)


if __name__=="__main__":
    a=rectangle()
    a.inputs()
    a.area()
    a.peri()

