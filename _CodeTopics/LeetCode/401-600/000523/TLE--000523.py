class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        # 如果直接二重循环，并且每次循环里计算加法，就是 O(N^3) 的复杂度，应该肯定会超时。
        # 预计算前缀和的话就是 O(N^2)，应该还好。

        if not nums:
            return False
        prefixSum = [nums[0]]
        for i in range(1, len(nums)):
            prefixSum.append(prefixSum[-1] + nums[i])
        
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if i == 0:
                    if prefixSum[j] % k == 0:
                        return True
                elif i > 0:
                    if (prefixSum[j] - prefixSum[i-1]) % k == 0:
                        return True
        return False
        
"""
https://leetcode-cn.com/submissions/detail/183077977/

93 / 94 个通过测试用例
状态：超出时间限制
"""
