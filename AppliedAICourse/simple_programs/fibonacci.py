def fibonacci(num):
    return num if num <= 1 else fibonacci(num - 1) + fibonacci(num - 2)

for i in range(10):
    print(fibonacci(i))
