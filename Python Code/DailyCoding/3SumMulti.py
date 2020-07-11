'''
Given an integer array A, and an integer target, return the number of tuples i, j, k  such that i < j < k and A[i] + A[j] + A[k] == target.

As the answer can be very large, return it modulo 10^9 + 7.



Example 1:

Input: A = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation:
Enumerating by the values (A[i], A[j], A[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.
'''

import collections
import itertools

def three_sum_multi(nums, target):
    count = collections.Counter(nums)
    result = 0
    for i, j in itertools.combinations_with_replacement(count, 2):
        k = target - i - j
        if i == j == k:
            result += count[i] * (count[i] - 1) * (count[i] - 2) // 6
        elif i == j != k:
            result += count[i] * (count[i] - 1) // 2 * count[k]
        elif max(i, j) < k:
            result += count[i] * count[j] * count[k]
    return result % (10**9 + 7)


nums = [1,1,2,2,3,3,4,4,5,5]
target = 8
print(three_sum_multi(nums, target))
