class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        def str_to_dict(s):
            dic = {}
            for ch in s:
                if ch in dic:
                    dic[ch] += 1
                else:
                    dic[ch] = 1
            return dic
        
        dicS, dicT = str_to_dict(s), str_to_dict(t)
        for k, v in dicT.items():
            if k not in dicS:
                return k
            elif v > dicS[k]:
                return k
        
"""
https://leetcode-cn.com/submissions/detail/131939320/

54 / 54 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.1 MB

执行用时：20 ms, 在所有 Python 提交中击败了81.42%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了16.14%的用户
"""
