class Solution(object):
    def is_word_breakable(self, s, wordDict):
        # 前一道题（LC139）和这个题基本一样，只是前一题只要求返回能否成功分割。
        # 这里完全就是 000139_algo2.py 代码复制过来了。
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
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        # 直接回溯的话，有些不能分割但是要匹配很久的用例太费时间。这里试试答案说的（但是答案没这么做）思路：
        # 先用动态规划确定一个字符串确实是可以分割的，然后再（用回溯）进行分割。但是我咋觉得还是悬呢？
        if not self.is_word_breakable(s, wordDict):
            return []
        
        res = []
        length = len(s)

        def backtrack(currWords, pos):
            if pos == length:
                res.append(currWords[:])
                return
            for i in range(1, length-pos+1):
                end = pos + i
                currStr = s[pos:end]
                if currStr in wordDict:
                    currWords.append(currStr)
                    backtrack(currWords, end)
                    currWords.pop()

        backtrack([], 0)
        res = [' '.join(elem) for elem in res]
        return res
        
"""
https://leetcode-cn.com/submissions/detail/120199922/

36 / 36 个通过测试用例
状态：通过
执行用时: 56 ms
内存消耗: 13.1 MB

执行用时：56 ms, 在所有 Python 提交中击败了28.40%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了17.39%的用户
"""
