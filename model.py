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
    def count_rows(self):
        return len(self.data)

    def count_columns(self):
        return len(self.data[0])

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

    def if_value_is_not_zero(self, row, column, value):
        if self.data[row][column] == 1 or self.data[row][column] == 2:
            return True

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


# ritorna true se tutti gli elementi della lista sono uguali ad n
def all_equal(my_list, n):
    for element in my_list:
        if element != n:
            return False
    return True


def is_winner(matrix, symbol_value):
    # Controllo righe
    num_rows = matrix.count_rows()
    for i in range(num_rows):
        row = matrix.get_row(i)
        if all_equal(row, symbol_value):
            return True
    # Controllo colonne
    num_columns = matrix.count_columns()
    for i in range(num_columns):
        column = matrix.get_column(i)
        if all_equal(column, symbol_value):
            return True
    # Controllo diagonali
    main_diagonal = matrix.get_main_diagonal()
    if all_equal(main_diagonal, symbol_value):
        return True
    antidiagonal = matrix.get_antidiagonal()
    if all_equal(antidiagonal, symbol_value):
        return True
    return False


def matrix_is_all_full(matrix):
    for row in matrix.data:
        for element in row:
            if element == 0:
                return False
    return True
