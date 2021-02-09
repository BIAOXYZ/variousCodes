class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        def str_to_dic(s):
            dic = {}
            for ch in s:
                dic[ch] = dic.setdefault(ch, 0) + 1
            return dic
        
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False
        
        dic1 = str_to_dic(s1)
        for i in range(len2 - len1 + 1):
            if s2[i] not in s1:
                continue
            dic2 = str_to_dic(s2[i:i+len1])
            if dic1 == dic2:
                return True
        return False
        
"""
https://leetcode-cn.com/submissions/detail/145037942/

103 / 103 个通过测试用例
状态：通过
执行用时: 3872 ms
内存消耗: 13.5 MB

执行用时：3872 ms, 在所有 Python 提交中击败了13.78%的用户
内存消耗：13.5 MB, 在所有 Python 提交中击败了23.98%的用户
"""
