def even_digits(nums):
    count, digit = 0, 0

    for i in nums:
        while i > 0:
            i = i // 10
            digit += 1
        # print(digit)
        if digit % 2 == 0:
            count += 1
        digit = 0
    return count

# nums = [12,345,2,6,7896]
nums2 = [437,315,322,431,686,264,442]
# print(even_digits(nums))
print(even_digits(nums2))
