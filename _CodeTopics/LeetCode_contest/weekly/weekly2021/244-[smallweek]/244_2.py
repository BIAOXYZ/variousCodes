class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ctr = collections.Counter(nums)
        keys = ctr.keys()
        keys.sort()
        
        res = 0
        for i in range(1, len(keys)):
            key = keys[i]
            res += ctr[key] * i
        return res
    
"""
https://leetcode-cn.com/submissions/detail/184389658/

78 / 78 个通过测试用例
状态：通过
执行用时: 300 ms
内存消耗: 21.3 MB
"""
