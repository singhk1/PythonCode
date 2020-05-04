def minTaps(n, ranges):
        wranges = []
        for i, r in enumerate(ranges):
            wranges.append((i - r, i + r))
        # sorted wranges
        wranges = sorted(wranges)
        print(wranges)
        cur_end = 0
        next_end = 0
        res = 0
        for start, end in wranges:
            if start <= cur_end:
                next_end = max(end, next_end)
            elif start > next_end:
                return -1 # cannot cover area (next_end, start)
            else:
                # in the range between cur_end < pos <= next_end
                # take a step,
                res += 1
                cur_end = next_end
                next_end = max(end, next_end)
            # print((start, end), cur_end, next_end, res)
        if cur_end >= n:
            return res
        if next_end >= n:
            return res + 1
        return -1

n = 7
ranges = [1,2,1,0,2,1,0,1]
print(minTaps(n, ranges))
