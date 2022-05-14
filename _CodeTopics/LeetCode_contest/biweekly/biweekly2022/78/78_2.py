class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # 其实没必要用前缀和了，不过写到半中间才发现，也懒得改了，继续写完
        
        n = len(nums)
        prefixSum = [0] * n
        prefixSum[0] = nums[0]
        for i in range(1, n):
            prefixSum[i] = prefixSum[i-1] + nums[i]
        
        res = 0
        for i in range(n-1):
            leftSum = prefixSum[i]
            rightSum = prefixSum[n-1] - prefixSum[i]
            if leftSum >= rightSum:
                res += 1
        return res
    
"""
https://leetcode.cn/submissions/detail/313512969/

100 / 100 个通过测试用例
状态：通过
执行用时: 136 ms
内存消耗: 24.7 MB
"""
