class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """

        # 感觉就是 LC300 最长递增子序列 的小变种，并且基本没啥变化。。。
        # 可以参见这个： https://leetcode-cn.com/submissions/detail/145896286/

        length = len(arr)
        dp = [1 for _ in range(length)]

        for i in range(1, length):
            for j in range(i):
                if arr[j] + difference == arr[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
        
"""
https://leetcode-cn.com/submissions/detail/235617960/

34 / 39 个通过测试用例
状态：超出时间限制
"""
