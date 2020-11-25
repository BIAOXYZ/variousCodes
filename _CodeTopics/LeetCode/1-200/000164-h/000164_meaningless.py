class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 先不管题目里要求的“线性时间复杂度和空间复杂度”。

        nums.sort()
        length = len(nums)
        res = 0
        for i in range(1, length):
            res = max(res, nums[i]-nums[i-1])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/126285159/

18 / 18 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 13.7 MB

执行用时：16 ms, 在所有 Python 提交中击败了97.96%的用户
内存消耗：13.7 MB, 在所有 Python 提交中击败了33.33%的用户
"""
