class Example:
    def __init__(self):
        self.x = 10
        self._y = 50
        self.__z = 64

#_single underscore is partially private and sake of developer
    def public_method(self):

        print(self.x)
        print(self._y)
        print(self.__z)
        
s = Example()

print(s._y)
print(s.x)
print(s.__z)

