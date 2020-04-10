def minesweeper(bombs, rows, columns):
    new_array = [[0 for i in range(rows + 1)] for j in range(columns + 1)]
    for b in bombs:
        row_index = b[0]
        column_index = b[1]
        new_array[row_index][column_index] = -1
        for i in range(row_index - 1, row_index + 2):
            for j in range(column_index - 1, column_index + 2):
                if 0 <= i < rows and 0 <= j < columns and new_array[i][j] != -1:
                    new_array[i][j] += 1
        return new_array

field1 = [[0, 0, 0, 0, 0],
          [0, 1, 1, 1, 0],
          [0, 1, -1, 1, 0]]

print(minesweeper(field1, 3, 5))
