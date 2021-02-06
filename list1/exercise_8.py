matrix = [[1,2,3,4,5,6],
          [1,2,3,4,5,6],
          [1,2,3,4,5,6],
          [1,2,3,9,5,6],
          [1,2,3,4,5,6],
          [1,2,3,4,5,6]]

# matrix = input_matrix()

matrix_as_list = [num for line in matrix for num in line]
print(max(matrix_as_list))
