'''2) 	Input the digits of square matrix [of order that is input by the user] and sort the non-boundary elements of the matrix.
Also find the sum of diagonal elements of the matrix after sorting.'''


def sort_non_boundary(matrix):
    non_boundary_elements = [matrix[i][j] for i in range(1, len(matrix)-1) for j in range(1, len(matrix)-1)]
    non_boundary_elements.sort()
    k = 0
    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix)-1):
            matrix[i][j] = non_boundary_elements[k]
            k += 1

def diagonal_sum(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))

order = int(input("Enter the Order: "))
print("Enter the Matrix:")
matrix = [list(map(int, input().split())) for _ in range(order)]

sort_non_boundary(matrix)

print("\nSorted Matrix:")
for row in matrix:
    print(" ".join(map(str, row)))

print("Sum of Diagonals:", diagonal_sum(matrix))