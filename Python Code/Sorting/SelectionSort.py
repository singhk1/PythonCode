
def swap(array, start, end):
    temp = array[start]
    array[start] = array[end]
    array[end] = temp


def selectionSort(array):
    for i in range(len(array)):
        min = i
        for j in range(i + 1, len(array)):
            if array[min] > array[j]:
                min = j
        swap(array, min, i)
    return array

array = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]
print(array)
selectionSort(array)
print(array)
