def sort(ls):
    low, high = 0, len(ls) - 1
    while low <= high:
        if ls[low] == 'R':
            low += 1
        else:
            ls[low], ls[high] = ls[high], ls[low]
            high -= 1
    return ls

ls = ['G', 'R', 'R', 'G', 'R']
print(sort(ls))
