class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        length = len(s)
        dp = [False] * (length + 1)
        dp[0] = True

        maxWordLen = 0
        for word in wordDict:
            maxWordLen = max(maxWordLen, len(word))
        
        for i in range(length):
            if dp[i] == True:
                for j in range(i+1, min(i+1+maxWordLen, length+1)):
                    if s[i:j] in wordDict:
                        dp[j] = True
        return dp[length]
        
"""
https://leetcode-cn.com/submissions/detail/82000162/

36 / 36 个通过测试用例
状态：通过
执行用时：28 ms
内存消耗：12.9 MB
"""
