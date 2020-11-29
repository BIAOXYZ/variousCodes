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

        # 这段开始，太丑陋恶心了，要睡觉了，不管了，回头readme里总结。
        dic2 = {}
        for ch in S:
            if dic2.has_key(ch):
                dic2[ch].append(ch)
            else:
                dic2[ch] = [ch]
        newS = dic2.values()
        newS.sort(key=lambda x:len(x), reverse=True)
        newS_with_string_element = [''.join(lis) for lis in newS]
        newS = ""
        for string in newS_with_string_element:
            newS += string
        tmplists = [[] for i in range(maxFreq)]
        index = 0
        for ch in newS:
            tmplists[index].append(ch)
            index = (index + 1) % maxFreq
        
        res = ""
        for lis in tmplists:
            res = res + "".join(lis)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/127278320/

62 / 62 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 13 MB

执行用时：16 ms, 在所有 Python 提交中击败了85.19%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了36.25%的用户
"""
