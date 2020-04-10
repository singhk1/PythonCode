import bisect

num = [1, 2, 3, 4]
seen = []
for mynum in num:
    i = bisect.bisect_left(seen, num)
    bisect.insort(seen, num)
    print(bisect.insort(seen,num))
