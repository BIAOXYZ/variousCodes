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
        if len1 == 0 and len2 == 0:
            return True
        elif len1 == 0:
            if s2 == s3: return True
            else: return False
        elif len2 == 0:
            if s1 == s3: return True
            else: return False

        dp = [[False for i in range(len2 + 1)] for j in range(len1 + 1)]
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
https://leetcode-cn.com/submissions/detail/89326448/

101 / 101 个通过测试用例
状态：通过
执行用时：40 ms
内存消耗：12.7 MB
"""
"""
执行用时：40 ms, 在所有 Python 提交中击败了33.33%的用户
内存消耗：12.7 MB, 在所有 Python 提交中击败了100.00%的用户
"""
