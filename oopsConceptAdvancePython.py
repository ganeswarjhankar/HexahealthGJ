class Employee:
    '''Doc string or the Description part of the '''
    def __init__(self,eno,ename,esal,eaddress):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddress = eaddress
    def info(self):
        print("employee Number:",eno)
        print("Employee Name:",ename)
        print("Employee salary:",esal)
        print("Employee address:",eaddress)

E1 = Employee(10,"Ganeswar",100,"Gurugram")
E2 = Employee(11,"anes",200,"gram")

