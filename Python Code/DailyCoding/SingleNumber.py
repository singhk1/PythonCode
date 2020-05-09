def single_number(nums):
    my_dict = {}
    for i, v in enumerate(nums):
        if v not in my_dict:
            my_dict[v] = 1
        else:
            my_dict[v] += 1
    for i in nums:
        if my_dict[i] == 1:
            return i
    return -1

nums = [4,1,2,1,2]
print(single_number(nums))
nums = [4,1,2,1,2, 4]
print(single_number(nums))
