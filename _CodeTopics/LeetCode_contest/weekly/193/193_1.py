class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        length = len(nums)
        res = []
        sum = 0
        
        for i in range(length):
            sum += nums[i]
            res.append(sum)
        return res
    
"""
https://leetcode-cn.com/contest/weekly-contest-193/submissions/detail/78789034/

53 / 53 个通过测试用例
	状态：通过
执行用时：28 ms
内存消耗：12.8 MB
"""
