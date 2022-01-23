from collections import Counter
class Solution(object):
    def findLonely(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        ctr = Counter(nums)
        res = []
        for key in ctr.keys():
            if ctr[key] == 1 and key-1 not in ctr and key+1 not in ctr:
                res.append(key)
        return res
    
"""
https://leetcode-cn.com/submissions/detail/261452723/

75 / 75 个通过测试用例
状态：通过
执行用时: 380 ms
内存消耗: 36.5 MB
"""
