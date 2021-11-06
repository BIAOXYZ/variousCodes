class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """

        minM, minN = m, n
        for op in ops:
            minM = min(minM, op[0])
            minN = min(minN, op[1])
        return minM * minN
        
"""
https://leetcode-cn.com/submissions/detail/236187426/

执行用时：20 ms, 在所有 Python 提交中击败了62.34%的用户
内存消耗：14 MB, 在所有 Python 提交中击败了44.16%的用户
通过测试用例：
69 / 69
"""
