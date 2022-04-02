class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        
        res = 0
        while start > 0 or goal > 0:
            if start & 1 != goal & 1:
                res += 1
            start >>= 1
            goal >>= 1
        return res
    
"""
https://leetcode-cn.com/submissions/detail/293849919/

249 / 249 个通过测试用例
状态：通过
执行用时: 12 ms
内存消耗: 12.9 MB
"""
