import bisect
def smaller_elements(ls):
    result = []
    for i, num in enumerate(ls):
        count = sum(val < num for val in ls[i + 1:])
        result.append(count)
    return result

def smaller_elements2(ls):
    result = []
    seen = []
    for num in reversed(ls):
        i = bisect.bisect_left(seen, num)
        result.append(i)
        bisect.insort(seen, num)
    #print(list(result))
    return list(reversed(result))


lis = [3, 4, 9, 6, 1]
#print(smaller_elements(lis))
print(smaller_elements2(lis))
