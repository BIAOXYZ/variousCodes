import math
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """

        # 如果频率最高的字符长度超过总长的一半，肯定不行。
        dic = {}
        for ch in S:
            if dic.has_key(ch):
                dic[ch] += 1
            else:
                dic[ch] = 1
        freq = dic.values()
        maxFreq, summmation = max(freq), sum(freq)
        if maxFreq > math.ceil(summmation / 2.0):
            return ""

        # newS可以不用搞那么复杂的生成，昨晚太晚了只能把那么丑的先提交了。
        # 这里主要是利用了python的语法糖：字符串*数字，等于把那个字符串重复若干遍。
        newS = [k*v for k,v in dic.items()]
        newS.sort(key=lambda x:len(x), reverse=True)
        tmplists = [[] for i in range(maxFreq)]
        index = 0
        for string in newS:
            for ch in string:
                tmplists[index].append(ch)
                index = (index + 1) % maxFreq

        res = ""
        for lis in tmplists:
            res = res + "".join(lis)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/127407999/

62 / 62 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13.2 MB

执行用时：24 ms, 在所有 Python 提交中击败了48.15%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了10.00%的用户
"""
