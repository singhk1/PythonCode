def jump(nums):
    check = 1
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] >= check:
            check = 1
        else:
            check += 1
    return check == 1

nums = [2,3,1,1,4]
print(jump(nums))
