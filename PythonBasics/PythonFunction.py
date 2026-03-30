# Function is a group of related statements that perform any specific task
# syntax: def function_name()
# def greeting():
#     print("What is your name?")
#     p = str(input())
#     if type(p)==str:
#         print("Hello", p, ", very nice to meet you!")
#
# greeting()

def greetMe(name):
    print("Hello", name, ", very nice to meet you!")

greetMe("Chand")

# it = 4
# if it==4:
#     greeting()
# else:print("wuhoooo")

def addNumbers(a,b):
    print(a+b)
addNumbers(2,3.1)

def addinteger(c,d):
    return c+d
print(addinteger(2,3))