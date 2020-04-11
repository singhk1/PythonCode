def longest(n):
    n = bin(n)[2:]
    max_len = curr_len = 0
    for i in n:
        if i == '1':
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 0
    return max_len


def longest_bit_manipulation(n):
    max_len = 0

    while n:
        max_len += 1
        n = n & (n << 1)
    return max_len

num = 3
num1 = 156
print(longest(num))
print(longest(num1))
print(longest_bit_manipulation(num))
print(longest_bit_manipulation(num1))
