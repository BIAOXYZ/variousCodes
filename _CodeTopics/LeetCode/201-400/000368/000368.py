class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nums.sort()
        length = len(nums)

        # dp[i] 表示以（排序过后的）第i个数结尾的最大整除子集的长度，那么开始时每个都只有自己，故为1。
        dp = [1 for _ in range(length)]
        for i in range(1, length):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
 
        maxLen = max(dp)
        res = [nums[dp.index(maxLen)]]
        currLen = maxLen - 1
        for i in range(length-1, -1, -1):
            if dp[i] == currLen and res[-1] % nums[i] == 0:
                res.append(nums[i])
                currLen -= 1
                if currLen == 0:
                    break
        res.reverse()
        return res
        
"""
https://leetcode-cn.com/submissions/detail/171554229/

48 / 48 个通过测试用例
状态：通过
执行用时: 320 ms
内存消耗: 12.9 MB

执行用时：320 ms, 在所有 Python 提交中击败了62.50%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了100.00%的用户
"""
