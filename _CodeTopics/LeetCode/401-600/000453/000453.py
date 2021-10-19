class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 每次 n - 1 个元素加一，等价于每次 1 个元素减一。
        
        nums.sort()
        return sum([nums[i] - nums[0] for i in range(len(nums))])
        
"""
https://leetcode-cn.com/submissions/detail/230491830/

84 / 84 个通过测试用例
状态：通过
执行用时: 64 ms
内存消耗: 14.3 MB

执行用时：64 ms, 在所有 Python 提交中击败了15.56%的用户
内存消耗：14.3 MB, 在所有 Python 提交中击败了5.56%的用户
"""
