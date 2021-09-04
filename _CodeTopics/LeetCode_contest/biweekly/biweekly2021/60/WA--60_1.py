class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        if n == 1: return 0
        
        for i in range(1, n-1):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        
        if sum(nums[:n-1]) == 0:
            return n-1
        else:
            return -1
        
"""
https://leetcode-cn.com/submissions/detail/215207189/

283 / 294 个通过测试用例
状态：解答错误

最后执行的输入：
[4,0]
输入：
[4,0]
输出：
-1
预期：
0
"""
