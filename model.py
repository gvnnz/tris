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
                row_string = row_string + "* "
            elif element == 1:
                row_string = row_string + "O "
            else:
                row_string = row_string + "X "
        print(row_string)


def get_matrix_row(matrix, n):
    assert n < len(matrix)
    return matrix[n]


def get_matrix_column(matrix, n):
    assert is_regular_matrix(matrix)
    assert n < len(matrix[0])
    count = 0
    column_list = []
    for element in matrix:
        column_list.append(matrix[count][n])
        count = count + 1
    return column_list
