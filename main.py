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


def get_current_player(turn_counter, player_1, player_2):
    if turn_counter % 2 == 0:
        return player_1
    return player_2


# -----------------------------------------------------------------------------------------------

matrix = model.Matrix(3, 3)

random_X = random.randint(0, (matrix.count_rows() - 1))
random_Y = random.randint(0, (matrix.count_columns() - 1))
random_Z = random.randint(0, (matrix.count_rows() - 1))
random_K = random.randint(0, (matrix.count_columns() - 1))


matrix.set_element(random_X, random_Y, 1)
matrix.set_element(random_Z, random_K, 2)


player_1_name = input("Player 1: insert your name, then press enter: ")
player_2_name = input("Player 2: insert your name, then press enter: ")

player_1 = model.Player(player_1_name, 1)
player_2 = model.Player(player_2_name, 2)

view.print_matrix(matrix)

"""
Prima di iniziare il gioco si sceglie a random il giocatore che deve iniziare, 
randomizzando il contatore. TODO - rendere questa feature configurabile (#28).
"""
turn_counter = random.randint(0, 1)
while True:
    current_player = get_current_player(turn_counter, player_1, player_2)

    input_string = sanitize_input(
        input(current_player.name + " insert the coordinates: ")
    )
    if input_string == "q":
        break  # vvvv
    if is_valid_input(input_string, matrix) == False:
        print("Invalid input!!!")
        continue
    input_tuple = parse_input(input_string, matrix)
    if matrix.is_element_zero(input_tuple[0], input_tuple[1]) == False:
        print("Alredy insert. Select another coordinates")
        continue
    matrix.set_element(input_tuple[0], input_tuple[1], current_player.symbol_value)
    turn_counter = turn_counter + 1
    view.print_matrix(matrix)
    if model.is_winner(matrix, player_1.symbol_value):
        print(player_1.name + " WIN!!!")
        break
    elif model.is_winner(matrix, player_2.symbol_value):
        print(player_2.name + " WIN!!!")
        break
    elif model.matrix_is_all_full(matrix):
        print("DRAW")
        break
