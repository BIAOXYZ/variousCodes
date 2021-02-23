class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        # 手动狗头题
        return [[1 - elem for elem in row[::-1]] for row in A]
        
"""
https://leetcode-cn.com/submissions/detail/148137653/

82 / 82 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 12.9 MB

执行用时：28 ms, 在所有 Python 提交中击败了96.37%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了93.23%的用户
"""
