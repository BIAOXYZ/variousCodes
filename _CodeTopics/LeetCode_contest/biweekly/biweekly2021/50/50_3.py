class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        
        length = len(nums)
        prefixXor = [nums[0]]
        for i in range(1, length):
            prefixXor.append(prefixXor[-1] ^ nums[i])
        
        maxnum = 2**(maximumBit) - 1
        res = []
        for i in range(length-1, -1, -1):
            res.append(maxnum ^ prefixXor[i])
        return res
    
"""
https://leetcode-cn.com/submissions/detail/169051582/

86 / 86 个通过测试用例
状态：通过
执行用时: 208 ms
内存消耗: 35 MB
"""
