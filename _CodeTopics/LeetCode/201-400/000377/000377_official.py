class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # 官方答案的dp还是简单多了。。。

        dp = [1] + [0 for _ in range(target)]
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]
        return dp[target]
        
"""
https://leetcode-cn.com/submissions/detail/171485756/

15 / 15 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13 MB

执行用时：24 ms, 在所有 Python 提交中击败了85.54%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了68.68%的用户
"""
