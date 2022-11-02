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
            dp[i] = dp[i+m] + int(sequence[i:i+m] == word)
        return max(dp)
        
"""
https://leetcode.cn/submissions/detail/378853435/

173 / 212 个通过测试用例
状态：解答错误

输入：
"baba"
"b"
输出：
2
预期结果：
1
"""
