class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        length = len(A)
        left, right = 0, length - 1

        # 其实这个属于很异类的双指针，因为left其实一直是0。
        while left <= right:
            if abs(A[left]) > abs(A[right]):
                A.insert(right+1, A[left]**2)
                A.pop(0)
            else:
                A[right] = A[right]**2
            right -= 1
        return A
        
"""
https://leetcode-cn.com/submissions/detail/116115734/

132 / 132 个通过测试用例
状态：通过
执行用时: 364 ms
内存消耗: 15.1 MB

执行用时：364 ms, 在所有 Python 提交中击败了5.93%的用户
内存消耗：15.1 MB, 在所有 Python 提交中击败了5.08%的用户
"""
