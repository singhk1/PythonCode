def count_digits(num):
    count = 0
    num = abs(num)
    while num > 0:
        num //= 10
        count += 1
    return count


num = -123
print(count_digits(num))
