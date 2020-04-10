
def insertionSort(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i

        while j > 0 and array[j - 1] > temp:
            array[j] = array[j - 1]
            j -= 1

        array[j] = temp
    return array

array = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]
print(array)
insertionSort(array)
print(array)
