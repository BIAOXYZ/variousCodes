class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        # 记忆化搜索。
        # 官方的python3实现又一次用到了python3的functools模块里的lru_cache()，但是python2没有。
        # （其实是有些类似的，但是LC应该不支持。。。）所以只能自己手动存函数的计算结果。。。

        res = []
        length = len(s)

        dic = {}
        wordSet = set(wordDict)

        def backtrack(pos):
            if pos in dic:
                return dic[pos]
            if pos == length:
                return [[]]
            res = []
            for end in range(pos+1, length+1):
                currStr = s[pos:end]
                if currStr in wordSet:
                    tmplist = backtrack(end)
                    for wordlist in tmplist:
                        res.append([currStr] + wordlist)
            dic[pos] = res
            return res

        res = backtrack(0)
        res = [' '.join(elem) for elem in res]
        return res
        
"""
https://leetcode-cn.com/submissions/detail/120540983/

36 / 36 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.6 MB

执行用时：20 ms, 在所有 Python 提交中击败了96.05%的用户
内存消耗：13.6 MB, 在所有 Python 提交中击败了8.09%的用户
"""
