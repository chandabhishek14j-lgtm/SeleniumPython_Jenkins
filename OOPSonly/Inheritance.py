# Inheritance in python : Aquiring all your properties from parent class example parent is Constructor.PY

from Constructor import Calculator

class InheritFromConstructor(Calculator):

    def __init__(self):
        Calculator.__init__(self, 8, 9, 10)

    def getAllData(self):
        return self.num+self.num1+self.num3

obj = InheritFromConstructor()
print(obj.getAllData(),"#####")