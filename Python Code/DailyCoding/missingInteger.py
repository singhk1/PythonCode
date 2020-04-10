def missing_positive_integer(ls):
    if not ls:
        return 1
    for i, num in enumerate(ls):
        while i + 1 != ls[i] and 0 < ls[i] <= len(ls):
            v = ls[i]
            ls[i], ls[v - 1] = ls[v - 1], ls[i]
            if ls[i] == ls[v - 1]:
                break
    for i, num in enumerate(ls, 1):
        if num != i:
            return i
    return len(ls) + 1

def missing_positive_integer2(ls):
    s = set(ls)
    i = 1
    while i in s:
        i += 1
    return i



ls = [0, 1, -1, 3]
ls1 = [1, 2, 0]
print(missing_positive_integer(ls))
print(missing_positive_integer(ls1))
print(missing_positive_integer2(ls))
print(missing_positive_integer2(ls1))
