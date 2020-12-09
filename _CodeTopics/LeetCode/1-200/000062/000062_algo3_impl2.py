class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        """
        # 不浪费额外外层空间的一维dp版本的另一个实现，这次以行为例。
        # 对比下上一个以列为例的实现 `000062_algo3_impl.py` 就会发现这俩基本是对称的。
        """

        dp = [1 for i in range(m)]
        
        for j in range(1, n):
            for i in range(1, m):
                dp[i] += dp[i-1]
        return dp[m-1]
        
"""
https://leetcode-cn.com/submissions/detail/129869567/

62 / 62 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.1 MB

执行用时：20 ms, 在所有 Python 提交中击败了64.09%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了13.60%的用户
"""
