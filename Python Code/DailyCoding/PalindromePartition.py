def partition(s):
    valid_partition = []
    partition_inprogress = []
    partion_string(s, 0, partition_inprogress, valid_partition)
    return valid_partition

def is_palindrome(s, start, end):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


def partion_string(s, build_pointer, partition_inprogress, valid_partition):
    if build_pointer == len(s):
        valid_partition.append(partition_inprogress)
    else:
        for i in range(build_pointer, len(s)):
            if is_palindrome(s, build_pointer, i):
                palindromic_string = s[build_pointer: i+1]
                partition_inprogress.append(palindromic_string)
                partion_string(s, i + 1, partitioninprogress, valid_partition)
                partition_inprogress.remove(len(partition_inprogress) - 1)


s = "aab"
print(partition(s))
