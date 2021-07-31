class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """

        rows = len(mat)
        tmpList = [(i, sum(mat[i])) for i in range(rows)]
        tmpList.sort(key = lambda x : (x[1], x[0]))
        res = [tmpList[i][0] for i in range(k)]
        return res
        
"""
https://leetcode-cn.com/submissions/detail/201866937/

52 / 52 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.1 MB

执行用时：20 ms, 在所有 Python 提交中击败了82.54%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了84.13%的用户
"""
