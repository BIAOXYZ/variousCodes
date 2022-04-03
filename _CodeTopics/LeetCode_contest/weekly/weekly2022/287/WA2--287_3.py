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
https://leetcode-cn.com/submissions/detail/293999205/

36 / 99 个通过测试用例
状态：解答错误

输入：
[9,10,1,2,10,9,9,10,2,2]
3
输出：
9
预期：
10
"""
"""
(2)
"""
