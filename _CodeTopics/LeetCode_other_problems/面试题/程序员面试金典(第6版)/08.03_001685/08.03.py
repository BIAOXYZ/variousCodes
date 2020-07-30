class Solution(object):
    def findMagicIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)
        res = []
        for i in range(length):
            if nums[i] == i:
                res.append(i)
        return -1 if not res else min(res)
        
"""
https://leetcode-cn.com/submissions/detail/93169514/

29 / 29 个通过测试用例
状态：通过
执行用时：32 ms
内存消耗：13.3 MB
"""
"""
执行用时：32 ms, 在所有 Python 提交中击败了20.21%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了50.00%的用户
"""
