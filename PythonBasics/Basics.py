# List basics
# values = [1, 2, "Abhishek", 4]
# print(values[0])
# print(values[-1])
# print(len(values))
# values.insert(3, "Chand")
# print(values)
# print(values[3])
# values.append("Last") # add element to last
# print(values)
# del values[0]
# del values[0]
# del values[-2]
# print(values)

#Tuple Basics :only diff in tuple and list is the Tuple is immutable and can not be changed
val = (1, 2, "Abhishek", "Chand")
print(val)

# Dictionary: These are the key value pairs "HashMap in java"
dic = {1:"Abhishek", "a":"Chand"}
print(dic[1])
print(dic["a"])
print(dic)

# creating dictionary at run time and pass values
BCD = {}
BCD["fistName"] = "Abhishek"
BCD["lastName"] = "Chand"
print(BCD)

# conditional statements
greeting = "Hello Abhishek"
if greeting == "Hello Abhishek":
    print("Condition Matches")
else:
    print("Condition Not Matches")

# for loop
bcd = [1, 2, 3, 4, 5]
for i in bcd:
    print(i)
    print(i*2)

# summ of first 10 numbers
value = 0
for j in range(1, 11): #  in loop range last number from range is excluded
    value = value + j
print("sum of first 10 natural number is:",value)

# jumping index in loop
for k in range(1, 11, 2): #2 is jumping index
    print(k)
print("*************************")
    # now what iff we only set single value in range
for l in range(5): print(l)
#python by default consider the single index as maximum value for range, it will start from 0
print("*************************")
## While Loop checks the condition if the condition is true it will execute if false it will exit

it = 4
while it>=1:
    if it !=3:
        print(it)
    else:
        print("Skipping value is three")
    it = it - 1
print("while loop exit")

# break and continue keywords
jt = 10
while jt > 0:
    if jt ==9:
        jt = jt - 1
        continue

    if jt ==3:
        break
    print(jt)
    jt = jt - 1
print("using break and continue")