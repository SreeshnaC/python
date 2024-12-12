class Student:
    tutor="Bindumiss"
    def __init__(self, name,age):
        self.name=name
        self.age=age


    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False


    def display(self):
        print(self.name)
        print(self.age)
        print(self.__class__.tutor)

s1=Student("Thahi",21)
s1.display()
s2=Student("Dishna",21)
s2.display()
s3=s1.compare(s2)
print(s3)