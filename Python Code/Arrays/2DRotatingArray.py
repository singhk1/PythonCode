def rotate(arr, n):
    arr_new = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            (new_i, new_j) = rotate_sub(i, j, n)
            arr_new[new_i][new_j] = arr[i][j]
    return arr_new


def rotate_sub(i, j, n):
    return j, n - 1 - i

def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'

arr = [[1,2,3],[4,5,6],[7,8,9]]
print(to_string(rotate(arr,3)))
