abc = "Abhishek Chand, learning python"
bcd = "never to late for learning new things"
efg = "Abhishek Chand"
print(len(abc))

print(abc[0:8]) #print substring last digit index is excluded
print(abc+" "+bcd)

print(efg in abc) #in check wheather one string is present in another string

#string splitting
variable = abc.split(",")
print(variable)
print(variable[0])

#trimming string
str1 = "    learning python is easy needs consistency    "
print(str1)
print(str1.strip())# remove both left and right extra space from string
print(str1.lstrip())# remove only left side
print(str1.rstrip())# remove spaces from right side


