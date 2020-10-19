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
        if len1 == 0 or len2 == 0:
            return True
        
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
13 / 101 个通过测试用例
状态：解答错误

输入："a"
      ""
      "c"
输出：true
预期：false
"""
