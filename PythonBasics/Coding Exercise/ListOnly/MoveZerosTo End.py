# Moving zeroes to end o the list
a = [1, 2, 3, 4, 0, 9, 8, 0, 8, 6, 7]
print(a)
b=[]
z_count = 0
for num in a:
    if num == 0:
        z_count += 1
    else:
        b.append(num)
new_list = b + [0]*z_count
print(new_list)

# Using list comprehension
c = [item for item in a if item!=0]
z = a.count(0)
result = c+[0]*z
print(result)