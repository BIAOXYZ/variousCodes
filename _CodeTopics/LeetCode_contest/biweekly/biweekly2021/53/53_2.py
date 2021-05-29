class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # 最大值肯定要跟最小值结合。然后依次类推即可。
        n = len(nums)
        nums.sort()
        res = 0
        for i in range(n/2):
            res = max(res, nums[i] + nums[n-1-i])
        return res
    
"""
https://leetcode-cn.com/submissions/detail/182013482/

37 / 37 个通过测试用例
状态：通过
执行用时: 436 ms
内存消耗: 21.3 MB
"""
