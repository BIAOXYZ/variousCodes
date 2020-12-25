class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """

        g.sort()
        s.sort()
        
        res, i, j = 0, 0, 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                res += 1
                i += 1
                j += 1
            else:
                j += 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/133598508/

21 / 21 个通过测试用例
状态：通过
执行用时: 36 ms
内存消耗: 13.7 MB

执行用时：36 ms, 在所有 Python 提交中击败了96.53%的用户
内存消耗：13.7 MB, 在所有 Python 提交中击败了80.48%的用户
"""
