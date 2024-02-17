import model

matrix = [[0, 0, 0], [1, 0, 0], [0, 1, 0]]

def is_valid_input(input_string, matrix):
    if len(input_string) != 3:
        return False
    if input_string[0] != "o" and input_string[0] != "x":
        return False
    if input_string[1].isdigit() == False or input_string[2].isdigit() == False:
        return False
    if (
        int(input_string[1]) >= 0
        and int(input_string[1]) < len(matrix)
        and int(input_string[2]) >= 0
        and int(input_string[2]) < len(matrix[0])
    ):
        return True
    else:
        return False


def parse_input(input_string, matrix):
    assert is_valid_input(input_string, matrix)
    symbol_value = 2 if input_string[0] == "x" else 1
    row_value = int(input_string[1])
    column_value = int(input_string[2])

    return (symbol_value, row_value, column_value)


def sanitize_input(input_string):
    return input_string.strip()


input_string = input("Digita o oppure x seguita dalle coordinate: ")


input_string = sanitize_input(input_string)

print(input_string)
