import model
import view

matrix = model.Matrix(3, 3)


def is_valid_input(input_string, matrix):
    if len(input_string) != 3:
        return False
    if input_string[0] != "o" and input_string[0] != "x":
        return False
    if input_string[1].isdigit() == False or input_string[2].isdigit() == False:
        return False
    if (
        int(input_string[1]) >= 0
        and int(input_string[1]) < matrix.count_rows()
        and int(input_string[2]) >= 0
        and int(input_string[2]) < matrix.count_columns()
    ):
        return True
    return False


def parse_input(input_string, matrix):
    assert is_valid_input(input_string, matrix)
    symbol_value = 2 if input_string[0] == "x" else 1
    row_value = int(input_string[1])
    column_value = int(input_string[2])

    return (symbol_value, row_value, column_value)


def sanitize_input(input_string):
    return input_string.strip()


# -----------------------------------------------------------------------------------------------
while True:
    input_string = sanitize_input(input("Digita o oppure x seguita dalle coordinate: "))
    if is_valid_input(input_string, matrix) == False:
        print("Invalid input!!!")
        continue
    input_tuple = parse_input(input_string, matrix)
    matrix.set_element(input_tuple[1], input_tuple[2], input_tuple[0])
    view.print_matrix(matrix)
    if model.is_winner(matrix, 1):
        print("Player 1 WIN!!!")
        break
    elif model.is_winner(matrix, 2):
        print("Player 2 WIN!!!")
        break
    elif model.matrix_is_all_full(matrix):
        print("DRAW")
        break
