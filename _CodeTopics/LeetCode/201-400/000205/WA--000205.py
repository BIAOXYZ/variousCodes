class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        dic = {}
        for i, ch in enumerate(s):
            if not dic.has_key(ch):
                dic[ch] = t[i]
            else:
                if dic[ch] != t[i]:
                    return False
        return True
        
"""
https://leetcode-cn.com/submissions/detail/133944072/

27 / 32 个通过测试用例
状态：解答错误

输入：
"ab"
"aa"
输出：
true
预期：
false
"""
