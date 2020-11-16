class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """

        res = []
        for x in range(R):
            for y in range(C):
                res.append([x, y, abs(x-r0)+abs(y-c0)])
        res.sort(key = lambda elem : elem[2])
        res = [[res[i][0], res[i][1]] for i in range(len(res))]
        return res
        
"""
https://leetcode-cn.com/submissions/detail/123980529/

66 / 66 个通过测试用例
状态：通过
执行用时: 132 ms
内存消耗: 16.7 MB

执行用时：132 ms, 在所有 Python 提交中击败了65.22%的用户
内存消耗：16.7 MB, 在所有 Python 提交中击败了15.91%的用户
"""
