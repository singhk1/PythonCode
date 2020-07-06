def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

        def get_median(nums, k):
            if k & 1:
                return nums[ k // 2]
            else:
                return (nums[k // 2] + nums[k // 2 - 1]) / 2

        res = []
        window = sorted(nums[:k])
        res.append(get_Median(window, k))

        for i in range(1, len(nums) - k + 1):
            window.pop(bisect_left(window, nums[i - 1]))
            insort(window, nums[i + k - 1])
            res.append(get_median(window, k))

        return res
