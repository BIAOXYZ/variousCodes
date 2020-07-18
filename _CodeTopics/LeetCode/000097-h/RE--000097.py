class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        len1, len2, len3 = len(s1), len(s2), len(s3)
        if len3 != len1 + len2:
            return False
        
        dp = [[False for i in range(len1 + 1)] for j in range(len2 + 1)]
        dp[0][0] = True

        for i in range(0, len1 + 1):
            for j in range(0, len2 + 1):
                pos = i + j - 1
                if i > 0:
                    dp[i][j] = dp[i][j] or (s3[pos] == s1[i-1] and dp[i-1][j])
                if j > 0:
                    dp[i][j] = dp[i][j] or (s3[pos] == s2[j-1] and dp[i][j-1])
        return dp[len1][len2]
        
"""
https://leetcode-cn.com/submissions/detail/89148266/

4 / 101 个通过测试用例
状态：执行出错

执行出错信息：Line 21: IndexError: list index out of range
最后执行的输入："a"
               ""
               "a"
"""
