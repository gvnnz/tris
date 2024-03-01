def print_matrix(matrix):
    for row in matrix:
        row_string = ""
        for element in row:
            if element == 0:
                row_string = row_string + "* "
            elif element == 1:
                row_string = row_string + "O "
            elif element == 2:
                row_string = row_string + "X "
            else:
                assert False, "Wrong element value: only 0, 1 or 2 allowed"
        print(row_string)
