def min_partition(nums, n, n1, n2):
    if n < 0:
        return abs(n1 - n2)

    i = min_partition(nums, n - 1, n1 + nums[n], n2)
    j = min_partition(nums, n - 1, n1, n2 + nums[n])
    return min(i, j)


nums = [5, 10, 15, 20, 25]
nums2 = [5, 10, 15, 20]
nums3 = [1, 2, 3, 5]
print(min_partition(nums, len(nums) - 1, 0, 0) == 0)
print(min_partition(nums2, len(nums2) - 1, 0, 0) == 0)
print(min_partition(nums3, len(nums2) - 1, 0, 0) == 0)
