def search(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + ((right - left) >> 1)
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

nums = [4, 5, 6, 7, 0, 1, 2]
print(search(nums))
