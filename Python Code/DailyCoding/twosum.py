def twosum(ls, target):
    s = dict()
    for i, num in enumerate(ls):
        x = target - num
        if x in s:
            return [s[x], i]
        s[num] = i
    return None

ls = [2, 7, 11, 15]
target = 9

print(ls, target)
