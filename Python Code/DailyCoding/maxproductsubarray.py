def max_product_subarray(nums):
    min_end = 0
    max_end = 0
    max_so_far = 0
    for i in nums:
        temp = max_end
        max_end = max(i, max(i*max_end, i*min_end))
        min_end = min(i, min(i*temp, i*min_end))
        max_so_far = max(max_so_far, max_end)
    return max_so_far

ls = [-6, 4, -5, 8, -10, 0, 8]
print(max_product_subarray(ls))
