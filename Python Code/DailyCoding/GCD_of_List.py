from functools import reduce

def gcd(array):
    result = array[0]
    for i in array[1:]:
        if result < i:
            temp = result
            result = i
            i = temp
            print(str(i) + " " + str(temp) + " " + str(result))
        while i != 0:
            temp = i
            i = result % i
            result = temp
    return result

def gcd2(a, b):
    if a == 0:
        return b
    else:
        return gcd2(b % a, a)

array = [10, 45]
print(gcd(array))
gcd_2 = reduce(lambda x, y: gcd2(x, y), array)
print(gcd_2)
