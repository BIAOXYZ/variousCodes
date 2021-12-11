class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        return sum(sorted(nums, reverse=True)[:k])
    
"""
https://leetcode-cn.com/submissions/detail/247557340/

0 / 48 个通过测试用例
状态：解答错误

输入：
[2,1,3,3]
2
输出：
6
预期：
[3,3]
"""
