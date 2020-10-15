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
        # 用下面这句肯定是对的，已经提交验证过了。所以试一试不转成list（也就是以deque的形式返回）看能不能过。我猜测是不能。。。
        # return list(res)        
        return res
        
"""
https://leetcode-cn.com/submissions/detail/116116038/

132 / 132 个通过测试用例
状态：通过
执行用时: 188 ms
内存消耗: 15.2 MB

执行用时：188 ms, 在所有 Python 提交中击败了98.27%的用户
内存消耗：15.2 MB, 在所有 Python 提交中击败了6.03%的用户
"""
"""
# 代码里最后的注释已经说明问题了。其实就是想试试返回的类型是list时，直接返回一个deque类型行不行。我猜不行，但是结果过了。我估计LeetCode平台可能有些转换之类的。
"""
