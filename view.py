def print_matrix(matrix):
    for i in range(matrix.count_rows()):
        row_string = str(i) + " "  # parte con il numero della riga
        row = matrix.get_row(i)
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
    print_coordinate_graph_abscissa(matrix)


def print_coordinate_graph_abscissa(matrix):
    s = ""
    for i in range(matrix.count_columns()):
        s = s + str(i) + " "
    print("  " + s)
