class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        
        n = len(candies)
        candies.sort()
        res = 0
        if k <= sum(candies):
            res = 1
        if k <= n:
            res = max(res, candies[n-k])
        
        small, big = 0, candies[-1]
        while small <= big:
            mid = small + (big - small) / 2
            if mid == 0:
                break
            total = sum([candy / mid for candy in candies])
            if total < k:
                big = mid - 1
            elif total >= k:
                res = max(res, mid)
                small = mid + 1
        return res
    
"""
https://leetcode-cn.com/submissions/detail/294021151/

99 / 99 个通过测试用例
状态：通过
执行用时: 644 ms
内存消耗: 20.8 MB
"""
