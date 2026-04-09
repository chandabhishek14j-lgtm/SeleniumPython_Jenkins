# find common elements between two lists
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
c = []
for item in a:
    if item in b:
        c.append(item)
print(c)

# using set
d = list(set(a)&set(b))
print(d)

