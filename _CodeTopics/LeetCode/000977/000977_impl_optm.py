from collections import deque
class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        # 需要额外空间的双指针算法（我之前的是直接在A上操作，并且左指针其实一直不动）
        length = len(A)
        left, right = 0, length-1
        res = deque([])

        while left <= right:
            if abs(A[left]) > abs(A[right]):
                res.appendleft(A[left]**2)
                left += 1
            else:
                res.appendleft(A[right]**2)
                right -= 1
        return list(res)
        
"""
https://leetcode-cn.com/submissions/detail/116115997/

132 / 132 个通过测试用例
状态：通过
执行用时: 196 ms
内存消耗: 15.1 MB

执行用时：196 ms, 在所有 Python 提交中击败了89.38%的用户
内存消耗：15.1 MB, 在所有 Python 提交中击败了6.03%的用户
"""
"""
# 用了deque果然比普通的list快不少~
"""
