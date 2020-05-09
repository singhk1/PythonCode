'''
GIven a positive integer num, write a function to check if the number is a
perfect square.

'''

def valid_square(num):
    if num < 2:
        return True

    l, r = 2, num

    while l <= r:
        mid = l + (r - l) // 2
        if mid ** 2 == num:
            return True
        elif mid **2 > num:
            r = mid - 1
        else:
            l = l + 1
    return False


num = 16
print(valid_square(num))
num = 14
print(valid_square(num))
