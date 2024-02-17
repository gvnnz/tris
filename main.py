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

def sanitize_input(input_string):
    return input_string.strip()


input_string = input("Digita o oppure x seguita dalle coordinate: ")


input_string = sanitize_input(input_string)

print(input_string)
