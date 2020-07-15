class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # 这三句少不了，其实官方答案n=0的时候直接index out of range了。
        if n == 0: return 1
        elif n == 1: return 1
        elif n == 2: return 2

        dp = [0 for i in range(n+1)]
        dp[0], dp[1], dp[2] = 1, 1, 2

        for i in range(3,n+1):
            for j in range(1,i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]
        
"""
https://leetcode-cn.com/submissions/detail/88077474/

19 / 19 个通过测试用例
状态：通过
执行用时：24 ms
内存消耗：12.9 MB
"""
"""
执行用时：24 ms, 在所有 Python 提交中击败了31.69%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了33.33%的用户
"""
