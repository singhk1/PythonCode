def search(nums, target):
    ln = len(nums)
    left, right = 0, ln - 1

    while left <= right:
        mid = (left + right) // 2

        if target == nums[mid]:
            return mid
        elif nums[mid] >= nums[left]:
            if target <= nums[mid] and target >= nums[left]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if target >= nums[mid] and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums, target))
nums = [4,5,6,7,0,1,2]
target = 3
print(search(nums, target))
