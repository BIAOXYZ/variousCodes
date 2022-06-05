class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        nums.sort()
        
        res = 1
        currMin = nums[0]
        for i in range(1, n):
            if nums[i] - currMin > k:
                res += 1
                currMin = nums[i]
        return res
                
"""
https://leetcode.cn/submissions/detail/321752681/

92 / 92 个通过测试用例
状态：通过
执行用时: 164 ms
内存消耗: 24.8 MB
"""
