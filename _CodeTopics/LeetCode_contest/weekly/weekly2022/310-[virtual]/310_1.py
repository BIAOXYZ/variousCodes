class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ctr = Counter(nums)
        keys = ctr.keys()
        keys.sort(key = lambda x : (ctr[x], -x), reverse=True)
        for key in keys:
            if key & 1 == 0:
                return key
        return -1
    
"""
https://leetcode.cn/submissions/detail/361794931/

217 / 217 个通过测试用例
状态：通过
执行用时: 124 ms
内存消耗: 13.8 MB
"""
