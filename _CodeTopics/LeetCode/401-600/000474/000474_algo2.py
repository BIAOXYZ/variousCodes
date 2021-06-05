class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """

        # 参考答案的dp写法，该题是 0-1 背包的变种，需要用到三维数组来存储dp的中间状态。

        length = len(strs)
        dp = [[[0 for i in range(n + 1)] for j in range(m + 1)] for k in range(length + 1)]

        for i in range(1, length+1):
            zeros, ones = strs[i-1].count('0'), strs[i-1].count('1')
            for j in range(m+1):
                for k in range(n+1):
                    if zeros > j or ones > k:
                        dp[i][j][k] = dp[i-1][j][k]
                    else:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-zeros][k-ones] + 1)
        return dp[length][m][n]
        
"""
https://leetcode-cn.com/submissions/detail/184341681/

70 / 70 个通过测试用例
状态：通过
执行用时: 3488 ms
内存消耗: 61.3 MB

执行用时：3488 ms, 在所有 Python 提交中击败了25.41%的用户
内存消耗：61.3 MB, 在所有 Python 提交中击败了5.21%的用户
"""
