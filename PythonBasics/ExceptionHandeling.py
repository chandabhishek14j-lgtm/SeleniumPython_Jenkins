itemsInCart = 0
# operation to put 2 items in cart is performed
"""Raise Exception using assert or raise exception"""
if itemsInCart != 2:
    #raise Exception("Items not matching the supposed item")
    pass
#assertion is also a way to match certain conditions or fail if not matching
assert(itemsInCart == 0)

#try catch for catch we use except instead of catch
"""
when exception is raised in try it will be send to except block
"""

try:
    with open('Texts.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print("File not exist")

#finally is the keyword which oly is used after try catch mechanism and not matter pass or fail it will run
finally:
    print("running finally")

#purpose of finally: if you want anything to happen for sure and do not want exception
#to hinder it we can put it in finally that way it will surely run