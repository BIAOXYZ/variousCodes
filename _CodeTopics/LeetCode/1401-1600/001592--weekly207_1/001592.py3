class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """

        length = len(text)
        n_blanks = text.count(" ")
        lis = text.split()
        n_words = len(lis)
        if n_words == 1:
            return lis[0] + " " * n_blanks

        quotient, remainder = n_blanks // (n_words - 1), n_blanks % (n_words - 1)
        res = []
        for i in range(n_words-1):
            res.append(lis[i])
            res.append(" " * quotient)
        res.append(lis[-1])
        res.append(" " * remainder)
        return "".join(res)
        
"""
https://leetcode.cn/submissions/detail/360016409/

执行用时：
20 ms
, 在所有 Python 提交中击败了
50.00%
的用户
内存消耗：
13 MB
, 在所有 Python 提交中击败了
88.46%
的用户
通过测试用例：
89 / 89
"""
