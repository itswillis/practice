def get_principal_diagonal_sum(matrix):
    return sum([matrix[row][row] for row in range(len(matrix))])

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(get_principal_diagonal_sum(data))
print(get_principal_diagonal_sum([[1, 2],[7, 6]])) 
print(get_principal_diagonal_sum([[3, 5],[2, 6]]))