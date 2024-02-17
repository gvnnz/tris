def is_regular_matrix(matrix):
    for row in matrix:
        if len(row) != len(matrix[0]):
            return False
    return True


def set_matrix_element(matrix, row, column, value):
    assert row < len(matrix)
    assert column < len(matrix[0])
    assert value == 1 or value == 2
    matrix[row][column] = value


# ritorna l'elemento row, column della matrix
def get_matrix_element(matrix, row, column):
    assert row < len(matrix)
    assert column < len(matrix[0])
    return matrix[row][column]


def print_matrix(matrix):
    for row in matrix:
        row_string = ""
        for element in row:
            if element == 0:
                row_string = row_string + "*"
            elif element == 2:
                row_string = row_string + "O"
            else:
                row_string = row_string + "X"
        print(row_string)
