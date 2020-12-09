class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        """
        # 不浪费额外外层空间的一维dp版本。对比的是`000062_algo3.py`。
        """

        dp = [1 for i in range(n)]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[n-1]
        
"""
https://leetcode-cn.com/submissions/detail/129777996/

62 / 62 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 12.9 MB

执行用时：16 ms, 在所有 Python 提交中击败了83.71%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了43.09%的用户
"""
