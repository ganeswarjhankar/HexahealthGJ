#n = input("Name: ")
#a = int(input("Age: "))
#m = int(input("Marks: "))

class Student:
    def __init__(self,n,a,**m):
        self.name = n
        self.age =  a
        self.marks = m
    def display(self):
        print("Hi",self.name)
        print("Your age",self.age)
        print("Your marks",self.marks)


s1 = Student("ganeswar",22,sc = 96,eng = 43,odia = 44)
s1.display()
print("-----------------------")


s2 = Student("Jhankar",43,math=23,eng=3,english=32)
s2.display()



