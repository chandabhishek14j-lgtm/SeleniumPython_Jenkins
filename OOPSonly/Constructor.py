# classes are user defined blueprint or prototype of what are
# different operation those particular classes perform
#functions inside a class is called methods

# class with have methods, class variable, instance variables or constructors

# keyword class name is used for class
"""creating a calculator"""
class Example:
    num = 100

    def __init__(self):
        print("Called Automatically when object is created")

    def getData(self):
        print("Executing as method in class")

obj = Example() #syntax to create an object
obj.getData()
print(obj.num)

# Constructor
"""
it is an object in a class that is called automatically
__init__ defines the constructor
#syntax : def __init__(self):
"""

# variables inside class are class variable and variables inside Constructor are ins variable
# instance variable are different for different objects

"""How to send parameters from object to class"""
# self keyword in mandatory to call variables inside class
class Calculator:
    num = 10

    def __init__(self, a, b, c):
        self.num1 = a
        self.num2 = b
        self.num3 = c

    def summation(self):
        return self.num1+self.num2+Calculator.num

"""
obje = Calculator(2, 3)
obje1 = Calculator(4, 5)

print(obje.summation())
print(obje1.summation())

"""




