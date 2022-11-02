class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """

        m, n = len(word), len(sequence)
        if n < m:
            return 0
        elif n == m:
            return int(sequence == word)
        
        dp = [0] * n
        dp[n-m] = int(sequence[n-m:] == word)
        for i in range(n-m-1, -1, -1):
            if sequence[i:i+m] != word:
                dp[i] = 0
            else:
                dp[i] = dp[i+m] + 1
        return max(dp)
        
"""
https://leetcode.cn/submissions/detail/378853770/

执行用时：
12 ms
, 在所有 Python 提交中击败了
92.86%
的用户
内存消耗：
12.9 MB
, 在所有 Python 提交中击败了
71.43%
的用户
通过测试用例：
212 / 212
"""
