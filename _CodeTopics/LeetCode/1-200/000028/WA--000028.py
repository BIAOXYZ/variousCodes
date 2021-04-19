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
        
        pos = 0
        for i in range(len1):
            if haystack[i] == needle[pos]:
                pos += 1
                if pos == len2:
                    return i - len2 + 1
            else:
                pos = 0
        return -1
        
"""
https://leetcode-cn.com/submissions/detail/169829117/

66 / 79 个通过测试用例
状态：解答错误

输入：
"mississippi"
"issip"
输出：
-1
预期：
4
"""
