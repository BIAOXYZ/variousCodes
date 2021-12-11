class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        n = len(nums)
        l = [[nums[i], i] for i in range(n)]
        l.sort(reverse=True)
        l2 = l[:k]
        l2.sort(key = lambda x : x[1])
        ##print l2
        res = [elem[0] for elem in l2]
        return res
    
"""
https://leetcode-cn.com/submissions/detail/247560233/

48 / 48 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13.3 MB
"""
