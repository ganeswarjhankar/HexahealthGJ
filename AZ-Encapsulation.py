class Speed:
    def __init__(self):
        self.speed = 10
        self.__new_speed = 88
    def get_new_speed(self):
        return self.__new_speed
    def set_new_speed(self,new_speed):
        self.__new_speed = new_speed



##Getter and setter Concepts are here .

s1 = Speed()
s1.speed=100
s1.set_new_speed(12)

print(s1.get_new_speed())



