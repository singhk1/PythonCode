def collatz(n):
    while n != 1:
        if n % 2 == 0:
            print(n // 2)
            return n // 2
        else:
            result = 3 * n + 1
            print(result)
            return result

n = input("Give me a number: ")
while n != 1:
    n = collatz(int(n))
