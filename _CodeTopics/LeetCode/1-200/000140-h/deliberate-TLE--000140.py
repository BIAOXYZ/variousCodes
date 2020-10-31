class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        # 这个是纯回溯算法实现的，我感觉应该会超时。不然这题不可能算困难。。。
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
https://leetcode-cn.com/submissions/detail/120059096/

31 / 36 个通过测试用例
状态：超出时间限制

最后执行的输入：
"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
"""
