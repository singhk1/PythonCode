
def numofdecoding(s, total=0):
    if len(s) <= 1:
        return 1
    if s.startswith('0'):
        return 0

    total += numofdecoding(s[1:])
    if int(s[:2]) <= 26:
        total += numofdecoding(s[2:])

    return total


def helper(s, k, memo):
    if k == 0:
        return 1
    if s.startswith('0'):
        return 0
    if memo[k] != None:
        return memo[k]
    result = helper(s, k - 1, memo)
    if k >= 2 and int(s[:2]) <= 26:
        result += helper(s, k - 2, memo)
    memo[k] = result
    return result

def num_of_ways(s):
    memo = [None for i in range(len(s) + 1)]
    return helper(s, len(s), memo)

s1 = "111"
s2 = "010"
s3 = "30"
#print(numofdecoding(s1))
#print(numofdecoding(s2))
#print(numofdecoding(s3))
print(num_of_ways(s1))
print(num_of_ways(s2))
print(num_of_ways(s3))
