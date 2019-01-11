array = list(range(55))

n = int(input("Enter a number to search: "))
hops = 0
i = 0
j = len(array) - 1
found = False

while i <= j:
    index = int(i + ((j - i) / 2))
    print("Index: ", index)
    if n == array[index]:
        found = True
        hops += 1
        break;
    elif n < array[index]:
        j = index - 1
    else:
        i = index + 1
    hops += 1


if found:
    print("Found ", array[index], " in ", hops, " hops")
else: 
    print(n, " not found in the array")
