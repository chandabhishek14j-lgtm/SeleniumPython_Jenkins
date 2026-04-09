# FREQUENCY OF LIST ELEMENTS
sample = [1, 2, 1, 4, 5, 3, 6, 5, 4, 6, 7, 5, 45 ,34, 34 ,2, 23, 34, 67, 9]
dictionary = {}
for i in sample:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i]=1
print(dictionary)

# Using count
for item in sample:
    print(f"{item} >> {sample.count(item)}")