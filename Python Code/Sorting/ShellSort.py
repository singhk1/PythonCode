

def shellSort(array):
    count = len(array) // 2

    while count:
        for i, el in enumerate(array[count:], count):
            while i >= count and array[i - count] > el:
                array[i] = array[i - count]
                i -= count
            array[i] = el
        count = 1 if count == 2 else count * 5 // 11

array = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]
print(array)
shellSort(array)
print(array)
