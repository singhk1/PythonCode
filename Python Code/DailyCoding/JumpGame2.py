'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''
def jump(nums):
    if len(nums) == 1:
        return 0
    max_range = nums[0]
    jumps = 0
    steps = nums[0]
    for i in range(1, len(nums) - 1):
        max_range = max(max_range, i + nums[i])
        print(str(max_range) + " printing ")
        steps -= 1

        if steps == 0:
            jumps += 1
            steps = max_range - i
        print(str(steps) + " steps ")
        print(str(jumps) + " jumps")
    return jumps + 1

def jump2(nums):
    step = max_far = curr_far = 0
    for i in range(len(nums)):
        if i > curr_far:
            curr_far = max_far
            step += 1
        max_far = max(max_far, i + nums[i])
        #print(i)
    return step


'''nums = [2,3,1,1,4]
print(jump(nums))
nums = [6, 2, 4, 0, 5, 1, 1, 4, 2, 9]
print(jump(nums))'''

nums = [2,3,1,1,4]
print(jump2(nums))
nums = [6, 2, 4, 0, 5, 1, 1, 4, 2, 9]
print(jump2(nums))
nums = [1,1,1,1]
print(jump2(nums))
