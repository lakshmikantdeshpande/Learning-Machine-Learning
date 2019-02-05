import math


def search(array, i, j, n):
    if i > j:
        return -1

    mid = int(i + ((j - i) / 2))

    if n == array[mid]:
        return mid
    elif n < array[mid]:
        return search(array, i, mid - 1, n)
    else:
        return search(array, mid + 1, j, n)


array = list(range(1, 51))
num = int(input("Enter a number <50 to search: "))
result = search(array, 0, len(array) - 1, num)
if result == -1:
    print("Number not found")
else:
    print("Number found :D")

