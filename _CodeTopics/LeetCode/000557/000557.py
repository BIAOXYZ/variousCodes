class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        s = s[::-1]
        l = s.split()

        length = len(l)
        for i in range(length/2):
            l[i], l[length-1-i] = l[length-1-i], l[i]
        return ' '.join(l)
        
"""
https://leetcode-cn.com/submissions/detail/102927814/

30 / 30 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 14 MB
"""
"""
执行用时：20 ms, 在所有 Python 提交中击败了90.22%的用户
内存消耗：14 MB, 在所有 Python 提交中击败了15.72%的用户
"""
