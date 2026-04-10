def find_factorial(num):
    result = 1
    if num != 0:
        for i in range(1, num + 1):
            result *= i
        print(result)
    else:
        result = 1
        print(result)
find_factorial(3)