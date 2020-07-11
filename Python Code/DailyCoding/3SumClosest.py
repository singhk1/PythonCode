'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

def three_sum_closest(nums, target):
    nums.sort()
    res = sum(nums[:3])
    for i in range(len(nums) - 2):
        j, k = i + 1, len(nums) - 1

        if nums[i] + nums[j] + nums[j + 1] >= target:
            k = j + 1
        if nums[i] + nums[k - 1] + nums[k] <= target:
            j = k - 1

        while j < k:
            sumnow = nums[i] + nums[j] + nums[k]
            if abs(sumnow - target) < abs(res - target):
                res = sumnow
            if sumnow < target:
                j += 1
            elif sumnow > target:
                k -= 1
            else:
                return sumnow
    return res


nums = [-1,2,1,-4]
target = 1
print(three_sum_closest(nums, target))
