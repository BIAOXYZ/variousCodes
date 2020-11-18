class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        len1, len2 = len(str1), len(str2)
        shorterLen = min(len1, len2)
        
        # 如果某个前缀子串确实是两者的公约数，那么至少其长度是两者长度的公约数。
        for i in range(shorterLen, 0, -1):
            if len1 % i == 0 and len2 % i == 0:
                if str1[:i] * (len1 / i) == str1 and str1[:i] * (len2 / i) == str2:
                    return str1[:i]
        return ''
        
"""
https://leetcode-cn.com/submissions/detail/124533539/

114 / 114 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13 MB

执行用时：20 ms, 在所有 Python 提交中击败了71.60%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了12.35%的用户
"""
