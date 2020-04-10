def counting_sort(arr, digit):
    counts = [[] for _ in range(10)]

    for num in arr:
        d = (num // 10 ** digit) % 10
        counts[d].append(num)
    result = []

    for bucket in counts:
        result.extend(bucket)
    return result


def radix_sort(arr):
    max_num = max(arr)
    digits = 0
    while max_num > 0:
        digits += 1
        max_num //= 10
    print(digits)
    for digit in range(digits):
        arr = counting_sort(arr, digit)
    return arr

arr = [100]
print(radix_sort(arr))
