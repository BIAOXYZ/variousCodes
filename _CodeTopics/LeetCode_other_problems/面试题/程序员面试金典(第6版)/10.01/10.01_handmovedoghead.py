class Solution(object):
    def merge(self, A, m, B, n):
        """
        :type A: List[int]
        :type m: int
        :type B: List[int]
        :type n: int
        :rtype: None Do not return anything, modify A in-place instead.
        """

        # 手动狗头题
        A[m:] = B
        A.sort()
        return A
        
"""
https://leetcode-cn.com/submissions/detail/110238252/

59 / 59 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 12.4 MB

执行用时：24 ms, 在所有 Python 提交中击败了48.68%的用户
内存消耗：12.4 MB, 在所有 Python 提交中击败了62.00%的用户
"""
