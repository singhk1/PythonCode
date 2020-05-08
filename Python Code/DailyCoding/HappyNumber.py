def is_happy(n):
    my_set = set()
    while n != 1:
        n = sum(int(i) ** 2 for i in str(n))
        if n in my_set:
            return False
        my_set.add(n)
    return True


n = 19
print(is_happy(n))
