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
            res = res or possibleDivide
        return res

"""
https://leetcode-cn.com/submissions/detail/81896303/

27 / 36 个通过测试用例
状态：超出时间限制

最后执行的输入：
"acaaaaabbbdbcccdcdaadcdccacbcccabbbbcdaaaaaadb"
["abbcbda","cbdaaa","b","dadaaad","dccbbbc","dccadd","ccbdbc","bbca","bacbcdd","a","bacb","cbc","adc","c","cbdbcad","cdbab","db","abbcdbd","bcb","bbdab","aa","bcadb","bacbcb","ca","dbdabdb","ccd","acbb","bdc","acbccd","d","cccdcda","dcbd","cbccacd","ac","cca","aaddc","dccac","ccdc","bbbbcda","ba","adbcadb","dca","abd","bdbb","ddadbad","badb","ab","aaaaa","acba","abbb"]
"""
