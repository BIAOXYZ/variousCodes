class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        length = len(wordDict)
        res = False

        def isPrefix(string, word):
            lens = len(string)
            lenw = len(word)
            if lens < lenw:
                return False
            for i in range(lenw):
                if word[i] != string[i]:
                    return False
            return True

        for i in range(length):
            stripped_s = s[len(wordDict[i]):]
            # 这里有个小坑就是 stripped_s == '' 是不能少的，否则即使一个正确的结果，由于一直不断地
            # 剥离prefix，最终也会恰好变成空字符串，空串肯定是False。
            possibleDivide = isPrefix(s, wordDict[i]) and (stripped_s == '' or self.wordBreak(stripped_s, wordDict))
            if possibleDivide:
                return True
        return False

"""
https://leetcode-cn.com/submissions/detail/81911400/

29 / 36 个通过测试用例
状态：超出时间限制

最后执行的输入：
"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
"""
"""
# 对之前超时的代码中下面这两句进行了修改，其毛病就是必须要把每一个possibleDivide都算出来，其实根本没必要。
# 只要有一个是True就可以直接返回True了。
    res = res or possibleDivide
return res
"""
