class Trie:
    def __init__(self, k):
        self._trie = {}
        self.size = k

    def insert(self, item):
        trie = self._trie

        for i in range(self.size, -1, -1):
            bit = bool(item & (1 << i))
            if bit not in trie:
                trie[bit] = {}
            trie = trie[bit]

    def find_max_xor(self, item):
        trie = self._trie
        xor = 0

        for i in range(self.size, -1, -1):
            bit = bool(item & (1 << i))
            if (1 - bit) in trie:
                xor |= (1 << i)
                trie = trie[1 - bit]
            else:
                trie = trie[bit]
        return xor
class Solution:
    def findMaximumXOR(self, nums):
        k = max(nums).bit_length()
        trie = Trie(k)
        for i in nums:
            trie.insert(i)
        xor = 0
        for i in nums:
            xor = max(xor, trie.find_max_xor(i))
        return xor

    def findMaximumXOR2(self, nums):
        ans = 0
        mask = 0
        for i in range(30, -1, -1):
            mask |= 1<<i
            ans |= 1<<i
            S = set()
            for x in nums:
                y = x & mask
                if y ^ ans in S: break
                else: S.add(y)
            else: ans ^= 1<<i
        return ans

ls = [3,10,5,25,2,8]
sol = Solution()
print(sol.findMaximumXOR(ls))
print(sol.findMaximumXOR2(ls))
