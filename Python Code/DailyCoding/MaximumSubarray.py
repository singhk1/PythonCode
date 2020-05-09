'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

def max_subarray(nums):
    if len(nums) == 0:
        return 0
    max_ending = nums[0]
    max_so_far = -float('inf')
    for i in nums:
        max_so_far = max(i, max_so_far + i)
        if max_so_far > max_ending:
            max_ending = max_so_far
    return max_ending

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(nums))
