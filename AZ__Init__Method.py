class Student:
    def __init__(self):
        self.name = "Ganeswar"
        self.age = 30
        self.pincode = 766001
        self.company = "Hexahealth"
        self.project = "Hexahealth.com"

    def talk(self):
        print("Name-:",self.name)
        print("Age-:",self.age)
        print("Pincode-:",self.pincode)


object1 = Student()
print(object1.name)
print(id(object1))
object2 = Student()
print(object2.name)
print(id(object2))

