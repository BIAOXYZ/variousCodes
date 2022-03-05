class Solution(object):
    def mostFrequent(self, nums, key):
        """
        :type nums: List[int]
        :type key: int
        :rtype: int
        """
        
        n = len(nums)
        dic = {}
        for i in range(n-1):
            if nums[i] == key:
                target = nums[i+1]
                dic[target] = dic.setdefault(target, 0) + 1
        maxVal = max(dic.values())
        for k, v in dic.items():
            if v == maxVal:
                return k
    
"""
https://leetcode-cn.com/submissions/detail/277903847/

94 / 94 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.2 MB
"""
