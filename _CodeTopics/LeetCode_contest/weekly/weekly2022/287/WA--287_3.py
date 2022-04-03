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
https://leetcode-cn.com/contest/weekly-contest-287/submissions/detail/293996172/ 【开始以为不小心网页关了，后来发现没关，只是顺序放到第二次错误的提交后面了- -也就是下面这个】
https://leetcode-cn.com/submissions/detail/293996172/

27 / 99 个通过测试用例
状态：解答错误

输入：
[1,2,3,4,10]
5
输出：
1
预期：
3
"""
"""
(1)
"""
