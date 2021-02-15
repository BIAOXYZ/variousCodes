class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 最plain的想法：从每个位置开始遍历并计算最长递增子序列。但是这个有点类似回溯算法的行为，基本（我觉得是肯定）会超时。
        # 这里观察这么一个例子：[11,13,17,23]。对于任何一个位置上的数，只要在之前的位置上有更小的数，这个就不用考虑了。
        # 所以算法基本就是倒着来的动态规划。比如上面例子里假定已经算出了 dp[2] = 2，那么 dp[1] = dp[2] + 1。

        length = len(nums)
        dp = [1 for i in range(length)]

        for i in range(length-2, -1, -1):
            for j in range(i+1, length):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
        
"""
https://leetcode-cn.com/submissions/detail/145879953/

54 / 54 个通过测试用例
状态：通过
执行用时: 2516 ms
内存消耗: 13.2 MB

执行用时：2516 ms, 在所有 Python 提交中击败了37.88%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了90.92%的用户
"""
