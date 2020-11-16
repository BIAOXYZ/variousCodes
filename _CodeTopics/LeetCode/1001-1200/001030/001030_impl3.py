class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """

        # 也算是手动狗头题。另外这个实现的效率应该不如官方那个用list.sort()的，尤其是空间复杂度方面。
        return sorted([[x, y] for x in range(R) for y in range(C)], key = lambda elem : abs(elem[0]-r0) + abs(elem[1]-c0))
        
"""
https://leetcode-cn.com/submissions/detail/123981509/

66 / 66 个通过测试用例
状态：通过
执行用时: 124 ms
内存消耗: 15.3 MB

执行用时：124 ms, 在所有 Python 提交中击败了84.78%的用户
内存消耗：15.3 MB, 在所有 Python 提交中击败了45.45%的用户
"""
