'''
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
'''
from collections import Counter
def single_number(nums):
    my_count = Counter(nums)
    for i in my_count:
        if my_count[i] == 1:
            return i
    return -1

nums = [0,1,0,1,0,1,99]
print(single_number(nums))
