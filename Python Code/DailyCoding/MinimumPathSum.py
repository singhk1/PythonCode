import itertools
def minimum(nums):
    if not nums:
        return 0
    row = len(nums)
    col = len(nums[0])
    nums[0][:] = itertools.accumulate(nums[0])
    print(nums[0][:])
    for i in range(1, row):
        nums[i][0] += nums[i - 1][0]
        print(str(nums[i][0]) + " row")
        for j in range(1, col):
            nums[i][j] += min(nums[i - 1][j], nums[i][j - 1])
            print(str(nums[i][j]) + " column")
    return nums[-1][-1]

nums = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(minimum(nums))
