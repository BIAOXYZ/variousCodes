class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        # 手动狗头题
        for i, elem in enumerate(A):
            A[i] = elem ** 2
        A.sort()
        return A
        
"""
https://leetcode-cn.com/submissions/detail/116110234/

132 / 132 个通过测试用例
状态：通过
执行用时: 192 ms
内存消耗: 14.8 MB

执行用时：192 ms, 在所有 Python 提交中击败了96.05%的用户
内存消耗：14.8 MB, 在所有 Python 提交中击败了5.08%的用户
"""
