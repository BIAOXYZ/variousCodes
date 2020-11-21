class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        def str_to_dic(s):
            if not s:
                return {}
            dic = {}
            for ch in s:
                if ch in dic:
                    dic[ch] += 1
                else:
                    dic[ch] = 1
            return dic
        
        return str_to_dic(s) == str_to_dic(t)
        
"""
https://leetcode-cn.com/submissions/detail/125245647/

34 / 34 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13.7 MB

执行用时：24 ms, 在所有 Python 提交中击败了96.41%的用户
内存消耗：13.7 MB, 在所有 Python 提交中击败了36.82%的用户
"""
