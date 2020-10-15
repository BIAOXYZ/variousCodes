class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        length = len(A)
        left, right = 0, length - 1

        # 其实这个属于很异类的双指针，因为left其实一直是0。
        while left < right:
            if abs(A[left]) > abs(A[right]):
                # 这里主要是插入到对应的位置，用insert总是会覆盖后面的值，所以只能这么来。。。
                A = A[:right+1] + [A[left]**2] + A[right+1:]
                A.pop(0)
                right -= 1
            else:
                A[right] = A[right]**2
                right -= 1
        # 最后循环出来，第一个元素也要再平方一下。
        A[0] = A[0]**2
        return A
        
"""
https://leetcode-cn.com/submissions/detail/116115362/

132 / 132 个通过测试用例
状态：通过
执行用时: 3092 ms
内存消耗: 15.1 MB

执行用时：3092 ms, 在所有 Python 提交中击败了5.19%的用户
内存消耗：15.1 MB, 在所有 Python 提交中击败了5.08%的用户
"""
