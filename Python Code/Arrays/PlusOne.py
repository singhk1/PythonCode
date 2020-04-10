def plus_one(arr):
    newArr = []
    carry = 1
    for i in arr[::-1]:
        if i + carry < 10:
            newArr.append(i + carry)
            carry = 0
        else:
            newArr.append(0)
    if carry == 1:
        newArr.append(1)
    return newArr[::-1]


arr = [9,9,9]
print(plus_one(arr))
