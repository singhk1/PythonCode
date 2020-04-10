def balancedString(s):
    res, counter = 0, 0
    for i in s:
        if i == 'L':
            counter += 1
        else:
            counter -= 1
        if counter == 0:
            res += 1
    return res

s = "RLRRLLRLRL"
print(balancedString(s))
