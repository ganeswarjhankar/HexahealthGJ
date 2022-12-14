class Employee:
    '''Doc string description'''
    def __init__(self,ename,eno,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
    def info(self):
        print('*%%%%'*20)
        print('Employee number',self.eno)
        print('Employee name',self.ename)
        print("employee salary",self.esal)
        print("Employee Address",self.eaddr)
        print('*%%%%%%%%%%%%%%%'*20)

E1 = Employee(100,'Durga',10000,'Gurgaon')
E2 = Employee(1000,'Gan',101000,'Gurgon')
E1.info()
E2.info()
