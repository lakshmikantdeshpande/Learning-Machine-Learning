matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

print(matrix)

print("Normal way to find transpose: \n")
transpose = []
for i in range(len(matrix[0])):
    new_row = []
    for row in matrix:
        new_row.append(row[i])
    transpose.append(new_row)

print(transpose)

print("List comprehension way: \n")

transpose = [ [row[i] for row in matrix] for i in range(len(matrix[0])) ]
print(transpose)
