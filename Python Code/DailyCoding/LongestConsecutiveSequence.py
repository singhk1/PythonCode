def longest_sequence(nums):
    lo_seq = 0
    my_set = set(nums)

    for i in my_set:
        if i - 1 not in my_set:
            curr_num = i
            curr_seq = 1
            while curr_num + 1 in my_set:
                curr_num += 1
                curr_seq += 1
            lo_seq = max(lo_seq, curr_seq)
    return lo_seq


nums = [100, 4, 200, 1, 3, 2]
print(longest_sequence(nums))
nums = [0, 1]
print(longest_sequence(nums))
