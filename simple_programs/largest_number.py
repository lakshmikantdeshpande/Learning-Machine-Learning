import sys
from random import shuffle

max = -sys.maxsize
array = list(range(55))
shuffle(array)
print("The array is: ", array)

for i in array:
    if i > max:
        max = i

print("Maximum number is ", max)
