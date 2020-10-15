class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        # 手动狗头题
        return sorted(num * num for num in A)
        
"""
https://leetcode-cn.com/submissions/detail/116115803/

132 / 132 个通过测试用例
状态：通过
执行用时: 180 ms
内存消耗: 15.2 MB

执行用时：180 ms, 在所有 Python 提交中击败了100.00%的用户
内存消耗：15.2 MB, 在所有 Python 提交中击败了6.03%的用户
"""
