def circular_array_maxsum(nums):
    curr_max = 0
    final_max = 0
    for i in nums:
        curr_max += i
        if curr_max <= 0:
            curr_max = 0
        if final_max < curr_max:
            final_max = curr_max

    if final_max == 0:
        return max(nums)

    curr_min = 0
    final_min = 0
    for i in nums:
        curr_min += i
        if curr_min >= 0:
            curr_min = 0
        if final_min > curr_min:
            final_min = curr_min

    return max(final_max, sum(nums) - final_min)


lst = [8, -1, 3, 4]
print(circular_array_maxsum(lst))
lst = [-4, 5, 1, 0]
print(circular_array_maxsum(lst))
