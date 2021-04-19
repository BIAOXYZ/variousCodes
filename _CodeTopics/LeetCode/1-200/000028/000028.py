class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if not needle:
            return 0
        len1, len2 = len(haystack), len(needle)
        if len1 < len2:
            return -1
        
        flag = True
        for i in range(len1 - len2 + 1):
            if haystack[i] != needle[0]:
                continue
            for j in range(1, len2):
                if haystack[i+j] != needle[j]:
                    flag = False
                    break
            if flag:
                return i
            else:
                flag = True
        return -1
        
"""
https://leetcode-cn.com/submissions/detail/169829419/

79 / 79 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13.8 MB

执行用时：24 ms, 在所有 Python 提交中击败了52.50%的用户
内存消耗：13.8 MB, 在所有 Python 提交中击败了28.56%的用户
"""
