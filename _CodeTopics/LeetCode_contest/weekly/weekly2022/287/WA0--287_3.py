class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        
        n = len(candies)
        candies.sort()
        if k <= n:
            return candies[n-k]
        
        res = 0
        small, big = 0, candies[-1]-1
        while small <= big:
            mid = small + (big - small) / 2
            if mid == 0:
                break
            total = sum([candy / mid for candy in candies])
            if total < k:
                big = mid - 1
            elif total >= k:
                res = max(res, mid)
                small += 1
        return res
    

"""
https://leetcode-cn.com/contest/weekly-contest-287/submissions/detail/293996172/
"""
