'''
Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)



Example 1:

Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3
'''

def sum_subarray(nums):
    curr_max = 0
    final_max = 0

    for i in nums:
        curr_max += i
        if curr_max <= 0:
            curr_max = 0
        if final_max < curr_max:
            final_max = curr_max
    if final_max == 0:
        return max(A)

    curr_min = 0
    final_min = 0

    for i in nums:
        curr_min += i
        if curr_min <= 0:
            curr_min = 0
        if final_min > curr_min:
            final_min = curr_min
    return max(final_max, sum(nums) - final_min)


nums = [1,-2,3,-2]
print(sum_subarray(nums))
