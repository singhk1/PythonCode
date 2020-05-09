'''
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice.
Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
'''
from collections import Counter
def single_number(nums):
    my_count = Counter(nums)
    count = []

    for i in my_count:
        if my_count[i] == 1:
            count.append(i)
    return count

nums = [1,2,1,3,2,5]
print(single_number(nums))
