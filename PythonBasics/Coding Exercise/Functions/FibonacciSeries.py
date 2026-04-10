def fibonacci(num):
    a, b =0, 1
    result = []
    for i in range(num):
        result.append(a)
        a = b
        b = a + b
    print(result)

fibonacci(10)