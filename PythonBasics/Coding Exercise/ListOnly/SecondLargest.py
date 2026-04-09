numList = [1, 4, 3, 5, 2, 5, 4, 3, 6, 7, 9]
uniqueList = []
def second_largest(value):
    # Using loop
    for num in numList:
        if num not in uniqueList:
            uniqueList.append(num)
    uniqueList.sort()
    print(uniqueList[-2])

