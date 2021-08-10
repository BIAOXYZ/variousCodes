import collections
class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 参照官方答案 动态规划 + 哈希表 实现。
        # 第一次碰到这种 dp 数组的元素是个字典的情况。
        
        length = len(nums)
        dp = [collections.defaultdict(int) for _ in range(length)]

        res = 0
        for endIndex in range(1, length):
            for secondLastIndex in range(endIndex):
                d = nums[endIndex] - nums[secondLastIndex]
                res += dp[secondLastIndex][d]
                dp[endIndex][d] += dp[secondLastIndex][d] + 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/205567052/

101 / 101 个通过测试用例
状态：通过
执行用时: 676 ms
内存消耗: 72.3 MB

执行用时：676 ms, 在所有 Python 提交中击败了65.22%的用户
内存消耗：72.3 MB, 在所有 Python 提交中击败了30.44%的用户
"""
