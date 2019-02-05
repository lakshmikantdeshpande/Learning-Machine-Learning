from functools import reduce

def square(n):
    return n ** 2

def positive_filter(n):
    return n if n > 0 else None

def summation(x, y):
    return x + y


lst = list(range(-3, 3))
print("Original list is: ", lst)

print("MAP: ", list(map(square, lst)))
print("FILTER: ", list(filter(positive_filter, lst)))
print("REDUCE: ", reduce(summation, lst))

