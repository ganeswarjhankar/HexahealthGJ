class Student:
    def __init__(self):
        self.name = 'Ganeswar'
        self.age = 20
        self.address = "GJ address"
        self.pincode = 122001
        self.lanenumber = "lane20"
        print("__intit__ is calling the init Function ")

    def talk(self):
        print("Name-",self.name)
        print("Age-",self.age)
        print("Address-",self.address)
        print("Pincode-",self.pincode)
        print("LaneNumber-",self.lanenumber)
v1 = Student()
v1.pincode= "00000"
v1.age = 12.3
print(v1.pincode)
print(v1.age)

v2 = Student()
print(v2.pincode)
print(v2.age)
v3 = Student()
print(v3.pincode)
print(v3.age)





