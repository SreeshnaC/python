class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
    def compare(self,other):
        if self.area == other.area:
            print ("rectangles have same area")
        else:
            print ("rectangles have different area")
    def display(self):
        print(self.length)
        print(self.breadth)
l1=int(input("Enter length 1:"))
b1=int(input("Enter breadth 1:"))
r1=Rectangle(l1,b1)
print("area of r1:",r1.area())
l2=int(input("Enter length 2:"))
b2=int(input("Enter breadth 2:"))
r2=Rectangle(l2,b2)
print("area of r2:",r2.area())
print(r1.compare(r2))