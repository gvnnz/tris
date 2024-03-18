import model
import view
from random import randint

matrix = model.Matrix(3, 3)

random_X = randint(0, (matrix.count_rows() - 1))
random_Y = randint(0, (matrix.count_columns() - 1))
random_Z = randint(0, (matrix.count_rows() - 1))
random_K = randint(0, (matrix.count_columns() - 1))


def is_valid_input(input_string, matrix):
    if len(input_string) != 2:
        return False
    if input_string[0].isdigit() == False or input_string[1].isdigit() == False:
        return False
    if (
        int(input_string[0]) >= 0
        and int(input_string[0]) < matrix.count_rows()
        and int(input_string[1]) >= 0
        and int(input_string[1]) < matrix.count_columns()
    ):
        return True
    return False


def parse_input(input_string, matrix):
    assert is_valid_input(input_string, matrix)
    row_value = int(input_string[0])
    column_value = int(input_string[1])

    return (row_value, column_value)


def sanitize_input(input_string):
    return input_string.strip()


# -----------------------------------------------------------------------------------------------

player_1 = input("Player 1: insert your name, then press enter: ")
player_2 = input("Player 2: insert your name, then press enter: ")

count = 0
while True:
    if count % 2 == 0:
        symbol_value = 1
    if count % 2 == 1:
        symbol_value = 2
    if count == 0:
        input_string = str(random_X) + str(random_Y)
    if count == 1:
        input_string = str(random_Z) + str(random_K)
    if count > 1:
        if count % 2 == 0:
            input_string = sanitize_input(input(player_1 + " insert the coordinates: "))
        else:
            input_string = sanitize_input(input(player_2 + " insert the coordinates: "))
    if input_string == "q":
        break  # vvvv
    if is_valid_input(input_string, matrix) == False:
        print("Invalid input!!!")
        continue
    input_tuple = parse_input(input_string, matrix)
    if matrix.is_element_zero(input_tuple[0], input_tuple[1]) == False and count != 1:
        print("Alredy insert. Select another coordinates")
        continue
    matrix.set_element(input_tuple[0], input_tuple[1], symbol_value)  # chiedere
    count = count + 1
    view.print_matrix(matrix)
    if model.is_winner(matrix, 1):
        print(player_1 + " WIN!!!")
        break
    elif model.is_winner(matrix, 2):
        print(player_2 + " WIN!!!")
        break
    elif model.matrix_is_all_full(matrix):
        print("DRAW")
        break
