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
