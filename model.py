class Matrix:
    # Costruttore
    def __init__(self, num_rows, num_columns):
        # proprieta' "data"
        self.data = []

        for i in range(num_rows):
            row = []
            for j in range(num_columns):
                number = 0
                row.append(number)
            self.data.append(row)

    # metodi
    def is_regular(self):
        for row in self.data:
            if len(row) != len(self.data[0]):
                return False
        return True

    def set_element(self, row, column, value):
        assert row < len(self.data)
        assert column < len(self.data[0])
        assert value == 1 or value == 2
        self.data[row][column] = value

    def get_element(self, row, column):
        assert row < len(self.data)
        assert column < len(self.data[0])
        return self.data[row][column]

    def get_row(self, n):
        assert n < len(self.data)
        return self.data[n]

    def get_column(self, n):
        assert self.is_regular()
        assert n < len(self.data[0])
        count = 0
        column_list = []
        for element in self.data:
            column_list.append(self.data[count][n])
            count = count + 1
        return column_list

    def get_main_diagonal(self):
        assert self.is_regular()
        count = 0
        diagonal_list = []
        for row in self.data:
            diagonal_list.append(row[count])
            count = count + 1
        return diagonal_list

    def get_antidiagonal(self):
        assert self.is_regular()
        count = len(self.data[0]) - 1
        diagonal_list = []
        for row in self.data:
            diagonal_list.append(row[count])
            count = count - 1
            if count < 0:
                break
        return diagonal_list


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


def get_matrix_main_diagonal(matrix):
    assert is_regular_matrix(matrix)
    count = 0
    diagonal_list = []
    for row in matrix:
        diagonal_list.append(row[count])
        count = count + 1
    return diagonal_list


def get_matrix_antidiagonal(matrix):
    assert is_regular_matrix(matrix)
    count = len(matrix[0]) - 1
    diagonal_list = []
    for row in matrix:
        diagonal_list.append(row[count])
        count = count - 1
        if count < 0:
            break
    return diagonal_list


# ritorna true se tutti gli elementi della lista sono uguali ad n
def all_equal(my_list, n):
    for element in my_list:
        if element != n:
            return False
    return True


def make_matrix(num_rows, num_columns):
    matrix = []
    for i in range(num_rows):
        row = []
        for j in range(num_columns):
            number = 0
            row.append(number)
        matrix.append(row)
    return matrix


def is_winner(matrix, symbol_value):
    # Controllo righe
    num_rows = len(matrix)
    for i in range(num_rows):
        row = get_matrix_row(matrix, i)
        if all_equal(row, symbol_value):
            return True
    # Controllo colonne
    num_columns = len(matrix[0])
    for i in range(num_columns):
        column = get_matrix_column(matrix, i)
        if all_equal(column, symbol_value):
            return True
    # Controllo diagonali
    main_diagonal = get_matrix_main_diagonal(matrix)
    if all_equal(main_diagonal, symbol_value):
        return True
    antidiagonal = get_matrix_antidiagonal(matrix)
    if all_equal(antidiagonal, symbol_value):
        return True
    return False


def matrix_is_all_full(matrix):
    for row in matrix:
        for element in row:
            if element == 0:
                return False
    return True
