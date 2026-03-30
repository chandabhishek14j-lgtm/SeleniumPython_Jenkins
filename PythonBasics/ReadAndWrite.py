obj = open('Text.txt')#this object now have the text file
print(obj.read(1))#read upto specific character
print(obj.read(2))#cpntinue from next
print(obj.read()) #will print all the content
obj.close()
print("************")

obj1 = open('Text.txt')
print(obj1.readline())
print(obj1.readline())
print(obj1.readline())
obj1.close()
print("/************/")
#what if too many lines to print we can use loop with readLine method
file = open('Text.txt')
line = file.readline()

while line != '':
    print(line)
    line = file.readline()

file.close()
print("//********//")

file1 = open('Text.txt')
value = file1.readlines()
print(value)

for line in value:
    print(line)
file1.close()
print("///********///")

#how to write in any file
#this will automatically open and close the file with open('Text.txt', 'r') as file3: in read mode
#this will automatically open and close the file with open('Text.txt', 'w') as file3: in write mode

# before writing
"""
read the file and store all line in ist
then reverse the list 
write the list back to file
"""
with open('Text.txt', 'r') as reader:
    val1 = reader.readlines()
    #reversed(val1)
    print(val1)
    with open('Text.txt', 'w') as writer:
        for line in reversed(val1):
            writer.write(line)

