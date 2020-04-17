def max_consecutive_ones(nums):
    result = 0
    count = 0
    for i in nums:
        if i == 1:
            count += 1
        else:
            result = max(result, count)
            count = 0
    return max(result, count)

nums = [1,1,0,1,1,1]
print(max_consecutive_ones(nums))
