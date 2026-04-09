nums = [1, 2, 3, 2, 2, 1 ,4 ,3 ,2 ,4, 1, 2, 4, 3 ,2 ,3,1 ,2 ,4 ,2, 1]
stringy = "abhishekabhishekabhishekabhsiehkabhishekabhishekabhishekabhishek"
listy = ["abc", "bcd", "abc", 123, "cde"]
def remove_duplicates_number(entry):
    # Using set
    distinct = list(set(entry))
    print(distinct)

    # using loop
    unique = []
    for num in entry:
        if num not in unique:
            unique.append(num)
    print(unique)
remove_duplicates_number(nums)

# Removing duplicates from string
def remove_duplicates_string(into):
    # using fromkeys()
    result = "".join(dict.fromkeys(into))
    print(result, "using fromkeys")

    # using loop
    empty = ""
    for abc in into:
        if abc not in empty:
            empty += abc
    print(empty, "Using Loop")
remove_duplicates_string(stringy)

# removing duplicates from list of items
def remove_duplicates_list(param):
    only = list(dict.fromkeys(param))
    print(only, "using fromkeys")
remove_duplicates_list(listy)

qwe = "qaws uwishiu asoxkm"
aws = qwe.split(" ", 2)
print(aws)