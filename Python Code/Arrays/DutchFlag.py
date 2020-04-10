def sort(ls):
    low, mid, high = 0, 0, len(ls) - 1

    while mid <= high:
        if ls[mid] == 'R':
            ls[low], ls[mid] = ls[mid], ls[low]
            low += 1
            mid += 1
        elif ls[mid] == 'G':
            mid += 1
        else:
            ls[mid], ls[high] = ls[high], ls[mid]
            high -= 1
    return ls

ls = ['R','B', 'G', 'R','B', 'G', 'R','B', 'G']
print(sort(ls))
