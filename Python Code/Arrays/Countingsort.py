def countingsort(ls, digit, base = 10):
    counts = [[] for _ in range(base)]
    for num in ls:
        d = (num // base ** digit) % base
        counts[d].append(num)
    #print(counts)
    result = []
    for bucket in counts:
        result.extend(bucket)
    return result

def radixsort(ls, digits = 3):
    for digit in range(digits):
        ls = countingsort(ls, digit)
    return ls

ls = [4, 100, 54, 537, 2, 89]
ls1 = [4, 2]
print(countingsort(ls1, 2))
#print(radixsort(ls))
