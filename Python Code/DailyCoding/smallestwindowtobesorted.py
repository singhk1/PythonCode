class windowtobesorted:
    def window(self,ls):
        start, end = None, None
        s = sorted(ls)

        for i in range(len(ls)):
            if ls[i] != s[i] and start is None:
                start = i
            elif ls[i] != s[i]:
                end = i
        return start, end

ls = [3, 7, 5, 6, 9]
wind = windowtobesorted()
print(wind.window(ls))
