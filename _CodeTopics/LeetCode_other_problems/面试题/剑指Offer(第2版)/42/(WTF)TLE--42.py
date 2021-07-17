class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)
        dp = [[0 for i in range(length)] for j in range(length)]
        maxElem = nums[0]

        for i in range(length):
            for j in range(i, length):
                if i == j:
                    dp[i][j] = nums[i]
                else:
                    dp[i][j] = dp[i][j-1] + nums[j]
                maxElem = max(maxElem, dp[i][j])
        return maxElem
        
"""
https://leetcode-cn.com/submissions/detail/196860639/

199 / 202 个通过测试用例
状态：超出时间限制
"""
"""
纯粹是被题目里的标签误解了，我就想着动态规划和前缀和都是O(N^2)的啊，怎么能不超时呢。。。但是题目标签里有，就写了。。。
"""
