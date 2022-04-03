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
https://leetcode-cn.com/submissions/detail/294009100/

95 / 99 个通过测试用例
状态：解答错误

输入：
[1]
1
输出：
0
预期：
1
"""
"""
(4)
"""
