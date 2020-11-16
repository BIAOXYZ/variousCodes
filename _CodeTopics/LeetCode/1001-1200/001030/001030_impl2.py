class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """

        res = [[x, y] for x in range(R) for y in range(C)]
        res.sort(key = lambda elem : abs(elem[0]-r0) + abs(elem[1]-c0))
        return res
        
"""
https://leetcode-cn.com/submissions/detail/123981437/

66 / 66 个通过测试用例
状态：通过
执行用时: 116 ms
内存消耗: 15.4 MB

执行用时：116 ms, 在所有 Python 提交中击败了97.83%的用户
内存消耗：15.4 MB, 在所有 Python 提交中击败了37.50%的用户
"""
