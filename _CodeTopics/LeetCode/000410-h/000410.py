class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        """
        # dp[i][j]表示 nums 中前 i 个数分成 j 组时，各个子数组和的最大值中最小的那个值。
        那么最终只要一步步拓展到 dp[length][m] 即可。
        # 转移公式可以考虑枚举k，使得前k个数分成 j-1 段，k+1到i的数是第 j 段。那么新的
        dp[i][j]在以k为划分时，各个子数组和的最大值 就是下面两个数中较大的那个：
        dp[k][j-1] 和 sum(nums[k+1],...,nums[i])
        同时注意k的取值应该是从 j-1 到 i-1 （官方答案里是0到i-1，不够优化）
        此外，dp[0][0]应该是0。
        """

        sysMaxInt = 9223372036854775807
        length = len(nums)
        prefixSum = [0]
        for i in range(length):
            prefixSum.append(prefixSum[-1] + nums[i])
        dp = [[sysMaxInt for i in range(m+1)] for j in range(length+1)]
        

        # 任何dp[i][j]只要 j>i 肯定就不能分割，因为要求非空子数组。
        for i in range(length+1):
            for j in range(min(i,m)+1):
                if i == 0 and j == 0:
                    dp[i][j] = 0
                elif i == 0:
                    continue
                elif j == 0:
                    continue
                else:
                    for k in range(j-1,i):
                        dp[i][j] = min(dp[i][j], max(dp[k][j - 1], prefixSum[i] - prefixSum[k]))
        return dp[length][m]
        
"""
https://leetcode-cn.com/submissions/detail/91428260/

27 / 27 个通过测试用例
状态：通过
执行用时：3380 ms
内存消耗：12.9 MB
"""
"""
执行用时：3380 ms, 在所有 Python 提交中击败了10.43%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了100.00%的用户
"""
