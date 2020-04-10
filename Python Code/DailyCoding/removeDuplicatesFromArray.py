def removeDups(ls):
    i = 0
    while i < len(ls):
        if i + 1 == len(ls):
            break
        if ls[i] == ls[i + 1]:
            ls.pop(i)
            i = i - 1
        i = i + 1
    return ls

ls = [1,1,2]
print(removeDups(ls))
