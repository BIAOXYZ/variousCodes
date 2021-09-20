class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 这个是官方答案动态规划实现里的做法，这里的dp[i]意思是“以位置i上的数为结尾时，形成的最长递增子序列的长度”。
        # 而我的前一个实现 `000300.py` 里的dp[i]是以位置i的数为开头时最长递增子序列的长度（所以那个外层循环要倒着来）。

        length = len(nums)
        dp = [1 for i in range(length)]

        for i in range(1, length):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
        
"""
https://leetcode-cn.com/submissions/detail/145896286/

54 / 54 个通过测试用例
状态：通过
执行用时: 2576 ms
内存消耗: 13.6 MB

执行用时：2576 ms, 在所有 Python 提交中击败了26.99%的用户
内存消耗：13.6 MB, 在所有 Python 提交中击败了6.64%的用户
"""
