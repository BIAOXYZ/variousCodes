class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """

        stk = []
        for ch in S:
            if not stk or stk[-1] != ch:
                stk.append(ch)
            else:
                stk.pop()
        return "".join(stk)
        
"""
https://leetcode-cn.com/submissions/detail/152744373/

98 / 98 个通过测试用例
状态：通过
执行用时: 52 ms
内存消耗: 13.8 MB

执行用时：52 ms, 在所有 Python 提交中击败了88.31%的用户
内存消耗：13.8 MB, 在所有 Python 提交中击败了23.98%的用户
"""
