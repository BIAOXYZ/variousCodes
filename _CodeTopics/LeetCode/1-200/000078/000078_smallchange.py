class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(currSubset, pos):
            if pos == length:
                return
            for ind in range(pos, length):
                currSubset.append(nums[ind])
                res.append(currSubset[:])
                backtrack(currSubset, ind+1)
                currSubset.pop()

        length = len(nums)
        res = [[]]
        backtrack([], 0)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/109785196/

10 / 10 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 12.5 MB

执行用时：20 ms, 在所有 Python 提交中击败了66.33%的用户
内存消耗：12.5 MB, 在所有 Python 提交中击败了82.89%的用户
"""
