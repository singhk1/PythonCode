from collections import deque
class MaximumofKLenthSubArray:
    def max_of_subarray(self,ls, k):
        arr = []
        for i in range(len(ls) - k + 1):
            arr.append(max(ls[i: i + k]))
        return arr

    def max_of_subarray_deque(self, ls, k):
        q = deque()
        arr = []
        if len(ls) == 0:
            if k >= 0:
                return []
            else:
                return []
        for i in range(k):
            while q and ls[i] > ls[q[-1]]:
                q.pop()
            q.append(i)

        for i in range(k, len(ls)):
            arr.append(ls[q[0]])
            while q and q[0] <= i - k:
                q.popleft()
            while q and ls[i] >= ls[q[-1]]:
                q.pop()
            q.append(i)
        arr.append(ls[q[0]])
        return arr

obj = MaximumofKLenthSubArray()
ls = [10, 20, 2, 7, 8, 7]
print(obj.max_of_subarray(ls, 3))
ls2 = []
print(obj.max_of_subarray_deque(ls2, 0))
