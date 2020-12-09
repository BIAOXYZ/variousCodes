class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        """
        # 接着就是一维dp，也就是状态压缩版本的dp（或者带滚动数组的dp）。具体到这个题来说，虽然是二维格子，
        # 但是其实不需要所有格子对应的dp值都存储，只需要存一行或者一列的dp值就够了。下面代码以列为例（列的代码写起来更直观些）。
        """

        dp = [1 for i in range(n+1)]
        
        for i in range(2, m+1):
            for j in range(2, n+1):
                dp[j] += dp[j-1]
        return dp[n]
        
"""
https://leetcode-cn.com/submissions/detail/129771534/

62 / 62 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 13 MB

执行用时：28 ms, 在所有 Python 提交中击败了14.68%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了26.55%的用户
"""
