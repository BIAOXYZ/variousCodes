class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        dicS, dicT = {}, {}
        for i in range(len(s)):
            if not dicS.has_key(s[i]) and not dicT.has_key(t[i]):
                dicS[s[i]] = t[i]
                dicT[t[i]] = s[i]
            elif not dicS.has_key(s[i]) or not dicT.has_key(t[i]):
                return False
            else:
                if dicS[s[i]] != t[i] or dicT[t[i]] != s[i]:
                    return False
        return True
        
"""
https://leetcode-cn.com/submissions/detail/133944359/

32 / 32 个通过测试用例
状态：通过
执行用时: 40 ms
内存消耗: 14 MB

执行用时：40 ms, 在所有 Python 提交中击败了33.04%的用户
内存消耗：14 MB, 在所有 Python 提交中击败了64.09%的用户
"""
