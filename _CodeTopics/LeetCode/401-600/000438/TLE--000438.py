from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        ctrP = Counter(p)
        res = []
        for i in range(len(s) - len(p) + 1):
            if Counter(s[i:i+len(p)]) == ctrP:
                res.append(i)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/242966583/

33 / 61 个通过测试用例
状态：超出时间限制
"""
