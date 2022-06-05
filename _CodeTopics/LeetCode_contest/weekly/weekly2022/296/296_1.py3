class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return nums[0]
        
        newNums = [-1] * (n//2)
        for i in range(n//2):
            if i & 1 == 0:
                newNums[i] = min(nums[2*i+1], nums[2*i])
            else:
                newNums[i] = max(nums[2*i+1], nums[2*i])
        res = self.minMaxGame(newNums)
        return res
    
"""
https://leetcode.cn/submissions/detail/321743251/

96 / 96 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 15.1 MB
"""
