def rotate(ls, k):
    n = len(ls)
    for i in range(k):
        pre = ls[n - 1]
        for j in range(n):
            temp = ls[j]
            ls[j] = pre
            pre = temp
    return ls

def rotate2(ls, k):
    n = len(ls)
    a = [0 for i in range(n)]
    for i in range(n):
        a[(i + k) % n] = ls[i]
    nums = a
    return nums

def rotate3(ls, k):
    ln = len(ls)
    temp = ls[:ln - k]
    print("printing temp")
    print(temp)
    ls[:k] = ls[ln - k:]
    print("Printing ls")
    print(ls)
    ls[k:] = temp
    return ls

ls1 = [1, 2, 3, 4, 5, 6, 7]
ls2 = [1, 2, 3, 4, 5, 6, 7]
ls3 = [1, 2, 3, 4, 5, 6, 7]
print(ls1)
print(rotate(ls1, 4))
print(ls2)
print(rotate2(ls2, 4))
print(ls3)
print(rotate3(ls3, 4))
