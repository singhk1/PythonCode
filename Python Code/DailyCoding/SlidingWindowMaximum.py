'''
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
'''

from collections import deque
def max_of_subarray(nums, k):
    q = deque()
    res = []
    for i in range(k):
        while q and nums[i] >= nums[q[-1]]:
            q.pop()
        q.append(i)
    for i in range(k, len(nums)):
        res.append(nums[q[0]])
        while q and q[0] < i - k:
            q.popleft()
        while q and nums[i] >= nums[q[-1]]:
            q.pop()
        q.append(i)
    res.append(nums[q[0]])
    return res

nums, k = [1,3,-1,-3,5,3,6,7], 3

print(max_of_subarray(nums, k))
