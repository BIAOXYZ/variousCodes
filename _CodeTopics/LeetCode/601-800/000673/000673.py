class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 和官方答案稍有些不一样：
        ## 没有在遍历过程中维护 maxLen，即：“当前最长的递增子序列的长度”，以及该长度
        ## 目前对应的符合条件的上升子序列的数目。相反，从可读性的角度，选择最后一起计算。
        ## 但总体思路还是 LC300 最长递增子序列 的动态规划方法，可以先参考那里。

        length = len(nums)
        dp = [1 for _ in range(length)]
        ctr = [1 for _ in range(length)]

        for i in range(1, length):
            for j in range(i):
                if nums[j] < nums[i]:
                    # 如果有更长的递增子序列，就更新 dp[i] 以及 ctr[i]
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        ctr[i] = ctr[j]
                    # 如果有另外的位置 j 也能满足和 nums[i] 一起形成当前最长，则加上这部分。
                    elif dp[j] + 1 == dp[i]:
                        ctr[i] += ctr[j]
        
        maxLen = max(dp)
        res = 0
        for i in range(length):
            if dp[i] == maxLen:
                res += ctr[i]
        return res
        
"""
https://leetcode-cn.com/submissions/detail/221354388/

223 / 223 个通过测试用例
状态：通过
执行用时: 696 ms
内存消耗: 13.5 MB

执行用时：696 ms, 在所有 Python 提交中击败了47.32%的用户
内存消耗：13.5 MB, 在所有 Python 提交中击败了12.20%的用户
"""
