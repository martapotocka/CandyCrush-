from random import randint


def candy(num_of_rows, num_of_columns, num_of_colors):
    matrix = [[None for _ in range(num_of_rows)] for _ in range(num_of_columns)]

    for row in range(num_of_rows):
        for col in range(num_of_columns):
            avoided_row = None
            avoided_col = None
            if col < 2 and row < 2:
                matrix[row][col] = find_random_color(num_of_colors)
            else:
                found_color = find_random_color(num_of_colors)
                if col >= 2:
                    avoided_row = check_cells_behind(matrix, row, col)
                if row >= 2:
                    avoided_col = check_columns_above(matrix, row, col)
                while found_color == avoided_row or found_color == avoided_col:
                    found_color = find_random_color(num_of_colors)

                matrix[row][col] = found_color
    return matrix


def find_random_color(C):
    return randint(1, C)


def check_cells_behind(matrix, row, column):
    if matrix[row][column - 1] == matrix[row][column - 2]:
        return matrix[row][column - 1]
    else:
        return None


def check_columns_above(matrix, row, column):
    if matrix[row - 1][column] == matrix[row - 2][column]:
        return matrix[row - 1][column]
    else:
        return None


C = candy(10, 10, 5)
for i in C:
    print(i)
