from collections import deque
class BackSpace:
    def backspace_comp(self, S: str, T: str) -> bool:
        return self.build(S) == self.build(T)

    def build(self, string: str) -> str:
        res = deque()
        l = 0
        for i in string:
            if i == '#':
                if l > 0:
                    res.pop()
                    l -= 1
            else:
                res.append(i)
                l += 1
        return ''.join(list(res))


S ='ab##c'
T = 'ad#c'
bckspace = BackSpace()
print(bckspace.backspace_comp(S, T))
