'''
Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.
For example, for the input [1, 2, 3, 10], you should return 7.
'''

def smallest(nums):
    res = 1
    for i in range(len(nums)):
        if nums[i] > res:
            return res
        else:
            res = res + nums[i]
    return res


nums = [1, 2, 3, 10]
print(smallest(nums))
nums = [1, 2, 3, 4, 13]
print(smallest(nums))
