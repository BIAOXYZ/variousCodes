class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        length = len(nums)
        res = [[]]

        def backtrack(currSubset, pos):
            if pos == length:
                return
            for ind in range(pos, length):
                currSubset.append(nums[ind])
                res.append(currSubset[:])
                backtrack(currSubset, ind+1)
                currSubset.pop()

        backtrack([], 0)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/109783547/

10 / 10 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 12.6 MB

执行用时：16 ms, 在所有 Python 提交中击败了88.56%的用户
内存消耗：12.6 MB, 在所有 Python 提交中击败了46.58%的用户
"""
