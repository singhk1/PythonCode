import sys
def max_sub_Array_CubicSolution(nums):
    n = len(nums)
    maximum = -sys.maxsize -1
    for i in range(n):
        for j in range(i, n):
            winSum = 0
            for k in range(i, j):
                winSum += nums[k]
            maximum = max(maximum, winSum)
    return maximum

def max_sub_Array_QuadraticSolution(nums):
    n = len(nums)
    maximum = -sys.maxsize - 1
    for i in range(n):
        runningWindow = 0
        for j in range(i, n):
            runningWindow += nums[j]
            maximum = max(maximum, runningWindow)
    return maximum

def max_sub_Array_linearSolution(nums):
    max_so_far = nums[0]
    maxEndingHere = nums[0]
    for i in range(1, len(nums)):
        maxEndingHere = max(maxEndingHere + nums[i], nums[i])
        max_so_far = max(max_so_far, maxEndingHere)
    return max_so_far

def max_sub_Array_linearSolution2(nums):
    if len(nums) == 0:
        return 0
    max_ending_here = nums[0]
    max_so_far = -float('inf')
    for i in nums:
        max_so_far = max(i , max_so_far + i)
        if max_so_far > max_ending_here:
            max_ending_here = max_so_far
    return max_ending_here


ls = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sub_Array_CubicSolution(ls))
print(max_sub_Array_QuadraticSolution(ls))
print(max_sub_Array_linearSolution(ls))
print(max_sub_Array_linearSolution2(ls))
