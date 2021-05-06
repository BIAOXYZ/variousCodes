class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """

        # 此题为第194周周赛第一题：
        # https://leetcode-cn.com/contest/weekly-contest-194/problems/xor-operation-in-an-array/
        # 原提交为：
        # https://leetcode-cn.com/contest/weekly-contest-194/submissions/detail/80711509/
        
        # 这个和过去代码一模一样。。。
        res = 0
        for i in range(n):
            res ^= start + 2*i
        return res
        
"""
https://leetcode-cn.com/submissions/detail/174969183/

54 / 54 个通过测试用例
状态：通过
执行用时: 8 ms
内存消耗: 13 MB

执行用时：8 ms, 在所有 Python 提交中击败了99.64%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了46.26%的用户
"""
