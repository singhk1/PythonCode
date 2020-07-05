'''
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:

1 is typically treated as an ugly number.
n does not exceed 1690.
'''

def ugly_number2(n):
    arr = [1]
    p2 = p3 = p5 = 0
    while len(arr) != n:
        num = min(2 * arr[p2], 3 * arr[p3], 5 * arr[p5])
        arr.append(num)
        if 2 * arr[p2] == num:
            p2 += 1
        if 3 * arr[p3] == num:
            p3 += 1
        if 5 * arr[p5] == num:
            p5 += 1
    return arr[-1]

print(ugly_number2(10))
