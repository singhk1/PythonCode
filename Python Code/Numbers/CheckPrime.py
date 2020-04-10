import math
def checkprime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                print("number is not prime")
                break
        else:
                print("number is prime")
    else:
        print("number is not prime")


def sieveoferatothenes(n):
    primes = []
    for i in range(2, n + 1):
        primes.append(i)

    i = 2
    while i <= int(math.sqrt(n)):
        if i in primes:
            for j in range(i * 2, n + 1, i):
                if j in primes:
                    primes.remove(j)
        i += 1
    return primes

def primesum(n):
    primes = sieveoferatothenes(n)
    primes_set = set(primes)
    for i in primes:
        j = n - i
        if j in primes_set:
            return i, j


n = 74
checkprime(n)
checkprime(55)
print("prime number between 2 and n")
print(sieveoferatothenes(n))
print(primesum(n))
