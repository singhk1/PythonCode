
class solution:
    def reverse(self, x: int) -> int:
        int_range = range(-2**31, 2**31-1)
        if x not in int_range:
            rev = 0
        elif x < 0:
            rev = -1 * int(str(x)[::-1][:-1])
        else:
            rev = int(str(x)[::-1])
        return rev if rev in int_range else 0


number1 = -321
number2 = 123
number3 = 0

solu = solution()
print(solu.reverse(number1))
print(solu.reverse(number2))
print(solu.reverse(number3))
