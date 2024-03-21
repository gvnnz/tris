import model
import view
import random


def is_valid_input(input_string, matrix):
    if len(input_string) != 2:
        return False
    row_value = input_string[0]
    column_value = input_string[1]
    if row_value.isdigit() == False or column_value.isdigit() == False:
        return False
    if (
        int(row_value) >= 0
        and int(row_value) < matrix.count_rows()
        and int(column_value) >= 0
        and int(column_value) < matrix.count_columns()
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


def get_current_symbol_value(count):
    if count % 2 == 0:
        return 1
    return 2


# -----------------------------------------------------------------------------------------------

matrix = model.Matrix(3, 3)

random_X = random.randint(0, (matrix.count_rows() - 1))
random_Y = random.randint(0, (matrix.count_columns() - 1))
random_Z = random.randint(0, (matrix.count_rows() - 1))
random_K = random.randint(0, (matrix.count_columns() - 1))


player_1 = input("Player 1: insert your name, then press enter: ")
player_2 = input("Player 2: insert your name, then press enter: ")


count = 0
while True:
    symbol_value = get_current_symbol_value(count)
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
    matrix.set_element(input_tuple[0], input_tuple[1], symbol_value)
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
