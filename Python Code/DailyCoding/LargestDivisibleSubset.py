'''
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]
'''

def subset(nums):
    nums = sorted(nums)
    ln = len(nums)
    pre = [-1] * ln
    largest = [1] * ln

    for i in range(ln):
        for j in range(i + 1, ln):
            if nums[j] % nums[i] == 0:
                if largest[j] < largest[i] + 1:
                    largest[j] = largest[i] + 1
                    pre[j] = i
    most = -1
    for i in range(ln):
        if most == -1 or largest[i] > largest[most]:
            most = i

    if most == -1:
        return []

    result = []
    while pre[most] != -1:
        result.append(nums[most])
        most = pre[most]
    result.append(nums[most])

    return sorted(result)
def largestDivisibleSubset(nums):
    result = []
    if not nums:
        return result
    nums = sorted(nums)
    pre = [1] * len(nums)
    lon = [-1] * len(nums)

    max = 0
    max_index = -1
    for i in range(len(pre)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and pre[j] + 1 > pre[i]:
                pre[i]= pre[j] + 1
                lon[i] = j
        if max < pre[i]:
            max = pre[i]
            max_index = i

    while max_index >= 0:
        result.append(nums[max_index])
        max_index = lon[max_index]
    return sorted(result)

nums = [1, 2, 3]
print(subset(nums))
nums = [1, 2, 4, 8, 123, 5, 13, 312, 51]
print(subset(nums))
print(largestDivisibleSubset(nums))
