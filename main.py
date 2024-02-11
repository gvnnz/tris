import model

matrix = [[0, 0, 0], [1, 0, 0], [0, 1, 0]]


def sanitize_input(input_string):
    return input_string.strip()


input_string = input("Digita o oppure x seguita dalle coordinate: ")


input_string = sanitize_input(input_string)

print(input_string)
